# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:37:13 2024

@author: carlo

programa dividi a lista em 4 partes e utilizará 4 processos para realizar a pesquisa.
"""

import time
import multiprocessing

def pesquisar_parte(lista, elem, inicio, fim, resultado):
    achou = False
    for i in range(inicio, fim):
        if lista[i] == elem:
            achou = True
            break
    resultado.put(achou)

def main():
    N = 100_000_000  # Tamanho da lista 
    lista = list(range(N))
    elemento = lista[-1]  # Elemento a ser pesquisado

    processos = []
    resultado = multiprocessing.Queue()
    tamanho_parte = N // 4

    inicio = time.time()

    # Criar 4 processos
    for i in range(4):
        inicio_parte = i * tamanho_parte
        fim_parte = (i + 1) * tamanho_parte if i < 3 else N
        processo = multiprocessing.Process(target=pesquisar_parte, args=(lista, elemento, inicio_parte, fim_parte, resultado))
        processos.append(processo)
        processo.start()

    # Aguardar a conclusão dos processos
    for processo in processos:
        processo.join()

    fim = time.time()
    # Verificar se algum resultado foi True
    encontrado = any(resultado.get() for _ in range(4))
    print(encontrado)
    print(f"Tempo de execução (multiprocessing): {fim - inicio:.4f} segundos")

if __name__ == "__main__":
    main()