from abc import ABC, abstractmethod

class Notificavel(ABC):
    @abstractmethod
    def enviar_notificacao(self, mensagem):
        pass

class Relatavel(ABC):
    @abstractmethod
    def gerar_relatorio(self):
        pass

class GerenciavelPedido(ABC):
    @abstractmethod
    def atualizar_status(self, novo_status):
        pass

class GerenciavelEntrega(ABC):
    @abstractmethod
    def atribuir_entregador(self, entregador):
        pass