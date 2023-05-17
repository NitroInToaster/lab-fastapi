from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

class StudentCreateSchema(BaseModel):
    # name: str
    # description: str | None = None
    # price: float
    # tax: float | None = None
    first_name: str
    last_name: str

# class StudentUpdateSchema(BaseModel):


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items/")
async def create_item(item: StudentCreateSchema):
    return item

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}


# @app.post("/items/{item_id}")
# async def create_item(item: StudentCreateSchema):
#     return item

@app.put("/items/{item_id}", response_model=StudentCreateSchema)
async def update_item(item_id: str, item: StudentCreateSchema):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded