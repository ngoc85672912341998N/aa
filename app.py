from typing import Optional
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import bang_nhan_vien,update_data
from sqlmodel import Session,select
from sql_model import engine
from sqlmodel import Field, Session, SQLModel, create_engine, select
session=Session(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="templates")

limits = httpx.Limits(max_keepalive_connections=30, max_connections=30)
timeout = httpx.Timeout(timeout=30.0, read=30.0)
client = httpx.AsyncClient(limits=limits, timeout=timeout)


@app.on_event("shutdown")
async def shutdown_event():
    print("shutting down...")
    await client.aclose()


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):

    return templates.TemplateResponse("1.html", context={"request": request})

@app.post("/thoi_gian_update/", response_model=update_data)
def read_item(ngay:str,tinh_trang:str):
    new_update = update_data(ngay_update=ngay, tinh_trang=tinh_trang)
    session.add(new_update)
    session.commit()
    return new_update