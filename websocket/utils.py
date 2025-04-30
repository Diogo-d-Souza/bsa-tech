import asyncio
import json
from datetime import datetime

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

async def send_time(self):
  try:
      while True:
          now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
          await self.send(text_data=json.dumps({'message': now}))
          await asyncio.sleep(1)
  except asyncio.CancelledError:
      pass