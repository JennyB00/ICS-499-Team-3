from fastapi import Depends, FastAPI
from Controllers import account_controller, chat_controller
from Database.database import Base, engine


app = FastAPI()
app.include_router(account_controller.router)
app.include_router(chat_controller.router)
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


@app.get("/")
async def root():
    return {"message": "Hello World!"}