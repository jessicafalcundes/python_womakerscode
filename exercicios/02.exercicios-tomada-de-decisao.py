# 01 - Faça um Programa que peça dois números e imprima o maior deles.

# Solicita dois números ao usuário
"""num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Compara os números e imprime o maior
if num1 > num2:
    print(f"O maior número é: {num1}")
elif num2 > num1:
    print(f"O maior número é: {num2}")
else:
    print("Os dois números são iguais.")"""

# Esse código utiliza float(input()) para permitir a entrada de números decimais e inclui uma verificação para o caso de os números serem iguais.




# 02 - Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-Matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

# Solicita ao usuário que informe o turno em que estuda
"""turno = input("Em que turno você estuda? Digite M para Matutino, V para Vespertino ou N para Noturno: ").strip().upper()

# Verifica o turno e imprime a mensagem correspondente
if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")"""

# Esse código 
# usa .strip().upper() para remover espaços extras e aceitar letras minúsculas e maiúsculas.
# Verifica a entrada e imprime a saudação correspondente ou "Valor Inválido!" caso o usuário digite algo diferente das opções esperadas.




# 03 - Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

"""while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    
    if 0 <= nota <= 10:
        print("Nota válida!")
        break
    else:
        print("Valor inválido. Por favor, digite uma nota entre 0 e 10.")"""

# Este código usa um loop while True, que continuará até que o usuário insira uma nota válida. Se a nota for inválida, ele mostrará uma mensagem de erro e pedirá novamente.




# 04 - Implemente um programa que classifique um aluno com base em sua pontuação em um exame. 
# O programa deverá solicitar uma nota de 0 a 10. Se a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é reprovado.

"""nota = float(input("Digite a nota do aluno (0 a 10): "))

if 0 <= nota <= 10:
    if nota >= 7:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")
else:
    print("Nota inválida. Digite uma nota entre 0 e 10.")"""




# 05 - Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
# equilátero: todos os lados com o mesmo valor
# isósceles: dois lados com o mesmo valor
# escaleno: todos os lados com medidas distintas.

"""lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Os comprimentos dos lados devem ser maiores que zero.")
else:
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero.")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")"""




# 06 - Crie um programa que solicite ao usuário um login e uma senha. 
# O programa deve permitir o acesso apenas se o usuário for "admin" e a senha for "admin123", caso contrário imprima uma mensagem de erro.

"""login = input("Digite o login: ")
senha = input("Digite a senha: ")

if login == "admin" and senha == "admin123":
    print("Acesso permitido!")
else:
    print("Login ou senha inválidos. Acesso negado.")"""




# 07 - Desenvolver um programa que solicite a idade do usuário e identifique se ele é uma criança, um adolescente, adulto ou idoso.

"""idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida.")
elif idade <= 12:
    print("Você é uma criança.")
elif idade <= 17:
    print("Você é um adolescente.")
elif idade <= 59:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")"""




# 08 - Criar um programa em Python que solicite três números ao usuário.
# utilize estruturas condicionais para determinar o maior entre eles e apresente o resultado.

"""n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 >= n2 and n1 >= n3:
    print(f"O maior número é {n1}.")
elif n2 >= n1 and n2 >= n3:
    print(f"O maior número é {n2}.")
else:
    print(f"O maior número é {n3}.")"""




# 09 - O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos. 
# O processo de leitura deve ser encerrado quando o usuário informar o valor zero. 
# Certifique-se de incluir validações para garantir que apenas números positivos sejam considerados na contagem e cálculos.

"""pares = 0
impares = 0

while True:
    numero = int(input("Digite um número positivo (ou 0 para encerrar): "))
    
    if numero == 0:
        break
    
    if numero < 0:
        print("Por favor, digite apenas números positivos.")
        continue
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")"""




# 10 - Faça um programa que lê três números inteiros e os mostra em ordem crescente.

"""n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

# Coloca os números em uma lista e ordena
numeros = [n1, n2, n3]
numeros.sort()

print("Os números em ordem crescente são:", numeros)"""

# Esse programa lê três números inteiros, coloca-os em uma lista e utiliza o método .sort() para ordenar os números em ordem crescente.




# 11 - Escreva um programa que calcule o salário líquido. Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.
# Renda até R$ 1.903,98: isento de imposto de renda;
# Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
# Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
# Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
# Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.

"""salario_bruto = float(input("Digite o salário bruto: R$ "))

# Determina a alíquota do imposto de renda com base na faixa de salário
if salario_bruto <= 1903.98:
    desconto_ir = 0
elif salario_bruto <= 2826.65:
    desconto_ir = salario_bruto * 0.075
elif salario_bruto <= 3751.05:
    desconto_ir = salario_bruto * 0.15
elif salario_bruto <= 4664.68:
    desconto_ir = salario_bruto * 0.225
else:
    desconto_ir = salario_bruto * 0.275

# Calcula o salário líquido
salario_liquido = salario_bruto - desconto_ir

# Exibe o resultado
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Desconto de Imposto de Renda: R$ {desconto_ir:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")"""

# Solicita o salário bruto.
# Calcula o desconto do Imposto de Renda de acordo com a faixa de renda.
# Subtrai o imposto do salário bruto para calcular o salário líquido.
# Exibe o salário bruto, o valor do imposto e o salário líquido.