from fastapi import APIRouter
from pydantic import BaseModel
from app.database.db import get_connection
from datetime import datetime, timezone, timedelta

router = APIRouter()


class Message(BaseModel):
    sender: str
    receiver: str
    message: str



def iran_time():
    iran = timezone(timedelta(hours=3, minutes=30))
    return datetime.now(iran).strftime("%Y-%m-%d %H:%M:%S")



@router.post("/send")
def send_message(data: Message):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO messages (sender, receiver, message, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (
            data.sender,
            data.receiver,
            data.message,
            iran_time()
        )
    )

    conn.commit()
    conn.close()

    return {
        "message": "Message sent"
    }



@router.get("/messages")
def get_messages(user1: str, user2: str):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT sender, receiver, message, created_at
        FROM messages
        WHERE
        (sender=? AND receiver=?)
        OR
        (sender=? AND receiver=?)
        ORDER BY id
        """,
        (
            user1,
            user2,
            user2,
            user1
        )
    )

    messages = cursor.fetchall()

    conn.close()


    return [
        {
            "sender": m[0],
            "receiver": m[1],
            "message": m[2],
            "time": m[3]
        }
        for m in messages
    ]