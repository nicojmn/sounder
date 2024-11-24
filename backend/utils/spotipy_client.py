import spotipy
from dotenv import load_dotenv


class SPClient:
    def __init__(self, dotenv_path: str) -> None:
        """
        Initializes the Spotify client
        :param dotenv_path: relarive path to the .env file
        """
        load_dotenv(dotenv_path)

        scope = "playlist-modify-public playlist-modify-private playlist-read-private playlist-read-collaborative user-library-read user-library-modify"


        # FIXME: This is a temporary solution. The client_id and secret should be stored in the .env file
        # TODO : Add the client_id and secret to the .env file
        # DANGER: Do not commit the .env file to the repository
        # VERY VERY DANGEROUS: Do not commit the .env file to the repository
        client_id = "77b69edab01e42dda135604004b54142"
        secret = "5cb78a9a516b41e89668bfe8bc861b9d"
        redirect = "http://localhost:9090/callback"

        self.sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(scope=scope, client_id=client_id, client_secret=secret, redirect_uri=redirect))


    def get_recommendations(self):
        seed_genres = ["pop", "rock"]
        seed_artists = []
        seed_tracks = []
        saved_tracks = self.sp.current_user_saved_tracks(limit=5)

        if not isinstance(saved_tracks, dict):
            return

        for track in saved_tracks["items"]:
            seed_tracks.append(track["track"]["id"])
            seed_artists.append(track["track"]["artists"][0]["id"])

        recommendations = self.sp.recommendations(
            seed_genres=seed_genres,
            limit=3,
            country="BE"
            )
        return recommendations

    def get_song_name(self, song_id: str):
        track = self.sp.track(song_id)
        if not isinstance(track, dict):
            return
        
        return track["name"]
        

