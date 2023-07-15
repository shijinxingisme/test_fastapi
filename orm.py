from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from tortoise.contrib.fastapi import register_tortoise

from test_crm.test_sqlmodel import create_user,select_user,update_user,del_user,User

# https://www.bilibili.com/video/BV1oM411k7R4?p=12&spm_id_from=pageDriver&vd_source=d45e7fa6827868e5c143d3c05fd5e52e
app = FastAPI()
template = Jinja2Templates("pages")
# 数据库绑定
register_tortoise(app,
                  db_url="mysql://root:123456@localhost:3306/fastapi",
                  modules={"models":[]},
                  add_exception_handlers=True,
                  generate_schemas=True
                  )


# uvicorn orm:app --reload


@app.get("/testtem")
def testTemplate(req: Request):
    """html页面响应"""
    return template.TemplateResponse("index.html", context={"request": req})


@app.get("/")
def test(req: Request):
    """html页面响应1"""
    user = User(id=3, name="test1", email="test@bac.com")
    create_user(user)
    user = select_user(3)
    print(user)

    return template.TemplateResponse("index.html", context={"request": req, "name": user})

studys = ["VUE", "java", "php"]
@app.get("/study")
def study(req: Request):
    """html页面响应2"""
    return template.TemplateResponse("study.html", context={"request": req, "studys": studys})


@app.post("/add")
def study(study=Form(None)):
    """添加学习数据"""
    studys.insert(0,study)
    # studys.append(study)
    # post 转get 302
    return RedirectResponse("/study",status_code=302)
