import os
from datetime import datetime
from datetime import timedelta
from googleapiclient.discovery import build
import json
import isodate


class PlayList:
    '''Класс плейлиста ютюб'''
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.title = self.get_channel_info()["items"][0]["snippet"]["title"]
        self.url = "https://www.youtube.com/playlist?list="+self.get_channel_info()["items"][0]["id"]

    # создать специальный объект для работы с API
    api_key = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)


    def get_channel_info(self):
        """Получение информации о канале"""
        playlist = self.youtube.playlists().list(id=self.playlist_id, part='snippet').execute()
        return playlist
    def print_inf(self) -> None:
        """Выводит в консоль информацию о плейлисте."""
        playlist = self.youtube.playlists().list(id=self.playlist_id, part='snippet').execute()
        print(json.dumps(playlist, indent=2, ensure_ascii=False)) #выводит в читаемом виде json-формат

    def total_duration(self):
        playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()
        duration_count = []
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            duration_count.append(duration)
        total_duration = sum(duration_count, datetime.timedelta())
        print(total_duration)

    def show_best_video(self):
        playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id,
                                                            part='contentDetails',
                                                            maxResults=50,
                                                            ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        better_video = int(0)
        like = 0
        for id_video in video_ids:
            video_response = PlayList.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                            id=id_video).execute()
            like_count: int = video_response['items'][0]['statistics']['likeCount']
            if int(like_count) > int(better_video):
                better_video = int(like_count)
                like = video_response
        return f"https://www.youtube.com/results?search_query="+like['items'][0]['id']
        #
        #
        # video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
        #                                        id=video_id
        #                                        ).execute()
        # printj(video_response)
def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))