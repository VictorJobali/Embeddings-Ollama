import ollama

texto = input("Digite um texto em português ou inglês: ")

resposta = ollama.embed(
    model="nomic-embed-text",
    input=texto
)

vetor = resposta["embeddings"][0]

print("Texto original:", texto)
print("Modelo utilizado: nomic-embed-text")
print("Quantidade de dimensões:", len(vetor))
print("Primeiros 10 valores do vetor:", vetor[:10])
