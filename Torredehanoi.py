import time

def hanoi(n, origem, destino, auxiliar, movimentos):
    if n == 1:
        movimentos.append((origem, destino))
    else:
        hanoi(n - 1, origem, auxiliar, destino, movimentos)
        movimentos.append((origem, destino))
        hanoi(n - 1, auxiliar, destino, origem, movimentos)

def executar_testes(numero_discos, repeticoes=10):
    tempos_execucao = []

    for i in range(repeticoes):
        movimentos = []
        inicio = time.time()
        hanoi(numero_discos, 'A', 'C', 'B', movimentos)
        fim = time.time()
        duracao = fim - inicio
        tempos_execucao.append(duracao)
        print(f"Execução {i+1}: {duracao:.6f} segundos | Movimentos: {len(movimentos)}")

    return tempos_execucao

def gerar_relatorio(tempos_execucao):
    media = sum(tempos_execucao) / len(tempos_execucao)
    maximo = max(tempos_execucao)
    minimo = min(tempos_execucao)

    print("\nRelatório de Execução")
    print("---------------------")
    for i, tempo in enumerate(tempos_execucao, 1):
        print(f"Execução {i}: {tempo:.6f} segundos")

    print(f"\nTempo médio: {media:.6f} segundos")
    print(f"Tempo máximo: {maximo:.6f} segundos")
    print(f"Tempo mínimo: {minimo:.6f} segundos")


numero_discos = 10  
tempos = executar_testes(numero_discos)
gerar_relatorio(tempos)

