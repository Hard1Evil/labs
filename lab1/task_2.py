import requests
from datetime import datetime, timedelta

def get_exchange_rates(currency_code="CZK"):
    end = datetime.today()
    start = end - timedelta(days=7)

    url = (
        "https://bank.gov.ua/NBU_Exchange/exchange_site?"
        f"start={start:%Y%m%d}&end={end:%Y%m%d}&"
        f"valcode={currency_code}&sort=exchangedate&order=asc&json"
    )

    return requests.get(url).json()

def print_rates_table(rates):
    print(f"{'Date':<12} {'Currency':<10} {'Rate':<10}")
    print("-" * 34)

    for r in rates:
        date = r["exchangedate"]
        cc = r["cc"]
        rate = r["rate"]
        print(f"{date:<12} {cc:<10} {rate:<10}")

data = get_exchange_rates("USD")
print_rates_table(data)
