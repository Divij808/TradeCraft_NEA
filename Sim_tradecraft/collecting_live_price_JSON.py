import json
import re

# ---------- LOAD JSON ----------
with open("Companies_updated.json", "r", encoding="utf-8") as file:
    stocks = json.load(file)


# ---------- NORMALIZE TEXT ----------
def normalize(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())


# ---------- FIND LIVE PRICE ----------
def get_live_price(company_name):
    query = normalize(company_name)

    for stock in stocks:
        name = normalize(stock["name"])
        symbol = normalize(stock["symbol"])
        live_price = stock["live_price"]

        if query in name or query == symbol:
            return {
                "name": stock["name"],
                "symbol": stock["symbol"],
                "live_price": stock["live_price"],
                "image": stock["image"]
            }

    return None


# ---------- TEXT INPUT ----------
def live_price(symbol):
    result = get_live_price(symbol)

    price = result['live_price']
    return price
