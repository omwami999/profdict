from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from models.models import Item

app = FastAPI()

# Pydantic model
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

# In-memory "database"
items_db: List[Item] = []

# Create
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    if any(existing.id == item.id for existing in items_db):
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items_db.append(item)
    return item

# Read All
@app.get("/items/", response_model=List[Item])
def get_items():
    return items_db

# Read One
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

