import requests
import pandas as pd
import os
from dotenv import load_dotenv
from math import ceil

class DadosRepositorios:

    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        load_dotenv()
        self.access_token = os.getenv("GITHUB_TOKEN")
        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def lista_repositorios(self):
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
        return [repo.get('name') for repo in repos_list]

    def nomes_linguagens(self, repos_list):
        return [repo.get('language') for repo in repos_list]

    def cria_df_linguagens(self):
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
