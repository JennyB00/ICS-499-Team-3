from typing import Optional
from fastapi import APIRouter
from Server.Domain.bot import Bot

router = APIRouter(
    prefix="/bot",
    tags=["bot"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

bot = Bot()


@router.post("/process")
def process_handler(prompt: str, session_id: Optional[str] = None):
    if session_id:
        bot.session_id = session_id
    return bot.process(prompt)


@router.post("/generate_image")
def generate_image_handler(prompt: str, session_id: Optional[str] = None):
    if session_id:
        bot.session_id = session_id
    return bot.generate_image(prompt)