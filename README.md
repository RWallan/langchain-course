# Curso de Langchain

Este é um repositório de estudo do curso [LangChain e LangGraph: Crie Agentes de IA com LLMs e RAGs](https://www.udemy.com/course/lanchain/).

## Requisitos

* Python 3.13
* [Poetry](https://python-poetry.org/)
* [Jupyter Notebook](https://github.com/jupyter/notebook)

## Para desenvolvimento

Clone o repositório:

```bash
git clone https://github.com/RWallan/langchain-course.git; cd langchain-course
```

E instale as dependências:

```bash
poetry install
```

Dessa forma, você terá acesso aos notebooks com o [Jupyter Notebook](https://github.com/jupyter/notebook).

```bash
poetry run jupyter notebook
```

> [!NOTE]
> Esse repositório conta com dois serviços que precisam de API keys, a [OpenAI](https://openai.com/index/openai-api/) e [Pinecone](https://www.pinecone.io/). Portanto, copie o arquivo `.env.example` para `.env` e preencha as suas keys.

## Licença

Esse repositório está sob a licença AFL.
