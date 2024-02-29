# def pa():
#     filenames = [
#         (
#             f"video_jsons/{list(group_link.values())[0]}.json",
#             list(group_link.keys())[0],
#         )
#         for group_link in group_links
#     ]
#     video_urls = []

#     for filename, _ in filenames:
#         try:
#             with open(filename, "r") as f:
#                 video_urls.append(json.loads(f.read()))
#         except json.decoder.JSONDecodeError:
#             print(f"Файл {filename} закончился")
#             continue

#     for items in zip_longest(*video_urls):
#         for i, url in enumerate(items):
#             if url is not None:
#                 filename, group_link = filenames[i]
#             # zalu(data=(group_link, filename, url))
#             schedule_post(data=(group_link, filename, url), scheduler=video_scheduler)
