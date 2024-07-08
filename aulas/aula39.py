"""
Iterando strings com while
"""

# 012345678910
nome = 'Júlio César' #Iteráveis
#1110987654321
print(nome)
tamanho_nome = len(nome)
nova_string_tamanho = 0
novo_nome = ''

while nova_string_tamanho < tamanho_nome:
    novo_nome += nome[nova_string_tamanho]
    if nova_string_tamanho < tamanho_nome - 1:
        novo_nome += '*'
    nova_string_tamanho += 1

print(novo_nome)


"""
indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
"""