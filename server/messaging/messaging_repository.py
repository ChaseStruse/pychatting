import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from server.models.message import Base, Message

load_dotenv()

def create_tables(engine):
    Base.metadata.create_all(bind=engine)

def get_engine():
    engine = create_engine(os.getenv("DB_URL") or "")
    return engine

def get_all_items_from_db():
    SessionLocal = sessionmaker(bind=get_engine())
    with SessionLocal() as session:
        items = session.query(Message).all()
        return items
    
def insert_item_to_db(item):
    SessionLocal = sessionmaker(bind=get_engine())
    with SessionLocal() as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item
    
create_tables(get_engine())