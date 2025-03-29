import pathlib

from settings import *
from download_parts import download_video_from_m3u8
from utils import get_filename_from_url


def gen_temp_and_video_paths(film_name="", m3u8_url=""):
    filename, fileext = get_filename_from_url(file_url).split(".")[:2]

    temp = OUTPUT_TEMP_DIR.replace(FILMNAME_STR, film_name)
    temp = temp.replace(FILENAME_STR, filename)
    temp = temp.replace(FILEEXT_STR, fileext)

    video = OUTPUT_VIDEO_PATH.replace(FILMNAME_STR, film_name)
    video = video.replace(FILENAME_STR, filename)
    video = video.replace(FILEEXT_STR, OUTPUT_FILE_EXT)

    return pathlib.Path(temp), pathlib.Path(video)


for filmname, file_url in VIDEO_DATA:
    print(f"\n\n\n{filmname}")
    temp_dir, video_path = gen_temp_and_video_paths(filmname, file_url)
    print(f"{filmname} -- temp_dir: {temp_dir}; video_path: {video_path};")
    download_video_from_m3u8(file_url, temp_dir, video_path)
    print("\n\n\n")
