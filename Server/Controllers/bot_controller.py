from typing import Optional
from openai.error import *
from fastapi import APIRouter, HTTPException, Depends
from Domain.bot import Bot
from sqlalchemy.orm import Session
from Database.database import get_db
from Service import bot_service

router = APIRouter(
    prefix="/bot",
    tags=["bot"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.post("/process", response_model=str)
async def process_handler(prompt: str, username: str, db: Session = Depends(get_db)):
    bot = Bot(username=username, session_id=bot_service.get_session_id_by_username(username, db))
    try:
        response = bot.process(prompt)
        return {"message": response}
    except APIError as e:
        error_message = f"OpenAI API returned an API Error: {e}"
        raise HTTPException(status_code=500, detail=error_message)
    except APIConnectionError as e:
        error_message = f"Failed to connect to OpenAI API: {e}"
        raise HTTPException(status_code=500, detail=error_message)
    except RateLimitError as e:
        error_message = f"OpenAI API request exceeded rate limit: {e}"
        raise HTTPException(status_code=429, detail=error_message)

@router.post("/generate_image", response_model=str)
async def generate_image_handler(prompt: str, username: str, db: Session = Depends(get_db)):
    bot = Bot(session_id=bot_service.get_session_id_by_username(username, db))
    try:
        image_url = bot.generate_image(prompt)
        return {"image_url": image_url}
    except APIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API returned an API Error: {e}")
    except APIConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Failed to connect to OpenAI API: {e}")
    except RateLimitError as e:
        raise HTTPException(status_code=429, detail=f"OpenAI API request exceeded rate limit: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating image: {e}")
