import json

import websockets

from enums.enum import WebSocketResource


async def teke_crypto(message):
    ...


async def crypto_websocket():
    async with websockets.connect(WebSocketResource.WS_CRYPTO) as websocket:
        print("Websockets connect")
        print(WebSocketResource.message_call_5s_normal)
        await websocket.send(json.dumps(WebSocketResource.message_call_5s_normal))
        while True:
            try:
                message = await websocket.recv()
                message = json.loads(message).get("d")
                if message:
                    await teke_crypto(message)
            except websockets.ConnectionClosed:
                print("Websockets connect close")
                break
