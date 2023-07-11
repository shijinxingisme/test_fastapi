from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app = FastAPI()
template = Jinja2Templates("pages")


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
