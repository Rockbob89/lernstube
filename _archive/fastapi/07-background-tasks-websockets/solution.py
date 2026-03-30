from fastapi import FastAPI, BackgroundTasks, WebSocket, WebSocketDisconnect
from pydantic import BaseModel

app = FastAPI()


class Notification(BaseModel):
    email: str
    message: str


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        pass

    def disconnect(self, websocket: WebSocket):
        pass

    async def broadcast(self, message: str):
        pass


manager = ConnectionManager()


def write_notification_log(email: str, message: str):
    pass


@app.post("/notifications", status_code=202)
def send_notification(notification: Notification, background_tasks: BackgroundTasks):
    pass


@app.websocket("/ws")
async def websocket_echo(websocket: WebSocket):
    pass


@app.websocket("/ws/chat/{username}")
async def websocket_chat(websocket: WebSocket, username: str):
    pass
