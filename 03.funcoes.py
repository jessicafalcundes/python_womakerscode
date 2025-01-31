def soma(num1,num2): # definição da função soma  
    calculo = num1+num2
    print(f'o resultado da soma é: {calculo}')

def subtracao(num1,num2): #variável não pode ter o mesmo nome da função!!!
    sub = num1-num2
    print(f'o resultado da subtração é: {sub}')
    

def multiplicacao(num1,num2):
    mult = num1*num2
    print(f'o resultado da multiplicação é: {mult}')

num1 = int(input('digite o primeiro número: '))
num2 = int(input('digite o segundo número: '))
soma(num1,num2) #chamada de função
subtracao(num1,num2)
multiplicacao(num1,num2)



# parâmetros