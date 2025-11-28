from sqlalchemy import Column, String, Uuid, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Message(Base):
	__tablename__ = "messages"
	id = Column(Uuid, primary_key=True, index=True)
	message = Column(String, index=True)
	recipient_id = Column(Uuid, index=True)
	sender_id = Column(Uuid, index=True)
	timestamp = Column(Date, index=True)
