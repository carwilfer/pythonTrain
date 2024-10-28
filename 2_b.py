# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:19:37 2024

@author: carlo
# Obtendo informações sobre a memória
# Convertendo bytes para gigabytes (GB)
# Exibindo as informações
"""

import psutil

memoria = psutil.virtual_memory()

total_memoria_gb = memoria.total / (1024 ** 3)
memoria_utilizada_gb = memoria.used / (1024 ** 3)
memoria_disponivel_gb = memoria.available / (1024 ** 3)
percentual_memoria_utilizada = memoria.percent

print(f"Total de memória: {total_memoria_gb:.2f} GB")
print(f"Memória utilizada: {memoria_utilizada_gb:.2f} GB")
print(f"Memória disponível: {memoria_disponivel_gb:.2f} GB")
print(f"Percentual de memória utilizada: {percentual_memoria_utilizada}%")