import email.message
import smtplib
import ssl
import urllib.parse


class ClienteEmail:

    def __init__(self, email_url, login=False):
        self.email_url = email_url
        self.login = login

    def enviar_email(self, destinatario, mensagem):
        context = ssl.create_default_context()
        config = urllib.parse.urlparse(self.email_url)

        remetente = f'{config.username or "admin"}@{config.hostname}'
        mensagem = self.obter_email_message(remetente, destinatario, mensagem)

        port = int(config.port)
        if port == 465:
            with smtplib.SMTP_SSL(config.hostname, port, context=context) as server:
                if self.login:
                    server.login(config.username, config.password)

                server.send_message(mensagem)

        else:
            with smtplib.SMTP(config.hostname, port) as server:
                if self.login:
                    server.starttls(context=context)
                    server.login(config.username, config.password)

                server.send_message(mensagem)

    def obter_email_message(self, remetente, destinatario, mensagem):
        message = email.message.EmailMessage()
        message['Subject'] = 'Email teste'
        message['From'] = remetente
        message['To'] = destinatario
        message.set_content(mensagem)
        return message
