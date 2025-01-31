def multiplicacao():
    mult = 10*2
    

    file = 'arquivo.txt'
    # abertura de arquivo
    
    # abertura para escrita
    arquivo_escrita = open(file, "w")
    arquivo_escrita.write(f'o resultado da multiplicação é: {mult}')
    arquivo_escrita.close()
    
    # open somente para leitura
    arquivo_leitura = open(file, "r")
    leitura = arquivo_leitura.reed()
    print(leitura)
    arquivo_leitura.close()

    # print(f'o resultado da multiplicação é: {mult}')

#multiplicacao() # chamada de função