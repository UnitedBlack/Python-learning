import os, sys, subprocess
from tt_config import get_random_videofile_name


def get_video_duration(video_path):
    cmd = [
        "video/editor/ffprobe",
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        video_path,
    ]
    duration = subprocess.check_output(cmd).decode("utf-8")
    return float(duration)


def edit_video(input_video, banner="video/editor/banner_gif/banner.gif"):
    duration_first_video = get_video_duration(input_video)
    output_path = f"video/editor/temp/{get_random_videofile_name()}.mp4"
    command = [
        "ffmpeg",
        "-y",
        "-i",
        input_video,
        "-i",
        banner,
        "-filter_complex",
        f"[0:v]scale=1080:1920[v0];[1:v]scale=320:180,trim=duration={duration_first_video}[v1];[v0][v1]overlay=x=45:y=1320",
        "-preset",
        "ultrafast",
        "video/editor/temp/output_to_meta.mp4",
    ]
    clear_metadata_command = [
        "ffmpeg",
        "-y",
        "-i",
        "video/editor/temp/output_to_meta.mp4",
        "-map_metadata",
        "-1",
        "-map_metadata:s:v",
        "-1",
        "-map_metadata:s:a",
        "-1",
        "-c:v",
        "copy",
        "-c:a",
        "copy",
        output_path,
    ]
    print(f"Editing video: {input_video}")
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Clearing metadata")
    subprocess.run(
        clear_metadata_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    os.remove(input_video)
    os.remove("video/editor/temp/output_to_meta.mp4")
    return output_path


if __name__ == "__main__":
    edit_video("video/editor/temp/ВБ выбор победителей_output.mp4.mp4")
