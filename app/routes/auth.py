from fastapi import APIRouter, Form
from fastapi.responses import RedirectResponse
from app.database.db import get_connection
import sqlite3

router = APIRouter()


@router.get("/test")
def test():
    return {"message": "NovaChat OK"}


@router.post("/register")
def register(username: str = Form(...), password: str = Form(...)):

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()

    except sqlite3.IntegrityError:
        conn.close()
        return {"message": "Username already exists"}

    conn.close()

    return RedirectResponse("/login", status_code=303)



@router.post("/login")
def login(username: str = Form(...), password: str = Form(...)):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        return RedirectResponse(
            f"/chat?user={username}",
            status_code=303
        )

    return {"message": "Wrong username or password"}



@router.get("/users")
def get_users():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT username FROM users"
    )

    users = cursor.fetchall()

    conn.close()

    return [
        {
            "username": u[0]
        }
        for u in users
    ]