from fastapi import APIRouter

api_zz = APIRouter()

@api_zz.get("/get")
async def get_test():
    return {"method": "get method"}

@api_zz.post("/post")
async def post_test():
    return {"method": "post method"}
@api_zz.put("/put")
async def put_test():
    return {"method": "put method"}

@api_zz.delete("/delete")
async def delete_test():
    return {"method": "delete method"}