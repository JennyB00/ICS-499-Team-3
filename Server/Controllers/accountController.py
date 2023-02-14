from fastapi import APIRouter

app = APIRouter(
    prefix="/accounts",
    tags=["accounts"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/{username}")
def read_item(username: str):
    return 

#get all

#get by id

#etc...