import os
import requests
import deezer

class Client(deezer.Client):
    """
    Wrapper class for the deezer.Client class
    For now, we download everything locally
    """

    def __init__(self):
        super().__init__()

        if not "static" in os.listdir():
            os.mkdir("static")

    def download_track(self, track_id: int, filename: str) -> None:
        """
        Download a track from Deezer
        :param track_id: The id of the track to download
        :param filename: The name of the file to save the track to
        :return: None
        """
        if not f"track_{track_id}.mp3" in os.listdir("static"):
            track = self.get_track(track_id)
            response = requests.get(track.preview)
            with open(f"static/{filename}", "wb") as file:
                file.write(response.content)
        else:
            print("Track already downloaded")

    def download_cover(self, track_id: int, filename: str) -> None:
        """
        Download a cover from Deezer
        :param track_id: The id of the track to download the cover from
        :param filename: The name of the file to save the cover to
        :return: None
        """
        if not f"cover_{track_id}.jpg" in os.listdir("static"):
            track = self.get_track(track_id)
            response = requests.get(track.album.cover_xl)
            with open(f"static/{filename}", "wb") as file:
                file.write(response.content)