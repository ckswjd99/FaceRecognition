import asyncio
import websockets
 
async def connect():
  async with websockets.connect("ws://osam-api.herokuapp.com/api/iot") as websocket:

    for i in range(1,10,1):
      await websocket.send("Web Socket Test...")
      data = await websocket.recv()
      print("Received: ", data)

asyncio.get_event_loop().run_until_complete(connect())