primeiro_valor=input("Digite o primeiro valor: ")
segundo_valor=input("Digite o segundo valor: ")

primeiro_valor = int(primeiro_valor)
segundo_valor = int(segundo_valor)

if primeiro_valor > segundo_valor:
    print(
        f"O primeiro valor {primeiro_valor} é maior do que o segundo valor {segundo_valor}")
elif primeiro_valor < segundo_valor:
    print(
        f"O segundo valor {segundo_valor} é maior do que o primeiro valor {primeiro_valor}")
else:
    print(
        f"Os valores do primeiro valor: {primeiro_valor} e segundo valor: {segundo_valor} são iguais")
