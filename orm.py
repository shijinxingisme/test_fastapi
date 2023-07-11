from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from tortoise.contrib.fastapi import register_tortoise


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


# uvicorn template:app --reload


@app.get("/testtem")
def testTemplate(req: Request):
    """html页面响应"""
    return template.TemplateResponse("index.html", context={"request": req})


@app.get("/")
def test(username, req: Request):
    """html页面响应1"""
    return template.TemplateResponse("index.html", context={"request": req, "name": username})

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
