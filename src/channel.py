import json
import os
from googleapiclient.discovery import build
# import isodate

class Channel:
    '''Класс ютюб канала'''
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала.
         Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel_info = self.get_channel_info()
        self.title = self.channel_info["items"][0]["snippet"]["title"]
        self.desc = self.channel_info["items"][0]["snippet"]["description"]
        self.url = "https://www.youtube.com/channel/" + self.__channel_id
        self.channel_subs_count = self.channel_info["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel_info["items"][0]["statistics"]["videoCount"]
        self.channel_views = self.channel_info["items"][0]["statistics"]["viewCount"]

    # создать специальный объект для работы с API
    api_key = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        printj(channel)

    def get_channel_info(self):
        """Получение информации о канале"""
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        return channel

    @classmethod
    def get_service(cls, api_key):
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, filename):
        """Выводит словарь в json-подобном удобном формате с отступами"""
        with open(filename, 'w') as file:
            json.dump(self.channel_info, file)

def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))






