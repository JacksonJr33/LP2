velocidade = float(input("Digite a velocidade do carro em km/h: "))
limite = 80

if velocidade > limite:
    km_acima = velocidade - limite
    valor_multa = km_acima * 20
    print(f"Você foi multado por exceder o limite de {limite} km/h.")
    print(f"Velocidade acima do limite: {km_acima:} km/h")
    print(f"Valor da multa: R${valor_multa:}")
else:
    print("Dentro do limite de velocidade!")
