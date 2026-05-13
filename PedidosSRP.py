class Pedido:
    def __init__(self, id, itens):
        self.id = id
        self.itens = itens
        self.total = self._calcular_total()

    def _calcular_total(self):
        return sum(item['preco'] for item in self.itens)

class PedidoRepository:
    def __init__(self):
        self._pedidos = []

    def salvar(self, pedido):
        self._pedidos.append(pedido)
        return True

class PedidoView:
    def exibir(self, pedido):
        print(f"Pedido ID: {pedido.id}")
        for item in pedido.itens:
            print(f"- {item['nome']}: R$ {item['preco']:.2f}")
        print(f"Total: R$ {pedido.total:.2f}")