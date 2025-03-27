import os
import sys

def copy_file(arquivoOrigem, arquivoDestinoFork):
    try:
        with open(arquivoOrigem, 'rb') as src, open(arquivoDestinoFork, 'wb') as dest:
            while chunk := src.read(4096):  
                dest.write(chunk)
    except Exception as e:
        print(f"Erro ao copiar arquivo: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} <origem> <destino>", file=sys.stderr)
        sys.exit(1)
    
    arquivoOrigem = sys.argv[1]
    arquivoDestinoFork = sys.argv[2]
    
    pid = os.fork()
    
    if pid == 0:  
        copy_file(arquivoOrigem, arquivoDestinoFork)
        print(f"Arquivo copiado com sucesso: {arquivoOrigem} -> {arquivoDestinoFork}")
        sys.exit(0)
    else:  
        os.waitpid(pid, 0) 
if __name__ == "__main__":
    main()
