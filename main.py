from fastapi import FastAPI
import json
import random
from datetime import datetime

app = FastAPI()


@app.get("/")
async def view():
    """
    Fetched the list
    """
    resp = get_records()
    return resp


def get_records():
    with open("core/store/store.json") as store_file:
        store = json.load(store_file)
    return store

@app.get("/create")
async def create():
    """
    Create the record
    """
    resp = create_records()
    return resp


def create_records():
    with open("core/store/store.json") as store_file:
        store = json.load(store_file)
        store.get("students").append({
            "id": random.randint(1, 101),
            "date_created": datetime.now().strftime("%b-%d-%Y at %H:%M")
        })
    with open("core/store/store.json", "w") as outfile:
        json.dump(store, outfile)
    return store
