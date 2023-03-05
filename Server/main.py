from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from Domain.account import *
from Controllers import account_controller, chat_controller, contacts_controller, past_chats_controller, messages_controller, privileges_controller
from Database.database import *

app = FastAPI()
app.include_router(account_controller.router)
app.include_router(chat_controller.router)
app.include_router(contacts_controller.router)
app.include_router(past_chats_controller.router)
app.include_router(messages_controller.router)
app.include_router(privileges_controller.router)
# app.include_router(
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[],
#     responses={418: {"description": "I'm a teapot"}},
# )
@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
async def shutdown():
    pass

# html=True sets it to not need /index.html and automatically translate
app.mount("/", StaticFiles(directory="Resources/Static",html = True), name="static")
templates = Jinja2Templates(directory="Resources/Templates")

# @app.get("/", response_class=HTMLResponse)
# async def root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

