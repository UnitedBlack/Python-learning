from video.downloader import yt_downloader
from video.editor import video_maker
import json, os, calendar, time, yt_uploader
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from random import randint
from apscheduler.schedulers.background import BackgroundScheduler
from yt_config import youtube_accounts


def zalu(data):
    account, video_url = data
    print(account)
    download_path = yt_downloader.download_video(url=video_url)
    edited_path = video_maker.edit_video(input_video=download_path)
    yt_uploader.upload_yt(account_name=account, input_file=edited_path)
    os.remove(edited_path)
    with open("video_jsons/already_uploaded.json", "r+") as file:
        old_data = json.loads(file.read())
        old_data.append(video_url)
        file.seek(0)
        file.write(json.dumps(old_data))
        file.truncate()
    with open(f"video_jsons/{account}.json", "r") as file:
        old_data = json.loads(file.read())
    with open(f"video_jsons/{account}.json", "w") as file:
        file.write(json.dumps(old_data[1:]))
    print("Posted", datetime.now())


def schedule_post(data, scheduler):
    random_minute = randint(1, 50)
    try:
        day, month, year, hour, minute = get_free_time(scheduler)
    except TypeError:
        return
    scheduler.add_job(
        zalu,
        CronTrigger(day=day, hour=hour, minute=random_minute, month=month, year=year),
        args=[data],
    )


def get_free_time(scheduler, get_allowed=False):
    jobs = scheduler.get_jobs()
    current_day = datetime.now().day
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_hour = datetime.now().hour
    minute = 0
    allowed_hours_dict = {}
    days_in_month = calendar.monthrange(current_year, current_month)[1]
    if current_hour >= 22:
        if days_in_month < current_day + 1:
            current_day = 1
            current_month += 1
        else:
            current_day += 1
    for day in range(current_day, days_in_month + 1):
        allowed_hours = set(range(9, 25, 2))
        if current_hour < 10 and day == current_day or current_hour >= 22:
            allowed_hours = set(range(9, 25, 2))
        else:
            if day != current_day:
                allowed_hours = set(range(10, 23))
            else:
                allowed_hours = set(range(max(current_hour + 1, 10), 23))
        for job in jobs:
            run_time = job.next_run_time
            if (
                run_time
                and run_time.day == day
                and run_time.month == current_month
                and run_time.year == current_year
            ):
                hour_job_time = int(
                    datetime.strptime(str(run_time), "%Y-%m-%d %H:%M:%S%z").strftime(
                        "%H"
                    )
                )
                allowed_hours.discard(hour_job_time)
        allowed_hours_dict[day] = list(allowed_hours)
    if get_allowed:
        return current_day, current_month, current_year, allowed_hours_dict
    else:
        while current_day <= days_in_month:
            if allowed_hours_dict[current_day]:
                return (
                    current_day,
                    current_month,
                    current_year,
                    min(allowed_hours_dict[current_day]),
                    minute,
                )
            current_day += 1

        return None


def start():
    schedulers = {name: BackgroundScheduler() for name in youtube_accounts}
    [scheduler.start() for scheduler in schedulers.values()]
    for _ in range(10000):
        for account in youtube_accounts:
            filename = f"video_jsons/{account}.json"
            try:
                with open(filename, "r") as file:
                    video_url = json.loads(file.read())
                with open("video_jsons/already_uploaded.json", "r") as file:
                    uploaded_videos = json.loads(file.read())
                if video_url in uploaded_videos:
                    with open(filename, "w") as file:
                        file.write(json.dumps(video_url[1:]))
                    continue
                schedule_post(
                    data=(account, video_url[0]),
                    scheduler=schedulers[account],
                )
                # zalu(
                #     data=(account, video_url[0]),
                # )
            except Exception as e:
                print(e)
                continue
    [scheduler.print_jobs() for scheduler in schedulers.values()]
    print("Загрузил задачи, вхожу в бесконечный цикл")
    while True:
        time.sleep(1)


if __name__ == "__main__":
    start()
