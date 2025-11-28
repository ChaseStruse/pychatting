import uuid
import os
from server.models.message import Message
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

def get_last_ten_messages(user_id: str):
	test_uuid_sender = uuid.uuid4()
	test_uuid_reciever = uuid.uuid4()

	return {
		"messages": [
			Message(id=uuid.uuid4(), message="Test 1", recipient_id=test_uuid_reciever, sender_id=test_uuid_sender),
			Message(id=uuid.uuid4(), message="Test 2", recipient_id=test_uuid_reciever, sender_id=test_uuid_sender),
			Message(id=uuid.uuid4(), message="Test 3", recipient_id=test_uuid_reciever, sender_id=test_uuid_sender),
			Message(id=uuid.uuid4(), message="Test 4", recipient_id=test_uuid_reciever, sender_id=test_uuid_sender),
		]
	}


def insert_message(req_body: Message):
	return req_body
