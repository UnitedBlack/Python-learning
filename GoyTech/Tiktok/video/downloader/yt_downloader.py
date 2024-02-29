import subprocess
import glob


# def get_file_extension(path):
#     return os.path.splitext(path)[1]


# def download_video(url):
#     path = f"video/editor/temp/{url.replace('https://youtube.com/watch?v=', '')}"
#     command = ["yt-dlp", "-o", path, url]
#     subprocess.run(command)
#     time.sleep(10)
#     extension = get_file_extension(path)
#     print(f"File extension: {extension}")
#     return path
def download_video(url):
    path = (
        f"video/editor/temp/{url.replace('https://youtube.com/watch?v=', '')}.%(ext)s"
    )
    command = ["yt-dlp", "-o", path, url]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    actual_path = glob.glob(path.replace("%(ext)s", "*"))[0]
    print(f"Downloaded video to path: {actual_path}")
    return actual_path


# def download_video(url):
#     ydl_opts = {
#         "outtmpl": f"video/editor/temp/{url.replace('https://youtube.com/watch?v=', '')}.%(ext)s"
#     }
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])
# actual_path = glob.glob(ydl_opts['outtmpl'].replace("%(ext)s", "*"))[0]
# return actual_path


# import yt_dlp
# import os, time


# def download_video(url):
#     downloaded_file_path = None

#     def my_hook(d):
#         nonlocal downloaded_file_path
#         if d["status"] == "finished":
#             # file_tuple = os.path.split(os.path.abspath(d["filename"]))
#             # dirt_path = f"{file_tuple[0]}\{file_tuple[1]}"
#             # downloaded_file_path = dirt_path.replace("\\", "/")
#             # print(" AAAAAA ", d["filename"])
#             downloaded_file_path = d["filename"]

#     ydl_opts = {
#         "outtmpl": f"video/editor/temp/{url.replace('https://youtube.com/watch?v=', '')}",
#         "progress_hooks": [my_hook],
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])
#     print(downloaded_file_path)
#     return downloaded_file_path


# download_video("https://youtube.com/watch?v=CRE_dCBVbvk")
# https://www.youtube.com/shorts/CRE_dCBVbvk
