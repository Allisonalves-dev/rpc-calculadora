# 🧮 Calculadora Remota com XML-RPC em Python

Este projeto demonstra a utilização de **RPC (Remote Procedure Call)** com a biblioteca **xmlrpc** do Python para implementar uma **calculadora distribuída**.

## 📁 Estrutura

- `server.py`: servidor XML-RPC com funções matemáticas
- `cliente.py`: cliente que consome as funções do servidor
- `exemplos/`: prints da execução

## 🚀 Como Executar

1. Execute o servidor:

```bash
python server.py

Em outro terminal, execute o cliente:

bash
Copiar
Editar
python cliente.py
Escolha as opções do menu e interaja com a calculadora.

📷 Exemplos de execução


🧠 Funcionalidades implementadas
Soma

Multiplicação

Divisão (com tratamento de erro)

Potência

Fatorial (com validação de número negativo)

👨‍💻 Tecnologias
Python 3

xmlrpc.server

xmlrpc.client
