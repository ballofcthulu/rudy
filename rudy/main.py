import asyncio
import json
import random

from nio import AsyncClient, RoomMessageText, MatrixRoom

from rudy.config import Config
from rudy.callbacks import Callbacks

CONFIG_FILE = "config.json"

async def main() -> None:
  config = Config(CONFIG_FILE)
  client = AsyncClient(config.homeserver)
  client.user_id      = config.user_id
  client.device_id    = config.device_id
  client.access_token = config.access_token
  client.room_id      = config.room_id
  Callbacks(client)

  await client.sync_forever(timeout=30000)
