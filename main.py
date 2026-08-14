from fastapi import FastAPI
from routes import base
app=FastAPI()
#main.py should include base router
app.include_router(base.base_router)
