# Emulador do Comando `cp` em Python

Este projeto é um script em Python que emula o comando `cp` do Shell, utilizando `fork()`. O código realiza a cópia de um arquivo chamado `arquivo.txt` para um novo arquivo.

## Como Funciona
O script cria um processo filho usando `fork()`, que é responsável por realizar a cópia do conteúdo de `arquivo.txt` para outro arquivo especificado.

## Pré-requisitos
- Python 3
- Um sistema operacional baseado em Unix/Linux (necessário para `fork()` funcionar corretamente)

## Como Usar
1. Certifique-se de ter um arquivo chamado `arquivo.txt` na mesma pasta do script.
2. Adicione algum texto ao `arquivo.txt`.
3. Execute o script com:
   ```bash
   python3 cp_python.py
   ```
4. O script criará uma cópia do arquivo, geralmente com um nome predefinido ou passado como argumento.

## Observação
- O código usa `fork()`, que pode não ser compatível com Windows.
- Certifique-se de ter permissões adequadas para leitura e escrita nos arquivos.

## Autores
Pablo Oliveira(1134335) - Gabriela Lenz(1134940)

