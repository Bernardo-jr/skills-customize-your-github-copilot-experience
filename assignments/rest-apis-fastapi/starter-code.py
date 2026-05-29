from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Simple Items API")

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

# In-memory "database"
items_db: List[Item] = [
    Item(id=1, name="Apple", description="Fresh red apple", price=0.5),
    Item(id=2, name="Banana", description="Ripe banana", price=0.3),
]

@app.get("/items", response_model=List[Item])
def list_items():
    return items_db

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    # Simple uniqueness check
    if any(existing.id == item.id for existing in items_db):
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items_db.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated: Item):
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            items_db[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Item not found")

# To run locally:
# python3 -m pip install fastapi uvicorn
# uvicorn starter-code:app --reload
