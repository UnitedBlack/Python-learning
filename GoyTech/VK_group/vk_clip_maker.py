import subprocess
import os
import hashlib


def get_video_duration(video_path):
    cmd = [
        "editor/ffprobe",
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


def edit_video(input_video, banner="editor/banner_gif/banner.gif"):
    duration_first_video = get_video_duration(input_video)
    hash_input_path = hashlib.sha1(input_video.encode()).hexdigest()[:8]
    output_path = f"editor/temp/{hash_input_path}_output.mp4"
    command = [
        "editor/ffmpeg",
        "-y",
        "-i",
        input_video,
        "-i",
        banner,
        "-filter_complex",
        f"[0:v]scale=1080:1920[v0];[1:v]scale=320:180,trim=duration={duration_first_video}[v1];[v0][v1]overlay=x=45:y=1385",
        "-preset",
        "ultrafast",
        "editor/temp/output_to_meta.mp4",
    ]
    clear_metadata_command = [
        "editor/ffmpeg",
        "-y",
        "-i",
        "editor/temp/output_to_meta.mp4",
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
    subprocess.run(command)
    subprocess.run(clear_metadata_command)
    os.remove("editor/temp/output_to_meta.mp4")
    return output_path


if __name__ == "__main__":
    edit_video("editor/temp/input.mp4")
