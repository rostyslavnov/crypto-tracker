import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI()

SYMBOL_TO_ID = {
    "btc": "btc-bitcoin",
    "eth": "eth-ethereum",
    "ltc": "ltc-litecoin",
    "xrp": "xrp-xrp"
}

SUPPORTED_FIAT = {"usd"}


async def fetch_price(coin_id: str, fiat: str):
    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"

    async with httpx.AsyncClient(timeout=10.0) as client:
        r = await client.get(url)

    if r.status_code != 200:
        raise HTTPException(
            status_code=502,
            detail=f"External API error: {r.status_code}"
        )

    data = r.json()

    fiat_upper = fiat.upper()
    if fiat_upper not in data["quotes"]:
        raise HTTPException(status_code=400, detail="Unsupported fiat")

    quote = data["quotes"][fiat_upper]

    return quote["price"], quote["percent_change_24h"]


@app.get("/price")
async def get_price(symbol: str = "btc", fiat: str = "usd"):
    symbol = symbol.lower()
    fiat = fiat.lower()

    if symbol not in SYMBOL_TO_ID:
        raise HTTPException(status_code=400, detail="Unsupported symbol")

    if fiat not in SUPPORTED_FIAT:
        raise HTTPException(status_code=400, detail="Unsupported fiat currency")

    coin_id = SYMBOL_TO_ID[symbol]
    price, change_24h = await fetch_price(coin_id, fiat)

    return {
        "symbol": symbol,
        "fiat": fiat,
        "price": price,
        "change_24h": change_24h,
    }
