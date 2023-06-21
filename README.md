# Escripts

[Argparse](https://docs.python.org/3/library/argparse.html), [Poetry](https://python-poetry.org/) e algums *scripts* na linha de comando para testes.

## Utilização

As seguintes funcionalidades estão disponíveis via linha de comando:

- Envio de email teste
- Conexão e consulta a um banco de dados Postgresql

### Envio de email teste

Usuario e senha são opcionais, mas devem ser utilizados junto com a flag ```--login```. O remetente é obtido
da concatenação usuario (default: admin) @ hostname.

```bash
escripts email //usuario:senha@smtp.domain.com:465 destinatario@domain.com 'Mensagem do email' --login
```

`Remetente: usuario@smtp.domain.com`

ou

```bash
escripts email //@localhost:1025 destinatario@domain.com 'Mensagem do email'
```

`Remetente: admin@localhost`


### Conexão e consulta a um banco de dados Postgresql

```bash
escripts banco //usuario:senha@localhost:5432/database 'select * from administrativo.usuarios_usuario'
```
