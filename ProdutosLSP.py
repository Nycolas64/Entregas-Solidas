class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_informacoes(self):
        return f"{self.nome} - R$ {self.preco:.2f}"

class Hamburguer(Produto):
    def __init__(self, nome, preco, tipo_carne):
        super().__init__(nome, preco)
        self.tipo_carne = tipo_carne

class Bebida(Produto):
    def __init__(self, nome, preco, volume_ml):
        super().__init__(nome, preco)
        self.volume_ml = volume_ml

class Suco(Bebida):
    def __init__(self, nome, preco, volume_ml, fruta):
        super().__init__(nome, preco, volume_ml)
        self.fruta = fruta