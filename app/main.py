from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.routes.chat import router as chat_router
from app.routes.auth import router as auth_router

templates = Jinja2Templates(directory="/storage/emulated/0/NovaChat/templates")

app = FastAPI(title="NovaChat")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>NovaChat</title>
        <style>
            body{
                background:#111827;
                color:white;
                font-family:Arial;
                text-align:center;
                padding-top:80px;
            }

            h1{
                color:#4F8CFF;
                font-size:40px;
            }

            button{
                width:220px;
                padding:15px;
                margin:10px;
                border:none;
                border-radius:12px;
                font-size:18px;
                cursor:pointer;
            }

            .login{
                background:#4F8CFF;
                color:white;
            }

            .register{
                background:#22C55E;
                color:white;
            }
        </style>
    </head>

    <body>

        <h1>NovaChat</h1>

        <h3>Welcome to NovaChat</h3>

        <a href="/login"><button class="login">Login</button></a>

        <br>

        <a href="/register"><button class="register">Register</button></a>

    </body>
    </html>
    """


@app.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse(
        "register.html",
        {"request": request}
    )


@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )


@app.get("/chat")
def chat_page(request: Request, user: str):
    return templates.TemplateResponse(
        "chat.html",
        {
            "request": request,
            "user": user
        }
    )


app.include_router(auth_router)
app.include_router(chat_router)