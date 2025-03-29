import pathlib
import threading
import time
import urllib.request
import urllib.parse
from csv import excel

from colorama import Fore
from settings import MIN_LOG

# from concurrent.futures import ThreadPoolExecutor, as_completed # TODO: implement DownloadThreaded using this

LPRE = "<-UTILS.PY->:"


def get_filename_from_url(url):
    parsed_url = urllib.parse.urlparse(url)
    return parsed_url.path.split('/')[-1]


def download_file_by_url(url="", output_file=pathlib.Path("./download.out")):
    if not MIN_LOG:
        print(LPRE, f"download_file_by_url({url}, {output_file}) \n\r\t-- {Fore.YELLOW}starting download;{Fore.RESET}")
    if output_file.exists():
        if MIN_LOG:
            print("*", end="")
        else:
            print(LPRE, f"download_file_by_url({url}, {output_file}) \n\r\t-- {Fore.RED}file exists;{Fore.RESET}")
        return

    output_file.parent.resolve().mkdir(parents=True, exist_ok=True)
    while True:
        try:
            local_filename, headers = urllib.request.urlretrieve(url, output_file)
            break
        except Exception as e:
            print(LPRE, f"download_file_by_url({url}, {output_file}) \n\r\t-- {Fore.RED}{str(e)}{Fore.RESET}")
            pass

    if MIN_LOG:
        print("+", end="")
    else:
        print(LPRE,
              f"download_file_by_url({url}, {output_file}) \n\r\t-- {Fore.GREEN}Download finished;{Fore.RESET} -- filename: {local_filename}")


class DownloadThreaded:
    def _local_download_thread(self, dln_url, dln_out):
        download_file_by_url(dln_url, dln_out)
        self.threads_count -= 1

    def _controller_thread(self):
        while len(self.dln_list) > 0 and self.run:
            time.sleep(0.1)
            try:
                if self.threads_count < self.thread_max_count:
                    dln_url, dln_out = self.dln_list[0]
                    del self.dln_list[0]
                    threading.Thread(target=self._local_download_thread, args=(dln_url, dln_out)).start()
                    self.threads_count += 1

            except KeyboardInterrupt:
                print(LPRE, f"DownloadThreaded:\n\r\t",
                      f"{Fore.RED}-- Download Pool stopped:By KeyboardInterrupt;{Fore.RESET}.")
                self.run = False
                print("/n/n/n/stop", self.run, self.threads_count)
        self.run = False

    def __init__(self, output_dir_path=pathlib.Path("./ThreadedDownload/"), thread_max_count=4):
        self.run = False
        self.thread_max_count = thread_max_count
        self.out_dir = output_dir_path

        self.dln_list = []
        self.threads_count = 0

        self.lock = threading.Lock()
        self.out_dir.resolve().mkdir(parents=True, exist_ok=True)
        self.controller_thread = None  # Initialize as None

    def download_by_url(self, url=""):
        output_file = pathlib.Path(self.out_dir, get_filename_from_url(url))
        self.dln_list.append((url, output_file))
        if not MIN_LOG:
            print(LPRE, f"DownloadThreaded:download_by_url({url}):",
                  f"\n\r\t{Fore.YELLOW}-- New download url registered to download pool.{Fore.RESET} -- with output file: {output_file}")

    def start_downloading(self):
        if self.controller_thread is None or not self.controller_thread.is_alive():
            self.run = True
            self.controller_thread = threading.Thread(target=self._controller_thread)
            self.controller_thread.start()
        else:
            print(LPRE, f"DownloadThreaded:start_downloading():",
                  f"\n\r\t{Fore.RED}- cant start new downloading thread. old one is still running{Fore.RESET}.")

    def wait_till_end(self):
        if self.controller_thread and self.controller_thread.is_alive():
            self.controller_thread.join()
