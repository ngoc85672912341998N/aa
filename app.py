from typing import Optional
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import GithubUserModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

limits = httpx.Limits(max_keepalive_connections=5, max_connections=10)
timeout = httpx.Timeout(timeout=5.0, read=15.0)
client = httpx.AsyncClient(limits=limits, timeout=timeout)





@app.get("/", response_class=HTMLResponse)
async def index(request: Request, username: str = None):
    if not username:
        return templates.TemplateResponse("index.html", context={"request": request})

    user = await get_github_profile(request, username)
    if not user:
        return templates.TemplateResponse("404.html", context={"request": request})

    return templates.TemplateResponse("index.html", context={"request": request, "user": user})



