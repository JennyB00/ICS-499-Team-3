from typing import Optional

import openai
from fastapi import APIRouter, HTTPException
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
    try:
        response = bot.process(prompt)
        return {"success": True, "message": response}
    except openai.error.APIError as e:
        error_message = f"OpenAI API returned an API Error: {e}"
        raise HTTPException(status_code=500, detail=error_message)
    except openai.error.APIConnectionError as e:
        error_message = f"Failed to connect to OpenAI API: {e}"
        raise HTTPException(status_code=500, detail=error_message)
    except openai.error.RateLimitError as e:
        error_message = f"OpenAI API request exceeded rate limit: {e}"
        raise HTTPException(status_code=429, detail=error_message)


@router.post("/generate_image")
def generate_image_handler(prompt: str, session_id: Optional[str] = None):
    if session_id:
        bot.session_id = session_id
    try:
        image_url = bot.generate_image(prompt)
        return {"image_url": image_url}
    except openai.error.APIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API returned an API Error: {e}")
    except openai.error.APIConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Failed to connect to OpenAI API: {e}")
    except openai.error.RateLimitError as e:
        raise HTTPException(status_code=429, detail=f"OpenAI API request exceeded rate limit: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating image: {e}")
