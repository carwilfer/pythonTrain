# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:29:42 2024

@author: carlo

programa dividi a lista em 4 partes e utilizará 4 threads para realizar a pesquisa.
"""

import time
import threading

def pesquisar_parte(lista, elem, inicio, fim, resultado):
    achou = False
    for i in range(inicio, fim):
        if lista[i] == elem:
            achou = True
            break
    resultado.append(achou)

def main():
    N = 100_000_000  # Tamanho da lista
    lista = list(range(N))
    elemento = lista[-1]  # Elemento a ser pesquisado

    threads = []
    resultado = []
    tamanho_parte = N // 4

    inicio = time.time()

    # Criar 4 threads
    for i in range(4):
        inicio_parte = i * tamanho_parte
        fim_parte = (i + 1) * tamanho_parte if i < 3 else N
        thread = threading.Thread(target=pesquisar_parte, args=(lista, elemento, inicio_parte, fim_parte, resultado))
        threads.append(thread)
        thread.start()

    # Aguardar a conclusão das threads
    for thread in threads:
        thread.join()

    fim = time.time()
    # Verificar se algum resultado foi True
    encontrado = any(resultado)
    print(encontrado)
    print(f"Tempo de execução (threading): {fim - inicio:.4f} segundos")

if __name__ == "__main__":
    main()