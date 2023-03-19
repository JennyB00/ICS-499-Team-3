from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
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
@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
async def shutdown():
    pass

# html=True sets it to not need /index.html and automatically translate
app.mount("/static", StaticFiles(directory="Resources/Static",html = True), name="static")
templates = Jinja2Templates(directory="Resources/Templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

@app.get("/home/{username}", response_class=HTMLResponse)
def read_account_page(username: str, request: Request, db: Session = Depends(get_db)):
    account = get_account_by_username(username, db)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return templates.TemplateResponse("account.html", {"request": request, "account": account})

