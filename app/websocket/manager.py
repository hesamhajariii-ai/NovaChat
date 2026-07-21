from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections = {}

    async def connect(self, username: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[username] = websocket

    def disconnect(self, username: str):
        if username in self.active_connections:
            del self.active_connections[username]

    async def send_to_user(self, username: str, message: str):
        if username in self.active_connections:
            await self.active_connections[username].send_text(message)

    def is_online(self, username: str):
        return username in self.active_connections

    def get_online_users(self):
        return list(self.active_connections.keys())


manager = ConnectionManager()