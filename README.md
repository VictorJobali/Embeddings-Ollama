# Geração de Embeddings com Ollama e Python

## 1. Descrição do projeto

Este projeto tem como objetivo gerar embeddings de textos utilizando o Ollama localmente e a linguagem Python.

Neste projeto, é utilizado o modelo `nomic-embed-text`, específico para a geração de embeddings.

## 2. Tecnologias utilizadas

- **Python:** linguagem utilizada para desenvolver o script.
- **Ollama:** ferramenta utilizada para executar modelos de inteligência artificial localmente.
- **nomic-embed-text:** modelo utilizado para gerar os vetores de embeddings.
- **Biblioteca ollama:** biblioteca Python utilizada para se comunicar com o Ollama.

## 3. Requisitos

Antes de executar o projeto, é necessário ter instalado:

- Python 3.10 ou superior.
- Ollama instalado no computador.
- Biblioteca Python `ollama`.
- Modelo `nomic-embed-text` baixado no Ollama.

## 4. Instalação e configuração do ambiente

### 4.1. Instalar o Ollama

Faça o download e a instalação do Ollama pelo site oficial:

https://ollama.com/download

Após a instalação, abra o terminal e verifique se o Ollama está disponível:

```bash
ollama --version
```

### 4.2. Baixar o modelo de embeddings

Execute o seguinte comando no terminal:

```bash
ollama pull nomic-embed-text
```

Para verificar se o modelo foi instalado corretamente, utilize:

```bash
ollama list
```

O modelo `nomic-embed-text` deverá aparecer na lista.

### 4.3. Instalar a biblioteca Python

Na pasta do projeto, execute:

```bash
pip install ollama
```

## 5. Execução do projeto

### 5.1. Verificar se o Ollama está ativo

No Windows, o Ollama pode ser iniciado automaticamente após a instalação.

Caso o serviço não esteja ativo, abra um terminal e execute:

```bash
ollama serve
```

Mantenha o serviço em execução. Se ele já estiver ativo, não é necessário iniciá-lo novamente.

### 5.2. Executar o script Python

Na pasta em que está localizado o arquivo `embeddings.py`, execute:

```bash
python embeddings.py
```

O script enviará um texto ao modelo `nomic-embed-text`, receberá o vetor de embeddings e exibirá:

- O texto original.
- O modelo utilizado.
- A quantidade de dimensões do vetor.
- Os dez primeiros valores do vetor gerado.

## 6. Exemplo de saída

A execução apresenta um resultado semelhante ao seguinte:

```text
Texto original: A inteligência artificial está transformando a tecnologia.
Modelo utilizado: nomic-embed-text
Quantidade de dimensões: 768
Primeiros 10 valores do vetor: [0.022089029, 0.06341643, -0.14366959, ...]
```

Os valores apresentados são um exemplo de saída. Os valores reais são gerados durante a execução do script.

## 7. Funcionamento do código

O script utiliza a biblioteca `ollama` para enviar um texto ao modelo de embeddings.

A função `ollama.embed()` processa o texto e retorna uma representação numérica. Em seguida, o programa acessa o vetor retornado, calcula sua quantidade de dimensões com `len()` e exibe os dez primeiros valores utilizando `vetor[:10]`.

O modelo `nomic-embed-text` gera um vetor de 768 dimensões para a entrada utilizada neste projeto.
