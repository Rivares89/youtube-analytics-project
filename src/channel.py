import json
import os
from googleapiclient.discovery import build
# import isodate

class Channel:
    '''Класс ютюб канала'''
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel_id = 'UCwHL6WHUarjGfUM_586me8w'  # HighLoad Channel

    # создать специальный объект для работы с API
    api_key = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        printj(channel)

def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


