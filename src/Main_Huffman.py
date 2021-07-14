import os
from colorama import Fore, Style
from time import time
from Huffman import Huffman

if __name__ == "__main__":
    print(Fore.YELLOW + "\n---------------- CODIFICAÇÃO ------------------"+ Style.RESET_ALL)
    # Código para pegar texto do arquivo txt
    arquivo: str = open("src/entrada.txt", "r", encoding="UTF-8")
    mensagem: str = ""
    line: str = arquivo.readline()
    
    while line:
        line = arquivo.readline()
        mensagem = mensagem + line
    arquivo.close()

    # Código para pegar texto string digitado no input
    # mensagem = input(Fore.MAGENTA + 'Informe o texto: '+ Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+ f"\nTOTAL DE CARACTÉRES: \n {len(mensagem)}" + Style.RESET_ALL)
    simbolos: str = ''
    probabilidade: str = []
    msm: str = mensagem
    contador: float = 0
    
    for i in mensagem:
        if i in msm:
            simbolos += i
            probabilidade.append(float(float(msm.count(i))/float(len(mensagem))))
            msm = msm.replace(i,'')
            contador += 1
    simbolos = dict(zip(simbolos, probabilidade)) # função para chamar o simbolo e a sua possibilidade
    print(Fore.LIGHTBLUE_EX+f"\nCARACTERES COMPRIMIDOS: \n {contador} " + Style.RESET_ALL) # imprime a quantidade que contabiliza a função count
    # print(f"\nPROBABILIDADE DE CADA SIMBOLO:\n {simbolos}")
    
    tempo_inicial = time() # função para determinar o tempo do programa
    
    # Codificação dos simbolos 
    huffman = Huffman(simbolos) # Instaciamos a classe Huffman
    print(Fore.LIGHTCYAN_EX +"\nCARACTÉRES CODIFICADOS UTILIZANDO A ÁRVORE DE HUFFMAN: "+ Style.RESET_ALL)
    for simbolo in simbolos:
        print(f"Caracter: {simbolo} - Codigo Binário: {huffman.simbolo_cod(simbolo)}")
        
    codigo = huffman.codificar_arvore(mensagem) # Chama a função fazendo o procedimento de decodificação
    print(Fore.LIGHTMAGENTA_EX +f"\nCODIFICAÇÃO EM BITS: \n {codigo}"+ Style.RESET_ALL) # mostramos a mensagem em bits
    print(Fore.LIGHTBLUE_EX +f"\nO COMPRIMENTO DO CODIGO BINÁRIO: \n{len(codigo)}"+ Style.RESET_ALL)
    
    data = codigo
    
    # Decodificação
    print(Fore.YELLOW + "\n---------------- DECODIFICAÇÃO ------------------"+ Style.RESET_ALL)
    decodificar = huffman.decodificar_arvore(data) # Chamanos as funções corespondentes e mensagens do dado
    print(Fore.GREEN + f"CODIGO BINÁRIO PARA DECODIFICAR:\n{data}" + Style.RESET_ALL)
    print(Fore.BLUE + f"\nMENSSAGEM: \n{decodificar}" + Style.RESET_ALL) # imprimimos o resultado da função decoded
    
    # calculo para o tempo do processo
    tempo_final = time()
    tempo_execucao = tempo_final - tempo_inicial
    print(Fore.RED + "\n----------------------------------------------------------------------" + Style.RESET_ALL)
    print(Fore.RED + f"O tempo de execução: {tempo_execucao}" + Style.RESET_ALL)
    print(Fore.RED + "----------------------------------------------------------------------" + Style.RESET_ALL)

os._exit(0)
