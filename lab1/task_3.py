import requests
import datetime
import matplotlib.pyplot as plt


start = "20240101"  
end   = "20241117"  
valcode = "USD"     


url = (
    f"https://bank.gov.ua/NBU_Exchange/exchange_site?"
    f"start={start}&end={end}&valcode={valcode}&sort=exchangedate&order=asc&json"
)

response = requests.get(url)
response.raise_for_status()
data = response.json()

dates = []
rates = []
for entry in data:
    dt = datetime.datetime.strptime(entry["exchangedate"], "%d.%m.%Y")
    dates.append(dt)
    rates.append(entry["rate"])

plt.figure(figsize=(10, 6))
plt.plot(dates, rates, marker='o', linestyle='-', color='blue', label="USD → UAH")
plt.title("Зміна курсу Долара США до Гривні (UAH)")
plt.xlabel("Дата")
plt.ylabel("Курс (UAH за 1 USD)")
plt.grid(True)
plt.legend()
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.show()
