import argparse

from .banco import ClienteBanco
from .mail import ClienteEmail


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcomando')

    banco = subparsers.add_parser('banco')
    banco.add_argument('db_url')
    banco.add_argument('sql')

    email = subparsers.add_parser('email')
    email.add_argument('email_url')
    email.add_argument('destinatario')
    email.add_argument('mensagem', default='Testando linha de comando')
    email.add_argument('--login', action='store_true', default=False)

    args = parser.parse_args()

    match args.subcomando:
        case 'banco':
            with ClienteBanco(args.db_url) as cliente:
                cliente.executar(args.sql)

        case 'email':
            cliente = ClienteEmail(args.email_url, args.login)
            cliente.enviar_email(args.destinatario, args.mensagem)
