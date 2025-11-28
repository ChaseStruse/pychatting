import os
import uuid
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from server.models.message import Base, Message

load_dotenv()

def to_dict(message: Message):
    # Should be class function, not sure why it wasnt working...
	print(message)
	return {
		"id": str(message.id),
		"sender_id": str(message.sender_id),
		"recipient_id": str(message.recipient_id),
		"message": message.message,
		"timestamp": message.timestamp.isoformat()
	}

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
    
def get_all_messages_from_sender(sender_id: uuid.UUID, recipient_id: uuid.UUID):
    SessionLocal = sessionmaker(bind=get_engine())
    with SessionLocal() as session:
        statement = select(Message).where(
            (Message.recipient_id == recipient_id) & (Message.sender_id == sender_id)
        )
        result = session.execute(statement=statement).scalars().all()
        print(type(result[0]))
        messages = [to_dict(msg) for msg in result]
    return messages
    
def insert_item_to_db(item):
    SessionLocal = sessionmaker(bind=get_engine())
    with SessionLocal() as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item
    
create_tables(get_engine())