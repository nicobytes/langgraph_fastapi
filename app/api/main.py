from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from pydantic import BaseModel
from app.agents.graph import LangGraphAgent


app = FastAPI()
agent = LangGraphAgent()

class Message(BaseModel):
    message: str


@app.post("/")
def read_root():
    return {"Hello": "World"}


@app.post("/chat/")
async def create_item(item: Message):
    return await agent.get_response(item.message)
