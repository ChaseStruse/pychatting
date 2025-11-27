import uuid
from dataclasses import dataclass

@dataclass
class Message:
	id: uuid.UUID
	message: str
	recipient_id: uuid.UUID
	sender_id: uuid.UUID