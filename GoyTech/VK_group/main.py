import yt_downloader, vk_uploader
import json
import vk_clip_maker
import os
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from random import randint
from apscheduler.schedulers.background import BackgroundScheduler
import calendar
from itertools import zip_longest
import time
from ast import literal_eval
from pprint import pprint

clip_description = "Ссылка на канал: t.me/WBgirlsbot"

group_links = [
    {"https://vk.com/wbdiscount": "wbdiscount"},  #  Лучшие скидки WB
    {"https://vk.com/bestwbsales": "bestwbsales"},  #  WB для девушек
    {"https://vk.com/topturkishfilm": "topturkishfilm"},  #  Сериалы Турции
    {"https://vk.com/topturkfilm": "topturkfilm"},  #  Турецкие сериалы
]


def zalu(data):
    vk_group_url, video_url = data
    download_path = yt_downloader.download_video(url=video_url)
    edited_path = vk_clip_maker.edit_video(input_video=download_path)
    vk_uploader.upload_vk_clips(
        input_file=edited_path,
        vk_url=vk_group_url,
        description_text=clip_description,
    )
    os.remove(download_path)
    os.remove(edited_path)
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
    schedulers = {list(name.values())[0]: BackgroundScheduler() for name in group_links}
    [scheduler.start() for scheduler in schedulers.values()]
    for _ in range(10):
        for group in group_links:
            group_name = list(group.values())[0]
            group_url = list(group.keys())[0]
            filename = f"video_jsons/{group_name}.json"
            try:
                with open(filename, "r") as file:
                    video_url = json.loads(file.read())
                # schedule_post(
                #     data=(group_url, video_url[0]),
                #     scheduler=schedulers[group_name],
                # )
                zalu(
                    data=(group_url, video_url[0]),
                )
                with open(filename, "w") as file:
                    file.write(json.dumps(video_url[1:]))
            except Exception as e:
                print(e)
                continue
    print("Загрузил задачи, вхожу в бесконечный цикл")
    while True:
        time.sleep(1)


# не забыть убрать несколько ссылок на видео чтобы одно и то же не лило

if __name__ == "__main__":
    start()

# Яппи захурить, мб тт, мб шортсы, но надо добавлять эффекты
# Разобраться с хуйней что кривые видео остаются кривыми, хотя мб в вк клипах проблема
# можно собрать источники и зашафлить чтобы рандом видосы лились
