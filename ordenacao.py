import random
import time
import matplotlib.pyplot as plt

TAMANHO = 20000
REPETICOES = 20
CORTES = [1, 5, 10, 16, 20, 32, 50, 100, 200]


def insercao(lista):
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = atual
    return lista


def quicksort(lista):
    if len(lista) <= 1:
        return lista

    pivo = random.choice(lista)
    menores = []
    iguais = []
    maiores = []

    for x in lista:
        if x < pivo:
            menores.append(x)
        elif x == pivo:
            iguais.append(x)
        else:
            maiores.append(x)

    return quicksort(menores) + iguais + quicksort(maiores)


def quicksort_hibrido(lista, corte):
    if len(lista) < corte:
        return insercao(lista)
    if len(lista) <= 1:
        return lista

    pivo = random.choice(lista)
    menores = []
    iguais = []
    maiores = []

    for x in lista:
        if x < pivo:
            menores.append(x)
        elif x == pivo:
            iguais.append(x)
        else:
            maiores.append(x)

    return quicksort_hibrido(menores, corte) + iguais + quicksort_hibrido(maiores, corte)


def medir_puro(lista):
    total = 0
    for _ in range(REPETICOES):
        copia = lista[:]
        inicio = time.perf_counter()
        resultado = quicksort(copia)
        total += time.perf_counter() - inicio
        if resultado != sorted(lista):
            print("ERRO: quicksort puro nao ordenou")
    return total / REPETICOES


def medir_hibrido(lista, corte):
    total = 0
    for _ in range(REPETICOES):
        copia = lista[:]
        inicio = time.perf_counter()
        resultado = quicksort_hibrido(copia, corte)
        total += time.perf_counter() - inicio
        if resultado != sorted(lista):
            print("ERRO: hibrido nao ordenou com corte", corte)
    return total / REPETICOES


def main():
    lista = [random.randint(0, 1000000) for _ in range(TAMANHO)]

    tempo_puro = medir_puro(lista)

    resultados = []
    for corte in CORTES:
        tempo = medir_hibrido(lista, corte)
        resultados.append((corte, tempo))

    print(f"Quicksort puro: {tempo_puro * 1000:.2f} ms")
    print()
    print("| corte | tempo (ms) | ganho sobre a pura |")
    print("|------:|-----------:|-------------------:|")
    for corte, tempo in resultados:
        ganho = (tempo_puro - tempo) / tempo_puro * 100
        print(f"| {corte} | {tempo * 1000:.2f} | {ganho:+.1f}% |")

    cortes = [c for c, _ in resultados]
    tempos = [t * 1000 for _, t in resultados]

    plt.plot(cortes, tempos, marker="o", label="Quicksort híbrido")
    plt.axhline(tempo_puro * 1000, color="red", linestyle="--", label="Quicksort puro")
    plt.xlabel("Corte (elementos)")
    plt.ylabel("Tempo (ms)")
    plt.title("Tempo em função do corte (20.000 elementos)")
    plt.legend()
    plt.grid(True)
    plt.savefig("grafico.png")

    melhor_corte, melhor_tempo = min(resultados, key=lambda r: r[1])
    ganho = (tempo_puro - melhor_tempo) / tempo_puro * 100
    print()
    print(f"Melhor corte: {melhor_corte} ({melhor_tempo * 1000:.2f} ms, {ganho:.1f}% mais rapido que a pura)")


main()
