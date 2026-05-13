print("Iniciando o Sistema Entregas Sólidas")


from PedidosSRP import Pedido, PedidoRepository, PedidoView
from ProdutosLSP import Hamburguer, Suco
from PagamentosOCP import PagamentoPIX, ProcessadorPagamento
from NotificacoesDIP import NotificacaoWhatsApp, ServicoNotificacao

hamburguer = Hamburguer("X-Sólido", 30.00, "Bovina")
suco = Suco("Suco de Laranja", 12.00, 500, "Laranja")

itens_pedido = [
    {"nome": hamburguer.nome, "preco": hamburguer.preco},
    {"nome": suco.nome, "preco": suco.preco}
]
novo_pedido = Pedido(id=303, itens=itens_pedido)

view = PedidoView()
repositorio = PedidoRepository()

view.exibir(novo_pedido)
repositorio.salvar(novo_pedido)

processador = ProcessadorPagamento()
processador.realizar_pagamento(novo_pedido.total, PagamentoPIX())

meio_whatsapp = NotificacaoWhatsApp()
notificador = ServicoNotificacao(meio_whatsapp)
notificador.notificar_cliente(f"Pedido {novo_pedido.id} confirmado!")