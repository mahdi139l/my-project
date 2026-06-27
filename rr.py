import websocket
import json

def on_message(ws, message):
    data = json.loads(message)
    price = data['p']
    volume = data['q']
    print(f"Price: {price} | Volume: {volume}", flush=True)

def on_error(ws, error):
    print("ERROR:", error)

def on_open(ws):
    print("Connected to Binance ✅", flush=True)

socket = "wss://stream.binance.com:9443/ws/btcusdt@trade"

ws = websocket.WebSocketApp(
    socket,
    on_message=on_message,
    on_error=on_error,
    on_open=on_open
)

ws.run_forever()
