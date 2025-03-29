import pathlib
import time
from urllib.parse import urlparse
import utils
from colorama import Fore
from settings import FFMPEG_PART_LIST, CONVERT_TO_MP4, CONVERT_RESOLUTION_TO_360P, OUTPUT_FILE_EXT, MIN_LOG
import ffmpeg

LPRE = "<-DOWNLOAD_PARTS->:"


def get_part_urls_from_m3u8_file(file_path=pathlib.Path("test.file"), root_url="/"):
    urls = []
    root_url = root_url.rstrip("/") + "/"
    with open(file_path) as file:
        while line := file.readline():
            if not line.startswith("#"):
                urls.append(str(root_url) + line.strip())
    return urls


def download_m3u8_and_its_parts(m3u8_url="", out_dir=pathlib.Path("./m3u8/")):
    m3u8_file_path = pathlib.Path(out_dir, utils.get_filename_from_url(m3u8_url))
    utils.download_file_by_url(m3u8_url, m3u8_file_path)

    parsed_url = urlparse(m3u8_url)
    part_urls = get_part_urls_from_m3u8_file(
        m3u8_file_path,
        f'{parsed_url.scheme}://{parsed_url.netloc}' + str(pathlib.Path(parsed_url.path).parent)
    )

    dln_pool = utils.DownloadThreaded(out_dir, 16)

    for url in part_urls:
        dln_pool.download_by_url(str(url))

    dln_pool.start_downloading()
    dln_pool.wait_till_end()
    if not MIN_LOG:
        print(LPRE,
              f"download_m3u8_and_its_parts({m3u8_url}, {out_dir}) \n\r\t-- {Fore.GREEN}download_finished.{Fore.RESET}")
    return m3u8_file_path


def gen_ffmpeg_part_list(output_file_path=pathlib.Path("./PartList.txt"), paths_list=None):
    if paths_list is None:
        paths_list = list()
    with open(output_file_path, "w") as file:
        for path in paths_list:
            if pathlib.Path(path).exists():
                file.write(f"file '{str(path)}'\n")
            else:
                print(LPRE,
                      f"gen_ffmpeg_part_list({output_file_path}, []) \n\r\t-- {Fore.RED}Video Part didn't exist: file {str(path)}{Fore.RESET}")
                break
    return output_file_path


def download_video_from_m3u8(m3u8_url, temp_dir, video_out_path):
    temp_dir = temp_dir.resolve()

    # m3u8_file_path = pathlib.Path(temp_dir, utils.get_filename_from_url(m3u8_url))
    m3u8_file_path = download_m3u8_and_its_parts(m3u8_url, temp_dir)
    time.sleep(10)

    # wrong usage of function # TODO: solve this mistake
    part_paths = get_part_urls_from_m3u8_file(m3u8_file_path, str(temp_dir))

    part_list_path = pathlib.Path(temp_dir, FFMPEG_PART_LIST)
    gen_ffmpeg_part_list(part_list_path, part_paths)

    video_output_file = str(video_out_path.resolve())

    if CONVERT_TO_MP4:
        video_output_file = video_output_file.rstrip(OUTPUT_FILE_EXT) + "mp4"
        (
            ffmpeg
            .input(str(part_list_path.resolve()), format='concat', safe=0)
            .output(video_output_file, c='copy')
            .run(overwrite_output=True)
        )
    else:
        (
            ffmpeg
            .input(str(part_list_path.resolve()), format='concat', safe=0)
            .output(video_output_file, c='copy')
            .run(overwrite_output=True)
        )

    if CONVERT_RESOLUTION_TO_360P:
        out360p = video_output_file.rsplit(".", 1)
        out360p = out360p[0] + "_360p." + out360p[1]
        (
            ffmpeg
            .input(video_output_file)
            .output(out360p, vf='scale=-2:360', vcodec='libx264', crf=23, preset='veryslow', acodec='copy')
            .run(overwrite_output=True)
        )
