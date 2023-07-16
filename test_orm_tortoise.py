from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from tortoise.contrib.fastapi import register_tortoise

from dao.models import Study
from test_orm.test_orm_sqlmodel import create_user, select_user, update_user, del_user, User

# https://www.bilibili.com/video/BV1oM411k7R4?p=12&spm_id_from=pageDriver&vd_source=d45e7fa6827868e5c143d3c05fd5e52e
app = FastAPI()
template = Jinja2Templates("pages")
# 数据库绑定
register_tortoise(app,
                  db_url="mysql://root:root@localhost:3306/fast_api",
                  modules={"models": ['dao.models']},
                  add_exception_handlers=True,
                  generate_schemas=True
                  )


# uvicorn test_orm.test_orm_tortoise:app --reload


@app.get("/testtem")
def testTemplate(req: Request):
    """html页面响应"""
    return template.TemplateResponse("index.html", context={"request": req})


@app.get("/")
def test(req: Request):
    """html页面响应1"""
    user = User(id=3, name="test1", email="test@bac.com")
    try:
        create_user(user)
    except Exception as e:
        print("error ::::", e)
    user = select_user(3)
    print("user:::::::", user)

    return template.TemplateResponse("index.html", context={"request": req, "name": user})


# 全局变量
# studys = ["VUE", "java", "php"]


@app.get("/study")
async def study(req: Request):
    """html页面响应2"""
    # 设置为同步  async await
    studys = await Study.all()
    print("studys:", studys)
    return template.TemplateResponse("study.html", context={"request": req, "studys": studys})

""" todo """
@app.exception_handler(Exception)
async def error_handler(request: Request, exc: Exception):
    return template.TemplateResponse("error.html", {"request": request}, status_code=500)

""" None  不能为空  ...  必须要传递  """

@app.post("/add")
async def study(content=Form(None)):
    if not content:
        raise Exception("内容不能为空")
    """添加学习数据"""
    # studys.insert(0, study)
    # studys.append(study)

    """从数据库导入"""
    await Study(content=content).save()
    # post 转get 302
    return RedirectResponse("/study", status_code=302)

@app.post("/search")
async def study(req: Request, keyword=Form(None)):
    """查询学习数据"""
    # studys.insert(0, study)
    # studys.append(study)

    """从数据库导入"""
    # content__icontains  包含
    res = await Study.filter(content__icontains=keyword).all()

    # post 转get 302
    return template.TemplateResponse("/search_res.html", context={"request": req, "res": res})
