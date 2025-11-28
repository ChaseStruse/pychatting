import uuid
import datetime
from dataclasses import dataclass

@dataclass
class Message:
	id: uuid.UUID
	message: str
	recipient_id: uuid.UUID
	sender_id: uuid.UUID
	timestamp: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")