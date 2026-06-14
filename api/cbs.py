from fastapi import APIRouter

api_cbs = APIRouter()

@api_cbs.get("/get")
async def get_test():
    return {"method": "get method"}

@api_cbs.post("/post")
async def post_test():
    return {"method": "post method"}
@api_cbs.put("/put")
async def put_test():
    return {"method": "put method"}

@api_cbs.delete("/delete")
async def delete_test():
    return {"method": "delete method"}