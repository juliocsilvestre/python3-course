name = "Julio Silvestre"
altura = 1.70
peso = 72
imc = peso / (altura ** 2)

print(name, "tem", altura, "de altura e", peso, "de peso. Seu IMC é", imc)

"f-strings"
linha_1 = f'{name} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)