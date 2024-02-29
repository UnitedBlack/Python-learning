# День 2
# доделать открытие жсон файла с каждым названием жсон саба - V
# и проверкой на айди постов, - X
# если есть то ничего не происходит, если нет то скачивается  - X
# сделать запись этих данных в жсон - X
# также если пост онли текст проверки - X
# в отдельном файле подключить тг бота - X
# сделать загрузку галереи - V
# сделать загрузку гиф - V

# День 3
# Доделать функцию чтения/записи айди файлов
# Переписать ее на асинхронную
# Доделать обработку текстовых постов
# Сделать гига пиздатый словарь {author_name: {"media_path"}} итд


# Использование aiohttp.ClientSession(): Вместо создания новой сессии для каждого запроса, 
# лучше создать одну сессию и использовать её для всех запросов. 
# Это увеличит производительность, поскольку сессия управляет пулом соединений 
# и может повторно использовать уже открытые соединения, 
# что уменьшает накладные расходы на установку нового соединения stackoverflow.com, stackoverflow.com.

            # media_info = {
            #     'media_type': "text",
            #     'media_path': os.path.join(text_folder, f"{post['data']['author']}.txt"),
            #     'post_text': post['data']['title']
            # }
            #         return {
            # 'media_type': "image",
            # 'media_path': os.path.join(image_folder, filename),
            # 'post_text': post['data']['title']}
            
            
            
        # if os.path.exists(filename):
        #     async with aiofiles.open(filename, mode='r') as f:
        #         data = await f.read()
        #     posts = json.loads(data)
        #     if post_id in posts:
        #         return True
        # return False
        