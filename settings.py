# settings.py
TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": "127.0.0.1",
                "port": 3306,
                "user": "root",
                "password": "123456789",
                "database": "fastapi_db",
            },
            "minsize": 1,
            "maxsize": 5,
            "echo": True,  # 打印执行的SQL语句，开发调试用
        }
    },
    # 注册所有存放模型的文件/模块
    "apps": {
        "models": {
            "models": ['models',"aerich.models"],
            "default_connection": "default",
        }
    },
    'use_tz':False,
    'timezone':'Asia/Shanghai'
}