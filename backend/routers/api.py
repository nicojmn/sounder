import json
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