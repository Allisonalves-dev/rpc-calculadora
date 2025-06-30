from xmlrpc.server import SimpleXMLRPCServer
import math

def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def potencia(base, expoente):
    return base ** expoente

def fatorial(n):
    if n < 0:
        return "Erro: fatorial de número negativo"
    return math.factorial(n)

# Cria o servidor
server = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor RPC disponível em http://localhost:8000/")

# Registra as funções
server.register_function(somar, "somar")
server.register_function(multiplicar, "multiplicar")
server.register_function(dividir, "dividir")
server.register_function(potencia, "potencia")
server.register_function(fatorial, "fatorial")

# Inicia o servidor
server.serve_forever()
