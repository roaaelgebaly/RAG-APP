from fastapi import FastAPI,APIRouter

base_router=APIRouter()

@base_router.get("/")
def get_root():
    return {"msg": "Hello World"}