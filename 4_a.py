# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:28:45 2024

@author: carlo
"""

import os

# Definir o caminho do diretório que deseja verificar
diretorio = "C:/Users/carlo/OneDrive/Documentos"

# Verificar se o diretório existe
if os.path.exists(diretorio) and os.path.isdir(diretorio):
    print(f"O diretório '{diretorio}' existe.")
else:
    print(f"O diretório '{diretorio}' não existe.")