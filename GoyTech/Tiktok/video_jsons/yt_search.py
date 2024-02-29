import scrapetube
import json
from random import shuffle


def get_videos(channel_name, filename):
    video_list = []
    videos = []

    for channel in channel_name:
        channel_videos = scrapetube.get_channel(
            channel_username=channel, content_type="shorts"
        )
        videos.append(channel_videos)

    for video in videos:
        for vid in video:
            video_id = vid["videoId"]
            url = f"https://youtube.com/watch?v={video_id}"
            video_list.append(url)

    with open(filename, "w", encoding="utf-8") as f:
        [shuffle(video_list) for _ in range(10)]
        shuffle(video_list)
        shuffle(video_list)
        shuffle(video_list)
        to_write = json.dumps(video_list)
        f.write(to_write)


# WBgood)
# wildberries_shmotki
# wildberries_shmot
# ohwowwb (контент для молоденьких няшек зумерок)
# winplay2218 (ахуенный пример ультрашаблонного контента который легко автоматизировать и который заебись собирает (за 128 видосов 13к подписоты в тг, почти все видосы стабильно 2-3к просмотров)(для пиздинга надо прикрывать везде вотерку в верхней части экрана)
# wb_shmot (в рандом месте экрана и на рандом моменте видео вылетает их вотерка)
# Wbeshka1 (норм контент но почему то не набирает)
# topgameapk
# DEMIXOVA
# Just_Kati
if __name__ == "__main__":
    get_videos(
        channel_name=["sencalkapimi1505"],
        filename="turk_seriali.json",
    )
    get_videos(
        channel_name=["Top10BestHit"],
        filename="turk_ru_film.json",
    )
    get_videos(
        channel_name=["serialselina"],
        filename="ru_turk_films.json",
    )

# 1. https://www.youtube.com/@youamoore/shorts
# 2. https://www.youtube.com/@sitadah9916 (турецкие сериалы и эдиты с певцом джони)
# 3. https://www.youtube.com/@AveTurkTV (дохуя топ шортсов)
# 4. https://www.youtube.com/@serialselina
# 5. https://www.youtube.com/@Top10BestHit
# 6. https://www.youtube.com/@Elizaveta_Semina/shorts
# 7. https://www.youtube.com/@turetskaya.skazka/shorts
# 8. https://www.youtube.com/@sencalkapimi1505

# get_videos(
#     channel_name=["Wbeshka1", "topgameapk"],
#     filename="WbSuperSaver.json",
# )
# get_videos(
#     channel_name=[
#         "AveTurkTV",
#         "sitadah9916",
#         "serialselina",
#         "turetskaya.skazka",
#     ],
#     filename="topturkfilm.json",
# )
# get_videos(
#     channel_name=[
#         "youamoore",
#         "Top10BestHit",
#         "sencalkapimi1505",
#     ],
#     filename="topturkishfilm.json",
# )

# get_videos(
#     channel_name=["wildberries_shmotki", "WBgood", "topgameapk"],
#     filename="wbdiscount.json",
# )
# get_videos(
#     channel_name=["Wbeshka1", "wildberries_shmot"],
#     filename="bestwbsales.json",
# )

# ТУРЕЦКИЕ СЕРИАЛЫ


# ВБ ТОВАРЫ

# 1. [https://www.youtube.com/shorts/vN6LfsATFwc](https://www.youtube.com/@WBgood)
# 2. https://www.youtube.com/@wildberries_shmotki
# 3. https://www.youtube.com/@wildberries_shmot
# 7. https://www.youtube.com/@Wbeshka1 (норм контент но почему то не набирает)
# 8. https://www.youtube.com/@topgameapk
# ==============================================================================
# try:
#     length = video.get("lengthText").get("simpleText")
#     if len(length.split(":")) == 3:
#         continue
#     else:
#         time_obj = datetime.strptime(length, "%M:%S")
#     time_in_seconds = time_obj.minute * 60 + time_obj.second

#     if time_in_seconds > 60:
#         continue
#     else:
# download_video(name=video_id, url=url)
# except Exception:
#     continue

# videos = scrapetube.get_search(
#     query="турецкие сериалы на русском shorts",
#     sort_by="view_count",
#     results_type="video",
#     limit=100,
# )
