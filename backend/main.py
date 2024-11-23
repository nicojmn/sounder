# Packages and built-in modules
from re import S
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

# Sounder modules
from routers import auth


app = FastAPI(
    debug=True,
    title="Sounder",
    license_info={
        "name": "AGPLv3",
        "url": "https://www.gnu.org/licenses/agpl-3.0.html"
    }
)

app.mount("/front", StaticFiles(directory="../frontend/build", html=True), name="frontend")

# import routers here
app.include_router(auth.router)

# root route
@app.get("/", response_class=FileResponse)
async def read_root(request: Request):
    return RedirectResponse(url="/front/", status_code=302)