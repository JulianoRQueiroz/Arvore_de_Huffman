from Nodo import Node

class Huffman: # Declaração das variaveis para a criação da arvore de Huffman
    
    arvore: str = None # Retorna a arvore
    raiz: str = None # Retorna a raiz
    nos: str = [] # Vetor dos nos da lista
    evento: str = {}  # Conjunto 
    dict_codificado: str = {} # Dicionario codificador
    
    def __init__(self: object, simbolos: str) -> None:
        self.iniciando_nos(simbolos) # retorna valores
        self.construindo_arvore()
        self.construindo_dicionario()
        
    def iniciando_nos(self: object, evento: str): 
        for simbolo in evento:
            node = Node() # Iniciamos o node
            node.simbolo = simbolo
            node.probabilidade = evento[simbolo] # atibuimos uma possibilidade a cada simbolo e letra
            node.visited = False # variável que não é fixa que mudará
            self.nos.append(node) # Criamos uma lista para cada nodo 
            self.evento[simbolo] = evento[simbolo] # estabelece para cada possbilidade um simbolo
            
    def construindo_arvore(self: object): # Realizamos as operações de acordo com instruções de construção da arvore de Huffman
        indexMin1: float = self.no_min() # Buscamos o menor numero da primira possibilidade
        indexMin2: float = self.no_min() # Buscamos o menor numero da segunda possibilidade
        
        while indexMin1 != -1 and indexMin2 != -1: # avalia como verdadeiro se 2 variáveis ​​forem diferentes
            node = Node()
            node.simbolo = "." # Eu chamo o símbolo digitado para me dar o resultado
            node.cod = ""
            # Eu chamo para as possibilidades minimas
            prob1: float = self.nos[indexMin1].probabilidade
            prob2: float = self.nos[indexMin2].probabilidade
            node.probabilidade = prob1 + prob2 # Soma as possibilidades
            node.visited = False # Falso = 1 
            node.visto = -1 # subtraímos a probabilidade
            self.nos.append(node)
            self.nos[indexMin1].visto = len(self.nos) - 1 # lista a string que queremos medir
            self.nos[indexMin2].visto = len(self.nos) - 1 # lista a string que queremos medir
            
            # Regra: 0 a maior possibilidae, 1 a menor possibildidade
            if prob1 >= prob2:
                self.nos[indexMin1].cod = "0"
                self.nos[indexMin2].cod = "1"
            else:
                self.nos[indexMin1].cod = "0"
                self.nos[indexMin2].cod = "1"
                
            indexMin1 = self.no_min()
            indexMin2 = self.no_min()
            
    def no_min(self: object) -> str: #  É realizada uma comparação para obter o nodo da menor possibilidade
        minPorb = 1.0 # a minima possibilidade não pode ser maior que 1
        indexMin = -1 # indicie para subtrair da possibilidade
        
        for index in range(0, len(self.nos)): # indice é o numero de probabilidade
            if (self.nos[index].probabilidade < minPorb and (not self.nos[index].visited)): # se o indice for menor que 1 é falso
                minPorb = self.nos[index].probabilidade
                indexMin = index
        
        if indexMin != -1:
            self.nos[indexMin].visited = True
        return indexMin
    
    def simbolo_cod(self: object, simbolo: str) -> str: # realizamos um codigo binario a cada simbolo resolvido pela arvore de Huffman
        found: bool = False
        index: int = 0
        cod: str = "" 
        
        for i in range(0, len(self.nos)):
            if self.nos[i].simbolo == simbolo: # como definimos o codigo binario
                found = True
                index = i 
                break
            
        if found:
            while index != -1: # se encontrado for verdadeiro então enquanto o índice é distinto de -1 ele será salvo na codificação e lá ele nos enviará o resultado
                cod = "%s%s" % (self.nos[index].cod, cod)
                index = self.nos[index].visto
        else:
            cod = "Simbolo desconhecido"
        return cod
    
    def construindo_dicionario(self: object) -> str:
        """Crimos um dicionario, gaurdamos todos os simbolos em seus respectivos codigos binarios
        resolvidos pela arvore de Huffman """
        for simbolo in self.evento:
            cod = self.simbolo_cod(simbolo)
            self.dict_codificado[simbolo] = cod
            
    def codificar_arvore(self: object, cod_bin) -> str: 
        """Junta os codigos binarios codificados de acordo com a mensagem escrita"""
        cod: str = ""
        for simbolo in cod_bin:
            cod = "%s%s" % (cod, self.dict_codificado[simbolo])
        return cod
    
    # Inicio da codificação
    def decodificar_arvore(self: str, cod: str): # recebe a corrente do cod bin enviado
        index: int = 0 
        decodificado: str = ""
        
        while index < len(cod): 
            """à medida que pesquisamos o comprimento da parte da codificação"""
            found: bool = False # Estabelecemos uma variavel 
            
            auxiliar: None = cod[index:] 
            """irá procurar um símbolo para cada parte codificada, não ficará fixo, 
            irá procurar qual é compatível com cada uma"""
            
            for simbolo in self.evento:
                if auxiliar.startswith(self.dict_codificado[simbolo]): 
                    decodificado = f"{decodificado}{simbolo}" # parte decodificada
                    index = index + len(self.dict_codificado[simbolo]) # busca para cada simbolo a cada possibilidade
                    break
        return decodificado