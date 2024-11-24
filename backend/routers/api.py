import json
from deezer.resources import playlist
from fastapi import APIRouter, status, Request
from fastapi.responses import JSONResponse
import deezer as dz

from utils import spotipy_client as spc

router = APIRouter(
    prefix="/api",
    tags=["api"]
)

@router.get("/track/{track_id}", response_class=JSONResponse, status_code=status.HTTP_200_OK)
async def get_track(request: Request, track_id: int):
    with dz.Client() as client:
        track = client.get_track(track_id)
        return track.as_dict()


@router.get("/recommendations", response_class=JSONResponse, status_code=status.HTTP_200_OK)
async def get_recommendations(request: Request):
    spc_client = spc.SPClient("../.env")
    rec = []
    recommendations = spc_client.get_recommendations()
    if recommendations is None:
        return {"error": "No recommendations found"}
    for track in recommendations["tracks"]:
        rec.append({
            "name": track["name"],
            "id": track["id"],
        })
    return rec

@router.get("/song_deezer/{song_id}", response_class=JSONResponse, status_code=status.HTTP_200_OK)
async def get_song_name(request: Request, song_id: str):
    spc_client = spc.SPClient("../.env")
    name = spc_client.get_song_name(song_id)

    if name is None:
        return {"error": "Song not found"}

    with dz.Client() as client:
        tracks = client.search(name)
        return tracks[0].as_dict()


@router.get("/user_is_auth", response_class=JSONResponse, status_code=status.HTTP_200_OK)
async def user_is_auth(request: Request):
    spc_client = spc.SPClient("../.env")
    return {"is_auth": spc_client.sp.current_user() is not None}

@router.post("/playlist/add/{track_id}", response_class=JSONResponse, status_code=status.HTTP_200_OK)
async def add_to_playlist(request: Request, track_id: str):
    spc_client = spc.SPClient("../.env")
    user = spc_client.sp.current_user()

    if user is None:
        return {"error": "User not authenticated"}

    playlists = spc_client.sp.current_user_playlists()

    if not isinstance(playlists, dict):
        return {"error": "No playlists found"}

    playlists_names = [playlist["name"] for playlist in playlists["items"]]

    if "Sounder" not in playlists_names:
        spc_client.sp.user_playlist_create(user["id"], "Sounder", public=False)

    playlist_id = [playlist["id"] for playlist in playlists["items"] if playlist["name"] == "Sounder"][0]
    spc_client.sp.playlist_add_items(playlist_id, [track_id])

    return {
        "success": True,
        "message": f"Track {track_id} added to playlist",
        "playlist_id" : playlist_id
    }