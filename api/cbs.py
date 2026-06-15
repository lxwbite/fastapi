from fastapi import APIRouter
from models import Publish

api_cbs = APIRouter()

@api_cbs.get("/")
async def getAllPublish():
    # 这是 list 对象
    publish_obj = await Publish.all()
    print(publish_obj)
    # 这是 queryset 对象
    # publish_obj = Publish.all()

    # filter
    # users = await User.filter(name=name).all()

    # get
    # user = await User.get(id=user_id)

    # order_by
    # users = await User.all().order_by('name')

    # limit
    # users = await User.all().limit(limit)

    # print(publish_obj)
    # return {'code': 200, 'data': publish_obj}
    return {"message": "Hello cbs"}

@api_cbs.post("/post")
async def post_test():
    return {"method": "post method"}
@api_cbs.put("/put")
async def put_test():
    return {"method": "put method"}

@api_cbs.delete("/delete")
async def delete_test():
    return {"method": "delete method"}