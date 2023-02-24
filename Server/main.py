from fastapi import Depends, FastAPI
from Controllers import accountController, chatController
from Database.Database import Base, engine


app = FastAPI()
app.include_router(accountController.router)
app.include_router(chatController.router)
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