def divisao(a,b):
    try:
        resultado = a/b
        print(resultado)
    
    except ZeroDivisionError:
        print("erro: impossível dividir um valor por zero")
    except TypeError as e:
        print(f'erro: o tipo de dado informado está incorreto. \n detalhes: {e}')
    else:
        print('sem exceções') 


#divisao(10,2)
#divisao(10,0)
divisao(10,'rogerio')