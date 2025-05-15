# Define a classe que representa o ambiente (o "mundo") do agente
class Mundo:
    def __init__(self):
        # Cada célula do mundo 2x2 contém uma lista de percepções:
        # 'B' = brisa (indicando que há um poço em algum vizinho)
        # 'P' = poço (cair aqui seria fatal para o agente)
        self.celulas = {
            (0, 0): ['B'],  # Brisa porque há um poço vizinho
            (0, 1): ['P'],  # Poço real
            (1, 0): ['B'],  # Também com brisa por causa do poço ao lado
            (1, 1): []      # Célula segura, sem percepções
        }

    # Método que retorna as percepções de uma célula (posição)
    def perceber(self, posicao):
        return self.celulas.get(posicao, [])


# Define a classe do agente lógico que explora o mundo
class AgenteLogico:
    def __init__(self, mundo):
        self.mundo = mundo  # Referência ao mundo onde ele se move
        self.posicao_atual = (0, 0)  # Começa no canto superior esquerdo
        self.visitadas = set()       # Células que já foram visitadas
        self.perigos = set()         # Células marcadas como perigosas
        self.brisas = set()          # Células onde foi sentida brisa

    # Retorna as posições vizinhas válidas (dentro da grade 2x2)
    def vizinhos(self, x, y):
        return [(nx, ny) for nx, ny in 
                [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
                if 0 <= nx <= 1 and 0 <= ny <= 1]

    # Atualiza o conhecimento do agente com base na percepção atual
    def atualizar_conhecimento(self, pos):
        percepcao = self.mundo.perceber(pos)
        print(f"\nVisitando {pos}, percepção: {percepcao}")
        self.visitadas.add(pos)  # Marca como visitada

        # Se houver brisa, significa que há um poço em algum vizinho
        if 'B' in percepcao:
            self.brisas.add(pos)
            print(f"Brisa detectada nos vizinhos de {pos}")
            for viz in self.vizinhos(*pos):
                if viz not in self.visitadas:
                    self.perigos.add(viz)  # Marca os vizinhos como perigosos
                    print(f"Marcando {viz} como possivelmente perigosa")

    # Decide para onde o agente deve ir a seguir
    def escolher_movimento(self):
        print("\nAnalisando vizinhos...")
        for viz in self.vizinhos(*self.posicao_atual):
            if viz not in self.visitadas and viz not in self.perigos:
                print(f"{viz} parece segura. Escolhendo essa posição.")
                return viz  # Move para uma célula segura
            elif viz not in self.visitadas:
                print(f"{viz} é suspeita. Evitando.")
        return None  # Nenhuma opção segura encontrada

    # Executa a rotina principal do agente
    def executar(self):
        while True:
            self.atualizar_conhecimento(self.posicao_atual)
            proximo = self.escolher_movimento()
            if proximo:
                self.posicao_atual = proximo  # Atualiza a posição
            else:
                print("\nNenhum movimento seguro disponível. Encerrando execução.")
                break  # Para se não houver movimento seguro


# Cria o mundo e o agente, e inicia a simulação
mundo = Mundo()
agente = AgenteLogico(mundo)
agente.executar()
