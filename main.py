from fastapi import FastAPI, Request, Form 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# kết nối css
app.mount("/static/css", StaticFiles(directory="static/css"), name="static")

# kết nối img
app.mount("/static/img", StaticFiles(directory="static/img"), name="static")

# kết nối html
templates = Jinja2Templates(directory="template")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("Login.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("Register.html", {"request": request})

@app.post("/register")
async def register_user(account: str = Form(...), password: str =Form(...)):
    return {"message": account}