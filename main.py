from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import PlainTextResponse

# class StudentCreateSchema(BaseModel):
#     first_name: str
#     last_name: str
# # class StudentUpdateSchema(BaseModel):


# app = FastAPI()

# items = []

# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=400)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.post("/items/")
# async def create_item(item: StudentCreateSchema):
#     items.append(item)
#     return item

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     if len(items) <= item_id:
#             raise HTTPException(status_code=404, detail="Item not found", headers={"X-Error":"God Damnit"})
#     return {"item_id": items[item_id]}


# # @app.post("/items/{item_id}")
# # async def create_item(item: StudentCreateSchema):
# #     return item

# @app.put("/items/{item_id}", response_model=StudentCreateSchema)
# async def update_item(item_id: str, item: StudentCreateSchema):
#     update_item_encoded = jsonable_encoder(item)
#     items[item_id] = update_item_encoded
#     return update_item_encoded

from fastapi import FastAPI

import students

app = FastAPI()

app.include_router(students.router, prefix="/students")
