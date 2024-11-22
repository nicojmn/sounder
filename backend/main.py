# Packages and built-in modules
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Sounder modules
from routers import auth



app = FastAPI()

# import routers here
app.include_router(auth.router)

# root route
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return HTMLResponse(content="Waiting for front team", status_code=200) # TODO : create file in frontend
