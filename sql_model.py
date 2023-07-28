from sqlmodel import SQLModel,create_engine
import os

       
BASE_DIR=os.path.dirname(os.path.realpath(__file__))

conn_str='sqlite:///'+os.path.join(BASE_DIR,'database.db')
print(conn_str)

engine=create_engine(conn_str,echo=True, connect_args={"check_same_thread": False})