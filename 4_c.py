# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:33:52 2024

@author: carlo
"""

import os

# Definir o caminho do arquivo que deseja verificar
arquivo = "C:/Users/carlo/OneDrive/Documentos/moçaRh/Curriculo_Carlos_Ferreira_ok.pdf"

# Verificar se o caminho é um arquivo
if os.path.isfile(arquivo):
    print(f"O caminho '{arquivo}' é um arquivo.")
else:
    print(f"O caminho '{arquivo}' não é um arquivo.")