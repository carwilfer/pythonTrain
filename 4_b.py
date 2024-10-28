# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:31:20 2024

@author: carlo
"""

import os

# Definir o caminho do diretório que deseja verificar
diretorio = "C:/Users/carlo/OneDrive/Documentos"

# Verificar se o caminho é um diretório
if os.path.isdir(diretorio):
    print(f"O caminho '{diretorio}' é um diretório.")
else:
    print(f"O caminho '{diretorio}' não é um diretório.")