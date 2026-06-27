import websocket
import json
import time
from collections import deque

SYMBOL = input("Enter symbol (e.g. btcusdt, ethusdt): ").lower()

SOCKET = f"wss://stream.binance.com:9443/ws/{SYMBOL}@trade"

buy_volume = 0.0
sell_volume = 0.0

history = deque(maxlen=20)  # برای مقایسه حجم قبلی

def on_message(ws, message):
    global buy_volume, sell_volume

    data = json.loads(message)

    qty = float(data['q'])
    is_buyer_maker = data['m']

    if is_buyer_maker:
        sell_volume += qty
    else:
        buy_volume += qty

def on_open(ws):
    print(f"\nConnected to {SYMBOL.upper()} Trade Flow...")
    print("Watching for BURSTS...\n")

def burst_monitor():
    global buy_volume, sell_volume

    while True:
        time.sleep(1)

        total_volume = buy_volume + sell_volume
        delta = buy_volume - sell_volume

        avg_volume = sum(history) / len(history) if history else 0
        history.append(total_volume)

        burst = avg_volume > 0 and total_volume > avg_volume * 2

        direction = "BUY 🟢" if delta > 0 else "SELL 🔴"

        if burst:
            print("🚨 BURST DETECTED 🚨")

        print(
            f"1s | Buy: {buy_volume:.2f} | Sell: {sell_volume:.2f} | "
            f"Delta: {delta:.2f} | Vol: {total_volume:.2f} | {direction}"
        )

        buy_volume = 0
        sell_volume = 0

ws = websocket.WebSocketApp(
    SOCKET,
    on_message=on_message,
    on_open=on_open
)

import threading
threading.Thread(target=burst_monitor, daemon=True).start()

ws.run_forever()
