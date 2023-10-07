import json
import os
from googleapiclient.discovery import build

# import isodate

api_key: str = os.getenv('YOUTUBE_API_KEY')
# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


class
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        pass
