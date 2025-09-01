# Python e APIs: conhecendo a biblioteca Requests

Este projeto foi desenvolvido para o curso "Python e APIs: conhecendo a biblioteca Requests" da Alura, com o objetivo de estudar e praticar o uso da biblioteca Requests para consumir APIs públicas, em especial a API do GitHub, como parte do "Primeiros passos em Engenharia de Dados". 

## Descrição

O projeto realiza a coleta, análise e exportação de dados sobre os repositórios públicos de grandes empresas de tecnologia (Amazon, Netflix, Spotify e Apple) utilizando a API do GitHub. Os dados extraídos incluem o nome dos repositórios e suas linguagens de programação principais, permitindo identificar as linguagens mais utilizadas por cada empresa.

## Estrutura do Projeto

- `linguagens-repo.ipynb`: Notebook Jupyter com exemplos práticos, explicações e visualização dos dados extraídos.
- `script/data-repo-etl.py`: Script Python que automatiza a coleta e exportação dos dados em arquivos CSV.
- `data/`: Pasta onde são salvos os arquivos CSV gerados com os resultados das consultas.

## Como executar

1. **Instale as dependências:**
   - `requests`
   - `pandas`
   - `python-dotenv`

2. **Configure o token de acesso do GitHub:**
   - Crie um arquivo `.env` na raiz do projeto com o conteúdo:
     ```
     GITHUB_TOKEN=seu_token_aqui
     ```
   - O token é necessário para autenticação nas requisições à API do GitHub.

3. **Execute o notebook ou o script:**
   - O notebook pode ser executado célula a célula para fins de estudo e visualização.
   - O script `data-repo-etl.py` pode ser executado para gerar os arquivos CSV automaticamente.

## Resultados

Os arquivos CSV gerados trazem os nomes dos repositórios e as linguagens de programação principais utilizadas por cada empresa analisada. Estes dados podem ser utilizados para visualizações, análises estatísticas ou estudos sobre tendências tecnológicas.

## Créditos

Este projeto é parte do curso da Alura e foi desenvolvido para fins de estudo e prática de consumo de APIs com Python.
