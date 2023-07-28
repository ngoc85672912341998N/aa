from fastapi import FastAPI
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import time
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select
from models import bang_nhan_vien,update_data
from sqlmodel import Session,select
from sql_model import engine
from sqlmodel import Field, Session, SQLModel, create_engine, select
import os
from fastapi import BackgroundTasks, FastAPI

session=Session(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")
app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)