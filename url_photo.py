
import requests
import json
from config import data
from config import headers
from config import cookies
from logger import log_enter_exit
from logger import logger

from aiogram.types import InputMediaPhoto





@log_enter_exit
def _write_urls(query, value):
    logger.info(f"QUERY: {query}, VALUE: {value}")

    index = 0
    bookmark = ""
    tg_list = []
    urls_list = []
    list_range_10 = []
    stop = False

    while not stop:
        data_now = {
            'source_url': '/search/pins/',
            "data": json.dumps(data(query, bookmark))
        }

        response = requests.post('https://ru.pinterest.com/resource/BaseSearchResource/get/', cookies=cookies(), headers=headers(), data=data_now)
        if response.status_code == 200: logger.info(response)
        else: logger.warning(response)

        json_file = response.json()

        if "bookmark" in json_file["resource_response"]:
            bookmark = json_file["resource_response"]["bookmark"]
        else:
            tg_list.append(urls_list)
            tg_list.append(f"удалось найти не все фотографии")
            return tg_list


        for result in json_file["resource_response"]["data"]["results"]:
            if index >= value:
                stop = True
                urls_list.append(list_range_10.copy())
                break

            if len(list_range_10) == 10:
                urls_list.append(list_range_10.copy())
                list_range_10.clear()
            url = result["images"]["orig"]["url"]
            if url.endswith((".jpg", ".jpeg")):
                list_range_10.append(InputMediaPhoto(media=url))
                index += 1

            # img_src = result["images"]["orig"]["url"]
            # print(img_src)

    tg_list.append(urls_list)
    tg_list.append("отправка заершена")
    return tg_list


