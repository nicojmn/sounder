from fastapi import APIRouter, status, Request
from fastapi.responses import JSONResponse
import deezer as dz

router = APIRouter(
    prefix="/api",
    tags=["api"]
)

@router.get("/track/{track_id}", response_class=JSONResponse, status_code=status.HTTP_200_OK)
async def get_track(request: Request, track_id: int):
    with dz.Client() as client:
        track = client.get_track(track_id)
        return track.as_dict()