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

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)
SQLModel.metadata.create_all(engine)




# def create_data(ten,dv,stns,stnv,like):
#     hero_1 = bang_nhan_vien(ho_ten_nhan_su=ten, don_vi=dv,so_the_nhan_vien=stns, link_fb_nhan_vien=stnv,luot_thich=like)
#     session = Session(engine)
#     session.add(hero_1)
#     session.commit()
#     return session

# file = open("1.csv","r",encoding="utf-8-sig")
# k=file.readlines()
# for k in k:
#     print(k.replace("\n","").split(",")[0])
#     print(k.replace("\n","").split(",")[1])
#     print(k.replace("\n","").split(",")[2])
#     print(k.replace("\n","").split(",")[3])
#     print(k.replace("\n","").split(",")[4])
#     dt1 = k.replace("\n","").split(",")[0]
#     dt2= k.replace("\n","").split(",")[1]
#     dt3=k.replace("\n","").split(",")[2]
#     dt4=k.replace("\n","").split(",")[3]
#     dt5=k.replace("\n","").split(",")[4]
#     create_data(dt1,dt3,dt2,dt4,dt5)
# z=0
# for ten in ten:
#     Session1=create_data(ten,chi_nhanh[z],Ma_nhan_vien[z],link[z],Luot_thich[z])
#     z=z+1
#     Session1.commit()
# file = open("funtion.txt","w")
# for ten in ten:
#     string5="""hero_{} = bang_nhan_vien(ho_ten_nhan_su={}, don_vi={},so_the_nhan_vien={}, link_fb_nhan_vien={},luot_thich={})
#     session = Session(engine)
#     session.add(hero_{})""".format(i,ten[i],chi_nhanh[i],Ma_nhan_vien[i],Luot_thich[i])
#     file.write(string5+"\n")