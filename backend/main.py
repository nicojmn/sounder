# Packages and built-in modules
from re import S
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

# Sounder modules
from routers import auth, api


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
app.include_router(api.router)

# root route
@app.get("/", response_class=FileResponse)
async def read_root(request: Request):
    return RedirectResponse(url="/front/", status_code=302)

@app.get("/debug")
async def debug(request: Request, search: str | None):
    import deezer_client
    with deezer_client.Client() as client:
        if not search:    
            client.download_track(3135556, f"track-{3135556}.mp3")
            client.download_cover(3135556, f"cover-{3135556}.jpg")
        else:
            html = "<ul>"
            tracks = client.search(search)
            for track in tracks:
                html += f"""<li>{track.title} - {track.artist.name} --- {track.id} </li>"""
            html += "</ul>"
            return HTMLResponse(content=html)
                
        


