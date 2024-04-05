import time
from typing import Dict, Callable
from fastapi import WebSocket, WebSocketDisconnect
from .msg_stack import message_stack

DEL_DELT_SEC = 60 * 60 * 5

class Session:
    sid: str
    websocket: WebSocket | None
    last_active_ts: int = 0
    is_alive: bool = True

    def __init__(self, sid: str, ws: WebSocket | None):
        self.sid = sid
        self.websocket = ws
        self.last_active_ts = int(time.time())

    async def loop_recv(self, dispatch: Callable):
        # ... (rest of the method remains unchanged)

    async def send(self, data: Dict[str, object]) -> bool:
        # Implement the send method logic here
        pass  # Placeholder; replace with actual implementation

    async def send_error(self, message: str) -> bool:
        """Sends an error message to the client."""
        return await self.send({"error": True, "message": message})

    async def send_message(self, message: str) -> bool:
        """Sends a message to the client."""
        return await self.send({"message": message})
