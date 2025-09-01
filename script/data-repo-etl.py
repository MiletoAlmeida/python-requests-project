"""
Módulo para coleta e análise das linguagens de programação utilizadas em repositórios públicos de grandes empresas via API do GitHub.

Classes:
    DadosRepositorios: Realiza requisições à API do GitHub, extrai dados dos repositórios e organiza em DataFrame.

Uso:
    Instancie DadosRepositorios com o nome do usuário/empresa desejado e utilize o método cria_df_linguagens para obter um DataFrame com os nomes dos repositórios e suas linguagens principais.
"""
import requests
import pandas as pd
import os
from dotenv import load_dotenv
from math import ceil

class DadosRepositorios:
    """
    Classe para coletar dados de repositórios públicos de um usuário/empresa no GitHub.

    Métodos principais:
        lista_repositorios(): Retorna lista de repositórios públicos do usuário.
        nomes_repos(repos_list): Extrai nomes dos repositórios de uma lista.
        nomes_linguagens(repos_list): Extrai linguagens dos repositórios de uma lista.
        cria_df_linguagens(): Retorna DataFrame com nomes e linguagens dos repositórios.
    """

    def __init__(self, owner):
        """
        Inicializa a instância com o nome do usuário/empresa alvo.
        Carrega o token de acesso do GitHub a partir do arquivo .env.
        """
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        load_dotenv()
        self.access_token = os.getenv("GITHUB_TOKEN")
        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def lista_repositorios(self):
        """
        Retorna uma lista de todos os repositórios públicos do usuário/empresa.
        Utiliza paginação para garantir que todos os repositórios sejam coletados.
        """
        repos_list = []

        url_user = f'{self.api_base_url}/users/{self.owner}'
        response = requests.get(url_user, headers=self.headers)
        total_repos = response.json().get('public_repos', 0)

        per_page = 100
        num_pages = ceil(total_repos / per_page)

        for page_num in range(1, num_pages + 1):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?per_page={per_page}&page={page_num}'
                response = requests.get(url, headers=self.headers)
                response.raise_for_status()
                repos_list.extend(response.json()) 
            except Exception as e:
                print(f"Erro na página {page_num}: {e}")

        return repos_list 

    def nomes_repos(self, repos_list):
        """
        Extrai os nomes dos repositórios de uma lista de repositórios.
        Args:
            repos_list (list): Lista de dicionários de repositórios.
        Returns:
            list: Lista de nomes dos repositórios.
        """
        return [repo.get('name') for repo in repos_list]

    def nomes_linguagens(self, repos_list):
        """
        Extrai as linguagens principais dos repositórios de uma lista de repositórios.
        Args:
            repos_list (list): Lista de dicionários de repositórios.
        Returns:
            list: Lista de linguagens dos repositórios.
        """
        return [repo.get('language') for repo in repos_list]

    def cria_df_linguagens(self):
        """
        Cria um DataFrame pandas com os nomes dos repositórios e suas linguagens principais.
        Returns:
            pd.DataFrame: DataFrame com colunas 'repository_name' e 'language'.
        """
        repositorios = self.lista_repositorios()
        nomes = self.nomes_repos(repositorios)
        linguagens = self.nomes_linguagens(repositorios)

        dados = pd.DataFrame({
            'repository_name': nomes,
            'language': linguagens
        })

        return dados


amazon_rep = DadosRepositorios('amzn')
most_used_languages_amzn = amazon_rep.cria_df_linguagens()
#print(most_used_languages_amzn)

netflix_rep = DadosRepositorios('netflix')
most_used_languages_netflix = netflix_rep.cria_df_linguagens()
#print(most_used_languages_netflix)

spotify_rep = DadosRepositorios('spotify')
most_used_languages_spotify = spotify_rep.cria_df_linguagens()
#print(most_used_languages_spotify)

apple_rep = DadosRepositorios('apple')
most_used_languages_apple = apple_rep.cria_df_linguagens()
#print(most_used_languages_apple)

# Salvando os dados

most_used_languages_amzn.to_csv('data/most_used_languages_amzn.csv')
most_used_languages_netflix.to_csv('data/most_used_languages_netflix.csv')
most_used_languages_spotify.to_csv('data/most_used_languages_spotify.csv')
most_used_languages_apple.to_csv('data/most_used_languages_apple.csv')
