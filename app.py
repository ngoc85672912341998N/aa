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
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("shutdown")
async def shutdown_event():
    print("shutting down...")
    await client.aclose()


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    statement4 = select(bang_nhan_vien)
    results4 = session.exec(statement4).all()
    so_luong= len(results4)
    k=0
    for results4 in results4:
        k=k+int(results4.luot_thich)
    statement = select(bang_nhan_vien)
    results = session.exec(statement).all()
    statement2 = select(update_data)
    results2 = session.exec(statement2).all()
    return templates.TemplateResponse("1.html", {"request": request, "results": results,"results2":results2,"so_luong":so_luong,"tong_luot_thich":k})


