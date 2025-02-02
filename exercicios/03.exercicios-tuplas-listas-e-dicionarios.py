# 01 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
# As perguntas são:
# ""Telefonou para a vítima?""
# ""Esteve no local do crime?""
# ""Mora perto da vítima?""
# ""Devia para a vítima?""
# ""Já trabalhou com a vítima?""
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como ""Assassino"".
# Caso contrário,ele será classificado como ""Inocente"".

"""perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

# Contador de respostas "sim"
respostas_positivas = 0

# Loop para fazer as perguntas
for pergunta in perguntas:
    resposta = input(f"{pergunta} (sim/não): ").strip().lower()
    
    if resposta == "sim":
        respostas_positivas += 1

# Classificação com base nas respostas
if respostas_positivas == 2:
    classificacao = "Suspeita"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

# Exibe o resultado
print(f"A pessoa foi classificada como: {classificacao}")"""




# 02 - Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

"""alunos = 5
notas_por_aluno = 4
media_alunos = []

# Coleta as notas e calcula a média de cada aluno
for i in range(alunos):
    print(f"Aluno {i + 1}:")
    notas = []
    
    for j in range(notas_por_aluno):
        nota = float(input(f"Digite a nota {j + 1}: "))
        notas.append(nota)
    
    media = sum(notas) / notas_por_aluno
    media_alunos.append(media)

# Conta quantos alunos têm média >= 7.0
alunos_com_media_7 = sum(1 for media in media_alunos if media >= 7.0)

# Exibe o número de alunos com média maior ou igual a 7.0
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_com_media_7}")"""




# 03 Crie um dicionário representando um carrinho de compras. Adicione produtos (chaves) e quantidades (valores) ao carrinho. 
# Calcule o total do carrinho de compra.

# Dicionário do carrinho de compras
"""carrinho = {
    "arroz": 10.50,
    "feijão": 7.20,
    "macarrão": 4.90
}

# Dicionário para armazenar as quantidades dos produtos
quantidades = {
    "arroz": 2,
    "feijão": 3,
    "macarrão": 1
}

# Calcular o total do carrinho
total = 0
for produto, preco in carrinho.items():
    quantidade = quantidades.get(produto, 0)  # Obtém a quantidade do produto, se houver
    total += preco * quantidade

# Exibe o total do carrinho
print(f"Total do carrinho de compras: R$ {total:.2f}")"""




# 04 - Crie um dicionário representando contatos (nome, telefone). Permita ao usuário procurar por um contato pelo nome.

# Dicionário de contatos
"""contatos = {
    "fuinha": "1234-5678",
    "thiago": "9876-5432",
    "matheus": "5678-1234",
    "bruno": "4321-8765"
}

# Solicita o nome para buscar no dicionário
nome = input("Digite o nome para procurar o telefone: ").strip()

# Verifica se o nome está no dicionário e exibe o telefone
if nome in contatos:
    print(f"Telefone de {nome}: {contatos[nome]}")
else:
    print(f"Contato de {nome} não encontrado.")"""




# 05 - Crie duas tuplas. Concatene-as para formar uma nova tupla.

# Criação das tuplas
"""tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

# Concatenação das tuplas
tupla_concatenada = tupla1 + tupla2

# Exibe a tupla concatenada
print("Tupla concatenada:", tupla_concatenada)"""




# 06 - Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. 
# Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

# Solicita o nome do usuário
"""nome = input("Digite seu nome: ")

# Inverte o nome e converte para maiúsculas
nome_invertido = nome[::-1].upper()

# Exibe o nome invertido em maiúsculas
print("Nome invertido:", nome_invertido)"""

# Inverte o nome usando slicing ([::-1]).
# Converte o nome invertido para maiúsculas usando o método .upper().