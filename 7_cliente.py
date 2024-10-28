# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 23:02:30 2024

@author: carlo
"""

import socket
import pickle

def mostrar_menu():
    print("Menu de Opções:")
    print("[1] - Exibir informações sobre a memória principal")
    print("[2] - Exibir informações sobre o processador")
    print("[3] - Exibir informações sobre o disco")
    print("[4] - Exibir informações sobre os processos")
    print("[0] - Sair")

# Configuração do cliente
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta do servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))
    
    while True:
        mostrar_menu()
        opcao = int(input("Selecione uma opção: "))
        cliente.sendall(pickle.dumps(opcao))  # Serializa e envia a opção
        
        if opcao == 0:
            print("Saindo...")
            break
        
        resposta = cliente.recv(4096)  # Recebe a resposta do servidor
        resposta = pickle.loads(resposta)  # Deserializa a resposta
        print("Resposta do servidor:")
        print(resposta)  # Exibe a resposta