from fastapi import FastAPI
app=FastAPI()

@app.get("/myapp")
def Welcome():
    return {"msg": "Hello World"}