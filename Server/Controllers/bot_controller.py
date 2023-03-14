from fastapi import APIRouter
from Server.Domain.bot import *

router = APIRouter(
    prefix="/bot",
    tags=["bot"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/process", response_model=BotBase)
def process_handler(prompt: str):
    bot = Bot()
    return bot.process(prompt)


@router.post("/generate_image", response_model=BotBase)
def generate_image_handler(prompt: str):
    bot = Bot()
    return bot.generate_image(prompt)