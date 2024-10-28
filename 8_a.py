# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:55:01 2024

@author: carlo

programa que pesquisa o elemento na última posição da lista sequencialmente, sem utilizar concorrência.
"""

import time

def pesquisar(lista, elem):
    achou = False
    for i in range(len(lista)):
        if lista[i] == elem:
            achou = True
            break
    print(achou)

def main():
    N = 100_000_000  # Tamanho da lista
    lista = list(range(N))
    elemento = lista[-1]  # Elemento a ser pesquisado

    inicio = time.time()
    pesquisar(lista, elemento)
    fim = time.time()

    print(f"Tempo de execução (sequencial): {fim - inicio:.4f} segundos")

if __name__ == "__main__":
    main()