'''
Source: https://youtu.be/-ykeT6kk4bk?si=aPYVkjRxLIYAURPz
'''

'''Dependencies'''
# pip install fastapi
# pip install uvicorn

from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

'''
Initialize FastAPI on LocalHost (http://127.0.0.1:8000)
Add /docs to see the Swagger UI
'''
# uvicorn FastAPI:app --reload

'''Create a test route'''
@app.get("/")
def home():
    return {'Data': 'Testing'}

'''Create a second route'''
@app.get("/about")
def about():
    return {'Data': 'About'}

'''Create an example record'''
inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": 'Regular'
    },
}

'''Add parameters'''
@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]

'''Add multiple parameters'''
@app.get("/get-by-name/{item_id}/{name}")
def get_item(item_id: int, name: str):
    return inventory[item_id]

'''Set a default value for a parameter'''
@app.get("/get-item-default/")
def get_item(item_id: int = Query(1, description="The ID of the item you'd like to view")):
    return inventory[item_id]

''' Add constraints on item_id'''
@app.get("/get-item-constraints/{item_id}")
def get_item(item_id: int = Path(..., description="The ID of the item you'd like to view", gt=0, lt=2)):
    return inventory[item_id]

'''Query Parameters
Example: facebook.com/home?redirect=/john@msg=fail
'''
@app.get("/get-by-name")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
    return {"Data": "Not found"}

'''Make query parameter optional'''
@app.get("/get-by-name-optional")
def get_item(name: str = None):
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
    return {"Data": "Not found"}

'''Recommended way for optional parameters'''
@app.get("/get-by-name-recommended")
def get_item(name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
    return {"Data": "Not found"}

'''Add multiple query parameters with a required parameter'''
@app.get("/get-by-name-multiple")
def get_item(test: int, name: Optional[str] = None):
    '''
    Note: Required fields must go before optional fields.
    You can bypass this by doing the following:
    def get_item(*, name: Optional[str] = None, test: int):
    '''
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
    return {"Data": "Not found"}

'''Use path parameters and query parameters'''
@app.get("/get-by-name-path-query/{item_id}")
def get_item(*, item_id: int, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
    return {"Data": "Not found"}

'''Create a class object for post method'''
class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

'''Create a new item'''
@app.post("/create-item-null")
def create_item(item: Item):
    return {}

@app.post("/create_item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists"}
    inventory[item_id] = item
    return inventory[item_id]

'''Clear cached data'''
inventory = {}

'''Create a new item'''
@app.put("/get-by-name")
def get_item(name: str = Query(None, description="Name of item", max_length=10, min_length=2)):
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
    return {"Data": "Not found"}

'''Create a class object for update method'''
class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

'''Update an item'''
@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item ID does not exist"}
    if item.name is not None:
        inventory[item_id].name = item.name
    if item.price is not None:
        inventory[item_id].price = item.price
    if item.brand is not None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]

'''Delete an item'''
@app.delete("/delete-item}")
def delete_item(item_id: int = Query(..., description="ID of item to delete", gt=0)):
    if item_id not in inventory:
        return {"Error": "Item ID does not exist"}
    del inventory[item_id]
    return {"Message": "Item deleted"}

'''Status Codes'''    
@app.get("/get-by-name-status")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail="Item name not found")