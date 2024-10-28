# Projetos em Python

Este repositório contém vários programas em Python que coletam e exibem informações do sistema, além de implementar funcionalidades diversas, como comunicação cliente-servidor e manipulação de arquivos.

## Programas

### 1. Informações do Sistema

Um programa que obtém e exibe as seguintes informações:
- Nome do sistema operacional.
- Nome do usuário.
- Disco padrão.
- Diretório do usuário.
- PID do processo atual.

### 2. Informações de Hardware

Um programa que obtém e exibe as seguintes informações:
- Número de núcleos físicos.
- Número de núcleos lógicos.
- Frequência do processador.
- Total de memória principal em GB.
- Memória utilizada em GB.
- Memória disponível em GB.
- Percentual de memória utilizada.
- Total de espaço em disco do sistema.
- Espaço utilizado em disco.
- Espaço livre em disco.
- Percentual de uso do disco.

### 3. Execução de Processos

Um programa que cria um processo para executar a calculadora do sistema operacional e exibe o PID do processo criado.

### 4. Verificações de Diretório e Arquivo

Um programa que verifica:
- Se um determinado diretório existe.
- Se um determinado diretório é realmente um diretório.
- Se um determinado arquivo é realmente um arquivo.

### 5. Armazenamento de Informações em Arquivo

Um programa que armazena as informações de hardware em um arquivo texto no mesmo diretório do programa Python.

### 6. Manipulação de Arquivos

Um programa que lê dois arquivos de texto (`arq1.txt` e `arq2.txt`), contendo uma sequência de números desordenados. O programa cria um novo arquivo (`arq3.txt`) com os números ordenados.

### 7. Aplicação Cliente-Servidor

Uma aplicação cliente-servidor utilizando sockets TCP. O cliente apresenta um menu de opções que permite ao usuário solicitar informações sobre:
- Memória principal.
- Processador.
- Disco.
- Processos.

O servidor executa as funções correspondentes e retorna os resultados ao cliente.

#### Menu de opções:
[1] - Exibir informações sobre a memória principal [2] - Exibir informações sobre o processador [3] - Exibir informações sobre o disco [4] - Exibir informações sobre os processos [0] - Sair

markdown
Copiar código

### 8. Pesquisa em Listas

Três programas diferentes que pesquisam um elemento na última posição de uma lista inicializada com os valores de 0 a N-1.

#### Modos de implementação:
- Sequencialmente (sem concorrência).
- Usando o módulo `threading` com 4 threads.
- Usando o módulo `multiprocessing` com 4 processos.

Para os testes, utilize os tamanhos de lista N: 1.000.000, 10.000.000 e 100.000.000. Capture os tempos de execução e compare os resultados, justificando as diferenças.

## Conclusão

Esses programas demonstram o uso de diferentes bibliotecas e conceitos em Python, como manipulação de arquivos, comunicação de rede e processamento paralelo. Experimente executá-los em sua máquina para entender melhor como funcionam!

