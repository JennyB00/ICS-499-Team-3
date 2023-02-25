from fastapi import APIRouter
from Database.privilegesRepo import PrivilegesRepo
import Database.Database

app = APIRouter(
    prefix="/privileges",
    tags=["privileges"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@app.get("/")
def read_privileges():
    return PrivilegesRepo.get_all_privileges(cursor)