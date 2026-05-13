from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class PagamentoCartao(MetodoPagamento):
    def processar(self, valor):
        print(f"Processando pagamento de R$ {valor:.2f} via Cartão.")

class PagamentoPIX(MetodoPagamento):
    def processar(self, valor):
        print(f"Gerando QR Code para pagamento de R$ {valor:.2f} via PIX.")

class PagamentoDinheiro(MetodoPagamento):
    def processar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} registrado para recebimento em dinheiro.")

class ProcessadorPagamento:
    def realizar_pagamento(self, valor, metodo: MetodoPagamento):
        metodo.processar(valor)