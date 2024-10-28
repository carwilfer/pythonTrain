# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 23:00:30 2024

@author: carlo
"""

import socket
import psutil
import pickle

# Funções para obter informações do sistema
def obter_informacoes_memoria():
    memoria = psutil.virtual_memory()
    return {
        'Total': memoria.total,
        'Usada': memoria.used,
        'Disponível': memoria.available,
        'Percentual': memoria.percent
    }

def obter_informacoes_processador():
    return {
        'Núcleos Físicos': psutil.cpu_count(logical=False),
        'Núcleos Lógicos': psutil.cpu_count(logical=True),
        'Frequência (MHz)': psutil.cpu_freq().current
    }

def obter_informacoes_disco():
    disco = psutil.disk_usage('/')
    return {
        'Total': disco.total,
        'Usado': disco.used,
        'Livre': disco.free,
        'Percentual': disco.percent
    }

def obter_informacoes_processos():
    processos = [p.info for p in psutil.process_iter(attrs=['pid', 'name', 'status'])]
    return processos

# Configuração do servidor
HOST = '127.0.0.1'  # Endereço IP local
PORT = 65432        # Porta que o servidor irá escutar

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind((HOST, PORT))
    servidor.listen()
    print("Servidor ouvindo na porta", PORT)
    conn, addr = servidor.accept()
    
    with conn:
        print("Conectado por", addr)
        while True:
            opcao = conn.recv(1024)
            if not opcao:
                break

            opcao = pickle.loads(opcao)  # Deserializa a opção recebida
            if opcao == 1:
                resposta = obter_informacoes_memoria()
            elif opcao == 2:
                resposta = obter_informacoes_processador()
            elif opcao == 3:
                resposta = obter_informacoes_disco()
            elif opcao == 4:
                resposta = obter_informacoes_processos()
            elif opcao == 0:
                break  # Encerra o servidor se a opção 0 for recebida
            else:
                resposta = "Opção inválida!"

            conn.sendall(pickle.dumps(resposta))  # Serializa e envia a resposta