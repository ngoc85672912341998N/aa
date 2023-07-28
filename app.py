from typing import Optional
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
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