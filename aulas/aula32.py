"""
01.Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
02.Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
03.Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# Exercício 01

numero_str = input("Digite um número inteiro: ")

try:
    numero_int = int(numero_str)
    if numero_int % 2 == 0:
        print(f'O número {numero_int} é par')
    else:
        print(f'O número {numero_int} é ímpar')
except:
    print('Isso não é um número inteiro')

# Exercício 02

hora_str = input('Digite a hora atual: ')

try:
    hora_int = int(hora_str)
    if hora_int < 0 or hora_int > 23:
        print('Hora inválida')
    else:
        if hora_int < 12:
            print('Bom dia')
        elif hora_int < 18:
            print('Boa tarde')
        else:
            print('Boa noite')
except:
    print('Isso não é um número inteiro')

# Exercício 03

nome = input('Digite seu primeiro nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')