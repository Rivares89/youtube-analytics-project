import os
from googleapiclient.discovery import build
import json


class Video:
    '''Класс видео из ютюба'''
    api_key = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, video_id):
        self.video_id = video_id
        self.title = self.get_video_info()["items"][0]["snippet"]["title"]
        self.video_url = f'https://www.youtube.com/watch?v=' + self.video_id
        self.viewCount = self.get_video_info()["items"][0]["statistics"]["viewCount"]
        self.likeCount = self.get_video_info()["items"][0]["statistics"]["likeCount"]

    def __str__(self):
        return f'{self.title}'
    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        video = self.youtube.videos().list(id=self.video_id, part='snippet,statistics').execute()
        print(json.dumps(video, indent=2, ensure_ascii=False)) #выводит в читаемом виде json-формат

    def get_video_info(self):
        """Получение информации о канале"""
        video = self.youtube.videos().list(id=self.video_id, part='snippet,statistics').execute()
        return video

class PLVideo(Video):
    '''Класс по плейлистам'''
    api_key = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
        self.title = self.get_video_info()["items"][0]["snippet"]["title"]
        self.video_url = f'https://www.youtube.com/watch?v=' + self.video_id
        self.viewCount = self.get_video_info()["items"][0]["statistics"]["viewCount"]
        self.likeCount = self.get_video_info()["items"][0]["statistics"]["likeCount"]

    def __str__(self):
        return f'{self.title}'

    def print_inf(self) -> None:
        """Выводит в консоль информацию о канале."""
        video = self.youtube.videos().list(id=self.video_id, part='snippet,statistics').execute()
        print(json.dumps(video, indent=2, ensure_ascii=False)) #выводит в читаемом виде json-формат
