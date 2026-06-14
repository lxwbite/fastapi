from fastapi import FastAPI

# web服务器
import uvicorn

from api.book import api_book
from api.cbs import api_cbs
from api.zz import api_zz

app = FastAPI()

app.include_router(api_book, prefix="/book", tags=["book interface"])
app.include_router(api_cbs, prefix="/cbs", tags=["cbs interface"])
app.include_router(api_zz, prefix="/zz", tags=["zz interface"])

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/get")
async def get_test():
    return {"method": "get method"}

@app.post("/post")
async def post_test():
    return {"method": "post method"}
@app.put("/put")
async def put_test():
    return {"method": "put method"}

@app.delete("/delete")
async def delete_test():
    return {"method": "delete method"}

