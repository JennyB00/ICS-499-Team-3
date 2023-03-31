from typing import Optional, List
from openai.error import *
from fastapi import APIRouter, HTTPException, Depends
from Domain.bot import Bot


router = APIRouter(
    prefix="/bot",
    tags=["bot"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

bot = Bot()


@router.post("/process", response_model=str)
async def process_handler(prompt: str, username: str):
    try:
        response = bot.process(prompt, username)
        return response
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
def generate_image_handler(prompt: str):
    try:
        image_url = bot.generate_image(prompt)
        return image_url
    except APIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API returned an API Error: {e}")
    except APIConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Failed to connect to OpenAI API: {e}")
    except RateLimitError as e:
        raise HTTPException(status_code=429, detail=f"OpenAI API request exceeded rate limit: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating image: {e}")
