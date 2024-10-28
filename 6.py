# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:46:33 2024

@author: carlo
"""

# Caminho dos arquivos
caminho_arq1 = r"C:\Users\carlo\OneDrive\Documentos\Engenharia_Computacao\Reentrega_Python\arq1.txt"
caminho_arq2 = r"C:\Users\carlo\OneDrive\Documentos\Engenharia_Computacao\Reentrega_Python\arq2.txt"
caminho_arq3 = r"C:\Users\carlo\OneDrive\Documentos\Engenharia_Computacao\Reentrega_Python\arq3.txt"

# Função para ler números de um arquivo e retorná-los como uma lista de inteiros
def ler_numeros(arquivo):
    with open(arquivo, 'r') as f:
        numeros = f.read().splitlines()  # Lê cada linha do arquivo
    return [int(num) for num in numeros]  # Converte cada linha para um inteiro

# Lendo os números dos arquivos
numeros_arq1 = ler_numeros(caminho_arq1)
numeros_arq2 = ler_numeros(caminho_arq2)

# Mesclando e ordenando os números
numeros_totais = numeros_arq1 + numeros_arq2
numeros_ordenados = sorted(numeros_totais)

# Escrevendo os números ordenados no novo arquivo
with open(caminho_arq3, 'w') as f:
    for num in numeros_ordenados:
        f.write(f"{num}\n")  # Escreve cada número em uma nova linha

print(f"Números ordenados foram escritos em '{caminho_arq3}'.")