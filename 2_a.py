# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:59:06 2024

@author: carlo
# Obtendo o número de núcleos físicos
# Obtendo o número de núcleos lógicos
# Exibindo as informações
"""

import psutil

nucleos_fisicos = psutil.cpu_count(logical=False)

nucleos_logicos = psutil.cpu_count(logical=True)

frequencia = psutil.cpu_freq()

print(f"Número de núcleos físicos: {nucleos_fisicos}")
print(f"Número de núcleos lógicos: {nucleos_logicos}")
print(f"Frequência máxima do processador: {frequencia.max} MHz")
print(f"Frequência atual do processador: {frequencia.current} MHz")