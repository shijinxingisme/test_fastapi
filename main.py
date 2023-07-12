from typing import Union
import uvicorn  # 服务器

from fastapi import FastAPI, Header, Body, Form
from fastapi.responses import JSONResponse, HTMLResponse,FileResponse

# from fastapi import Header
# from fastapi import Body

app = FastAPI()


#  pip install fastapi[all]  全部包 包括文档
# uvicorn main:app --reload

# docs  文档地址一
# redoc   文档地址二

# 启动方法 1
# if __name__ == '__main__':
#     uvicorn.run(app)

# 启动方法2
# 命令  uvicorn 类名:app对象名      例如: uvicorn main:app
#   --reload   热部署

@app.get("/pic")
def user():
    """FileResponse定义响应"""
    pic="image/img.png"
    return FileResponse(pic,filename="testImg.png"
                        )

@app.get("/htmlresponse")
def user():
    """HTMLResponse定义响应"""
    html_msg="""
    <html>
    <body><p style="color:red">hello</p></body>
    </html>
    """
    return HTMLResponse(content=html_msg,
                        status_code=202,
                        headers={"token":"2asdagagsdsffsfsgsxcvbx"}
                        )

@app.get("/user")
def user():
    """JSONResponse定义响应"""
    return JSONResponse(content={"msg":"get user"},
                        status_code=202,
                        headers={"token":"2asdagagsdsffsfsgsxcvbx"}
                        )



@app.api_route("/mytest/{str}", methods=['GET', 'POST'])
def read_root(str: str, q: Union[str, None] = None):
    """测试GET/POST方法"""
    return {"GET": str, "q": q}


@app.get("/testform")
def read_root(username=Form(None), pwd=Form(None)):
    """从form表单中获取"""
    return {"data":{"username":username,"pws":pwd}}


@app.get("/testjson")
def read_root(a=Body(None)):
    """从JSON中获取"""
    return a


@app.api_route("/testheader", methods=['GET', 'POST'])
def read_root(token=Header(None)):
    """从请求头中获取"""
    return token


@app.get("/")
def read_root():
    """首页"""
    return {"Hello": "World"}


@app.get("/test")
def read_root():
    """测试页面"""
    return {"Hello": "Worldtest"}


@app.get("/projects")
def read_root():
    return ["a", "b", "c"]




@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
