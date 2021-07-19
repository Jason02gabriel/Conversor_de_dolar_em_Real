from forex_python.converter import CurrencyRates

c = CurrencyRates()

valor = float(input("Qual o valor em dólar você deseja converter para Real?\n"))

r = round(c.convert("USD","BRL",valor),2)

print(f"${valor} = {r}")