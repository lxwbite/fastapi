# 导入FastAPI静态文件挂载模块，用于托管图片、css、js等静态资源
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# 导入FastAPI核心实例、Request请求对象（用于接收请求参数）
from fastapi import FastAPI, Request

# 导入uvicorn ASGI异步web服务器，用来运行FastAPI项目
import uvicorn

# 从api子包中导入拆分后的各个路由蓝图对象，实现接口模块化拆分
from api.book import api_book
from api.cbs import api_cbs
from api.zz import api_zz

# 实例化FastAPI应用程序核心对象
app = FastAPI()

# 挂载静态资源目录
# path：浏览器访问URL前缀；directory：本地存放静态文件的文件夹；name：内部标识名
# 访问示例：http://127.0.0.1:8000/upimg/img.png 即可直接读取upimg文件夹下的img.png图片
app.mount("/upimg", StaticFiles(directory="upimg"), name="upimg")

templates = Jinja2Templates(directory="templates")

# 批量注册拆分后的子路由，统一添加接口前缀和接口分类标签（用于自动接口文档分组）
# prefix：给当前分组所有接口统一拼接URL前缀；tags：接口文档里的分组名称
app.include_router(api_book, prefix="/book", tags=["book interface"])
app.include_router(api_cbs, prefix="/cbs", tags=["cbs interface"])
app.include_router(api_zz, prefix="/zz", tags=["zz interface"])


# 根路径访问接口，项目首页测试接口
@app.get("/")
async def root():
    return {"message": "Hello World"}


# GET请求测试接口，演示基础GET方式请求
@app.get("/get")
async def get_test():
    return {"method": "get method"}


# POST请求测试接口，演示基础POST方式请求
@app.post("/post")
async def post_test():
    return {"method": "post method"}


# PUT请求测试接口，常用于更新资源操作
@app.put("/put")
async def put_test():
    return {"method": "put method"}


# DELETE请求测试接口，常用于删除资源操作
@app.delete("/delete")
async def delete_test():
    return {"method": "delete method"}


# GET接口：获取URL拼接的Query查询参数
# Request对象接收完整请求对象，通过query_params提取地址栏?后的参数
@app.get("/get_test")
async def get_test(request: Request):
    get_test = request.query_params
    print(get_test)  # 在服务端控制台打印GET携带的查询参数
    return {"method": "get_test"}


# POST接口：接收JSON格式请求体数据
# await request.json() 异步读取请求体中的json数据，必须加await否则拿不到真实数据
@app.post("/post_test")
async def post_test(request: Request):
    post_test = await request.json()
    print(post_test)  # 控制台打印前端传递的json请求体内容
    return {"method": "post_test"}

@app.get("/jinjia2templates")
async def jinjia2templates(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "books": ["平凡的世界","活着","兄弟","围城"]
        }
    )


