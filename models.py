import time
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select


class bang_nhan_vien(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ho_ten_nhan_su: str
    don_vi: str
    so_the_nhan_vien: str
    link_fb_nhan_vien: str
    luot_thich: str

class update_data(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ngay_update: str
    tinh_trang: str