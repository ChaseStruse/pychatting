from fastapi import FastAPI
from server.messaging.messaging_service import get_last_ten_messages

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# GET /message
@app.get("/message")
async def get_messages():
	return get_last_ten_messages("test")