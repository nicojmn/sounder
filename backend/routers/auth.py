from fastapi import APIRouter, status, Request
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.get("/register", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def register(request: Request):
    pass # TODO

@router.get("/login", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def login(request: Request):
    pass # TODO

@router.post("/register", response_class=HTMLResponse, status_code=status.HTTP_201_CREATED)
async def register_post(request: Request):
    pass # TODO

@router.post("/login", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def login_post(request: Request):
    pass # TODO