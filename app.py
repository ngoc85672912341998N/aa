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
import uvicorn

session=Session(bind=engine)

app = FastAPI()


templates = Jinja2Templates(directory="templates")



@app.get("/theo_doi_nhan_su/", response_class=HTMLResponse)
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


@app.get("/update_nhan_su_thich/", response_model=bang_nhan_vien)
async def read_item(nhan_su:str,so_luot_thich_cong):
    statement = select(bang_nhan_vien).where(bang_nhan_vien.link_fb_nhan_vien==nhan_su)
    result = session.exec(statement).first()
    result.luot_thich = int(result.luot_thich)+int(so_luot_thich_cong)
    session.commit()
    return result

@app.post("/thoi_gian_update/", response_model=update_data)
def read_item(ngay:str,tinh_trang:str):
    new_update = update_data(ngay_update=ngay, tinh_trang=tinh_trang)
    session.add(new_update)
    session.commit()
    return new_update

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)