# Quicksort híbrido com inserção

Trabalho de Estruturas de Dados Avançadas.

Implementação da ordenação rápida (quicksort) com pivô aleatório e de uma versão híbrida que troca para a ordenação por inserção quando o pedaço da lista fica pequeno. O objetivo é descobrir a partir de qual tamanho vale a pena fazer essa troca.

## O que tem no projeto

| arquivo | descrição |
|---|---|
| `ordenacao.py` | implementação, medição de tempo e geração do gráfico |
| `RELATORIO.md` | tabela, gráfico e análise dos resultados |
| `grafico.png` | gráfico do tempo em função do corte |

## Como funciona

- **Quicksort puro:** escolhe um pivô aleatório e separa a lista em menores, iguais e maiores que ele. Depois ordena os menores e os maiores do mesmo jeito.
- **Quicksort híbrido:** igual ao puro, mas quando o pedaço tem menos que `corte` elementos, usa a ordenação por inserção.

O teste usa uma lista de 20.000 números aleatórios e mede o tempo com os cortes 1, 5, 10, 16, 20, 32, 50, 100 e 200. Cada caso roda 20 vezes e o resultado é a média.

## Como rodar

Precisa do Python 3 e do `matplotlib`:

```
pip install matplotlib
python ordenacao.py
```

O programa mostra a tabela de tempos no terminal e salva o gráfico em `grafico.png`.

## Resultado

Com corte entre 10 e 32 o híbrido foi cerca de 20% mais rápido que o quicksort puro. O melhor foi corte = 20.
Com cortes grandes (100 e 200) ele fica mais lento, porque a inserção é O(n²) e passa a pesar.

Os detalhes estão no [RELATORIO.md](RELATORIO.md).
