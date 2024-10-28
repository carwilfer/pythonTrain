# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:21:34 2024

@author: carlo
"""

import psutil

# Obtendo informações sobre o disco
disco = psutil.disk_usage('/')

# Convertendo bytes para gigabytes (GB)
total_disco_gb = disco.total / (1024 ** 3)
espaco_utilizado_gb = disco.used / (1024 ** 3)
espaco_livre_gb = disco.free / (1024 ** 3)
percentual_uso_disco = disco.percent

# Exibindo as informações
print(f"Total de espaço em disco: {total_disco_gb:.2f} GB")
print(f"Espaço utilizado: {espaco_utilizado_gb:.2f} GB")
print(f"Espaço livre: {espaco_livre_gb:.2f} GB")
print(f"Percentual de uso do disco: {percentual_uso_disco}%")