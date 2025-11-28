import uuid
import datetime
from server.models.message import Message
from server.messaging.messaging_repository import insert_item_to_db, get_all_items_from_db

def get_last_ten_messages(user_id: str):
	return get_all_items_from_db()


def insert_message(req_body: dict):
	message = Message(
		id = uuid.uuid4(),
		message=req_body.get("message"),
		recipient_id=uuid.UUID(req_body.get("recipient_id")),
		sender_id=uuid.UUID(req_body.get("sender_id")),
		timestamp=datetime.datetime.now()
	)
	return insert_item_to_db(message)
