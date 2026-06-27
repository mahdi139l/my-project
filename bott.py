import requests
from telegram.ext import Updater, MessageHandler, filters

TOKEN = "8353719478:AAH7nAsCwoV0xACumH4MGRQh_jHh8C1vzUg"


def binance_data(symbol):
    url = "https://api.binance.com/api/v3/ticker/24hr"
    r = requests.get(url, params={"symbol": symbol})
    data = r.json()

    if "code" in data:
        return None

    return float(data["lastPrice"]), float(data["quoteVolume"])


def mexc_data(symbol):
    url = "https://api.mexc.com/api/v3/ticker/24hr"
    r = requests.get(url, params={"symbol": symbol})
    data = r.json()

    if "code" in data:
        return None

    return float(data["lastPrice"]), float(data["quoteVolume"])


def handle_message(update, context):
    symbol = update.message.text.upper().strip()

    b = binance_data(symbol)
    m = mexc_data(symbol)

    msg = f"📊 {symbol}\n\n"

    if b:
        msg += (
            "🟡 Binance\n"
            f"Price  : {b[0]:,.4f} $\n"
            f"Volume : {b[1]:,.0f} $\n\n"
        )
    else:
        msg += "🟡 Binance\nSymbol not found ❌\n\n"

    if m:
        msg += (
            "🔵 MEXC\n"
            f"Price  : {m[0]:,.4f} $\n"
            f"Volume : {m[1]:,.0f} $\n"
        )
    else:
        msg += "🔵 MEXC\nSymbol not found ❌"

    update.message.reply_text(msg)


updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(filters.text & ~filters.command, handle_message))

updater.start_polling()
updater.idle()