# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:54:31 2024

@author: carlo
"""

import psutil
import platform
import os

# Caminho do arquivo onde as informações serão salvas
caminho_arquivo = r"C:\Users\carlo\OneDrive\Documentos\Engenharia_Computacao\Reentrega_Python\info_sistema.txt"

# Função para obter informações do sistema
def obter_informacoes():
    # Obtendo informações do processador
    nucleo_fisico = psutil.cpu_count(logical=False)  # Núcleos físicos
    nucleo_logico = psutil.cpu_count(logical=True)   # Núcleos lógicos
    frequencia = psutil.cpu_freq().current           # Frequência em MHz

    # Obtendo informações da memória
    memoria = psutil.virtual_memory()
    total_memoria = memoria.total / (1024 ** 3)  # Convertendo para GB
    memoria_utilizada = memoria.used / (1024 ** 3)  # Convertendo para GB
    memoria_disponivel = memoria.available / (1024 ** 3)  # Convertendo para GB
    percentual_memoria = memoria.percent

    # Obtendo informações do disco
    disco = psutil.disk_usage('/')
    total_disco = disco.total / (1024 ** 3)  # Convertendo para GB
    disco_utilizado = disco.used / (1024 ** 3)  # Convertendo para GB
    disco_livre = disco.free / (1024 ** 3)  # Convertendo para GB
    percentual_disco = disco.percent

    # Formatando as informações
    informacoes = (
        f"Núcleos Físicos: {nucleo_fisico}\n"
        f"Núcleos Lógicos: {nucleo_logico}\n"
        f"Frequência do Processador: {frequencia:.2f} MHz\n\n"
        f"Total de Memória: {total_memoria:.2f} GB\n"
        f"Memória Utilizada: {memoria_utilizada:.2f} GB\n"
        f"Memória Disponível: {memoria_disponivel:.2f} GB\n"
        f"Percentual de Memória Utilizada: {percentual_memoria:.2f}%\n\n"
        f"Total de Espaço em Disco: {total_disco:.2f} GB\n"
        f"Espaço Utilizado: {disco_utilizado:.2f} GB\n"
        f"Espaço Livre: {disco_livre:.2f} GB\n"
        f"Percentual de Uso do Disco: {percentual_disco:.2f}%\n"
    )

    return informacoes

# Obtendo as informações
informacoes = obter_informacoes()

# Salvando as informações em um arquivo texto
with open(caminho_arquivo, 'w') as f:
    f.write(informacoes)

print(f"As informações foram salvas em '{caminho_arquivo}'.")