"""The API"""
from fastapi import FastAPI, HTTPException


app = FastAPI()

fake_db = {"foo": "foobar", "bar": "barfoo"}


@app.get("/{key}")
async def read_db(key: str):
    """Demo endpoint"""
    if key in fake_db.keys():
        return fake_db[key]
    raise HTTPException(status_code=404, detail="Item not found")


# uvicorn 07_fastapi:app --reload
