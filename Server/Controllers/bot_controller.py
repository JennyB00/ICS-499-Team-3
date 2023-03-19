from fastapi import APIRouter
from Domain.bot import *

router = APIRouter(
    prefix="/bot",
    tags=["bot"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/{username}/process", response_model=str)
async def process_handler(prompt: str):
    bot = Bot()
    return bot.process(prompt)

@router.get("/{username}/generate_image", response_model=str)
async def generate_image_handler(prompt: str):
    bot = Bot()
    return bot.generate_image(prompt)