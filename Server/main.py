from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from Domain.account import *
from Database.database import *
from Controllers import account_controller, chat_controller, contacts_controller, past_chats_controller, messages_controller, privileges_controller, bot_controller
from Service.account_service import *

app = FastAPI()
app.include_router(account_controller.router)
app.include_router(chat_controller.router)
app.include_router(contacts_controller.router)
app.include_router(past_chats_controller.router)
app.include_router(messages_controller.router)
app.include_router(privileges_controller.router)
app.include_router(bot_controller.router)
# app.include_router(
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[],
#     responses={418: {"description": "I'm a teapot"}},
# )
origins = ["http://localhost:4200"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
async def shutdown():
    pass

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return {"message" : "backend"}