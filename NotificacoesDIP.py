from abc import ABC, abstractmethod

class Notificacao(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass

class NotificacaoEmail(Notificacao):
    def enviar(self, mensagem):
        print(f"Enviando E-mail: {mensagem}")

class NotificacaoSMS(Notificacao):
    def enviar(self, mensagem):
        print(f"Enviando SMS: {mensagem}")

class NotificacaoWhatsApp(Notificacao):
    def enviar(self, mensagem):
        print(f"Enviando WhatsApp: {mensagem}")

class ServicoNotificacao:
    def __init__(self, meio_notificacao: Notificacao):
        self.meio_notificacao = meio_notificacao

    def notificar_cliente(self, mensagem):
        self.meio_notificacao.enviar(mensagem)