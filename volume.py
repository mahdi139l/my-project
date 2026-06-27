# import requests

# binance_url = "https://api.binance.com/api/v3/ticker/24hr"
# mexc_url = "https://api.mexc.com/api/v3/ticker/24hr"


import requests

def get_binance_volume(symbol):
    url = "https://api.binance.com/api/v3/ticker/24hr"
    r = requests.get(url, params={"symbol": symbol})
    data = r.json()

    if "code" in data:
        return None

    return float(data["quoteVolume"])


def get_mexc_volume(symbol):
    url = "https://api.mexc.com/api/v3/ticker/24hr"
    r = requests.get(url, params={"symbol": symbol})
    data = r.json()

    if "code" in data:
        return None

    return float(data["quoteVolume"])



symbol = input("name currency : ").upper()

binance_vol = get_binance_volume(symbol)
mexc_vol = get_mexc_volume(symbol)

print("\nRESULT")
print("-" * 30)

if binance_vol is not None:
    print(f"Binance Volume : {binance_vol:,.0f} USDT")
else:
    print("Binance : the currency is not exist. ")

if mexc_vol is not None:
    print(f"MEXC Volume    : {mexc_vol:,.0f} USDT")
else:
    print("MEXC : the currency is not exist. ")

if binance_vol and mexc_vol:
    diff = binance_vol - mexc_vol
    print(f"Difference    : {diff:,.0f} USDT")















# symbol = input("symbol :")

# print("binance : " , get_binance_volume(symbol))
# print("mexc :" , get_mexc_volume(symbol))




# api =  " https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_vol=true "
