pesos = input("¿Cuántos pesos Colombianos tienes?: ")
pesos = float(pesos)
valor_dolar = 3700
dolares = pesos/valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")
