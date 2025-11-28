from fastapi import FastAPI
from server.messaging.messaging_service import get_last_ten_messages, insert_message
from server.models.message import Message

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# GET /message
@app.get("/message")
async def get_messages():
	return get_last_ten_messages("test")


# POST /message
@app.post("/message")
async def post_message(req_body: dict):
      return insert_message(req_body=req_body)