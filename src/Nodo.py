

class Node: # Declaração de variáveis para criar os nodos
    
    def __init__(self: object) -> None:
        self.probabilidade: float = 0.0 # Declaração em float OCORRENCIA dos envento
        self.simbolo: str = "" # variavel vazia
        self.visto: bool = False # variavel boolena
        self.folha: int = -1 # comprimento de 0 a -1, varivel inteira
        