# 01 - Faça um Programa que peça dois números, realize as principais operações soma, subtração, multiplicação, divisão

# Solicita dois números ao usuário
"""num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza as operações
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Evita divisão por zero
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Erro! Divisão por zero não é permitida."

# Exibe os resultados
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")"""




# 02 - Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual.

"""from datetime import date

# Obtém o ano atual
ano_atual = date.today().year

# Solicita o ano de nascimento ao usuário
ano_nascimento = int(input("Digite o ano do seu nascimento: "))

# Calcula a idade
idade = ano_atual - ano_nascimento

# Exibe a idade
print(f"Você tem {idade} anos.")"""




# 03 - Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.

# Solicita a quantidade de quilômetros ao usuário
"""km = float(input("Digite a quantidade de quilômetros: "))

# Conversões
metros = km * 1000
centimetros = km * 100000
milimetros = km * 1000000

# Exibe os resultados
print(f"{km} km equivalem a:")
print(f"{metros} metros")
print(f"{centimetros} centímetros")
print(f"{milimetros} milímetros")"""




# 04 - Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l.

# Solicita os dados ao usuário
"""litros = float(input("Digite a quantidade de litros de combustível consumidos: "))
distancia = float(input("Digite a distância percorrida em quilômetros: "))

# Evita divisão por zero
if litros > 0:
    consumo_medio = distancia / litros
    print(f"O consumo médio do veículo é de {consumo_medio:.2f} km/l.")
else:
    print("Erro! A quantidade de litros deve ser maior que zero.")"""




# 05 - Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião, carro e ônibus.
# Levando em consideração: avião = 600 km/h carro = 100 km/h ônibus = 80 km/h

# Velocidades médias em km/h
"""velocidade_aviao = 600
velocidade_carro = 100
velocidade_onibus = 80

# Solicita a distância da viagem ao usuário
distancia = float(input("Digite a distância da viagem em quilômetros: "))

# Calcula o tempo de viagem para cada meio de transporte
tempo_aviao = distancia / velocidade_aviao
tempo_carro = distancia / velocidade_carro
tempo_onibus = distancia / velocidade_onibus

# Exibe os resultados
print("\nTempo estimado de viagem:")
print(f"Avião: {tempo_aviao:.2f} horas")
print(f"Carro: {tempo_carro:.2f} horas")
print(f"Ônibus: {tempo_onibus:.2f} horas")"""





# 06 - Solicite ao usuário o peso em kg e a altura em metros. Calcule e imprima o Índice de Massa Corporal (IMC) usando a fórmula:
# IMC = peso / (altura x altura).

# Solicita os dados ao usuário
"""peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o resultado
print(f"Seu Índice de Massa Corporal (IMC) é: {imc:.2f}")"""





# 07 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

# Solicita os dados ao usuário
"""valor_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcula o salário total
salario = valor_hora * horas_trabalhadas

# Exibe o resultado
print(f"Seu salário no mês será de R$ {salario:.2f}")"""




# 08 - Solicite ao usuário o número de horas de exercício físico por semana.
# Calcule o total de calorias queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício.

# Solicita o número de horas de exercício por semana
"""horas_por_semana = float(input("Digite o número de horas de exercício por semana: "))

# Converte horas para minutos
minutos_por_semana = horas_por_semana * 60

# Calcula calorias queimadas por semana e por mês
calorias_por_semana = minutos_por_semana * 5
calorias_por_mes = calorias_por_semana * 4  # Considerando um mês com 4 semanas

# Exibe o resultado
print(f"Você queima aproximadamente {calorias_por_mes:.0f} calorias por mês com esses exercícios.")"""




# 09 - Faça um Programa que utilize 4 variáveis como preferir e no final print uma mensagem amigável utilizando as variáveis criadas.
# Exemplos de variáveis: nome, idade, lugar, profissão ....
# Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo também e estou migrando de área.
# Lembrando que para o retorno vamos usar print com as variáveis criadas e este texto é somente um exemplo, utilizem a criatividade.

# Definição das variáveis
"""nome = input("Qual é o seu nome? ")
idade = input("Quantos anos você tem? ")
cidade = input("De qual cidade você é? ")
hobby = input("O que você gosta de fazer no tempo livre? ")

# Mensagem amigável com as variáveis
print(f"\nOlá, {nome}! Que legal saber que você tem {idade} anos e é de {cidade}.")
print(f"Eu também acho incrível quando as pessoas têm hobbies como {hobby}. Vamos conversar mais sobre isso!")"""