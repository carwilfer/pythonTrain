# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:24:38 2024

@author: carlo
"""

import subprocess

# Criando um processo para executar a calculadora
processo = subprocess.Popen('calc.exe')

# Exibindo o PID do processo criado
print(f"PID do processo da calculadora: {processo.pid}")