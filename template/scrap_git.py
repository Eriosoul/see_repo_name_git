import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup


load_dotenv()


class RepositoryGit:
    def __init__(self):
        self.url = os.getenv('REPOSITROY_EXERCICE')

    def get_status(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                print("Status:", response.status_code)
                return response
            else:
                print("Status:", response.status_code)
                return None
        except Exception as e:
            print("Error", e)

    def get_repository(self):
        response = self.get_status()
        if response is not None:
            try:
                soup = BeautifulSoup(response.text, 'html.parser')
                div_content = soup.find('div', id="user-repositories-list")
                repository_names = []  # Crear una lista vacía para guardar los nombres de los repositorios
                repository_languages = []  # Crear una lista vacía para guardar los nombres de los lenguajes

                for tag_a in div_content.find_all('a', itemprop=True):
                    name = tag_a.text.strip()
                    repository_names.append(name)  # Agregar el nombre del repositorio a la lista

                for tag_b in div_content.find_all('span', class_='ml-0 mr-3'):
                    language = tag_b.text.strip()
                    repository_languages.append(language)  # Agregar el nombre del lenguaje a la lista

                # Combinar ambas listas en una sola
                repository_info = list(zip(repository_names, repository_languages))
                return repository_info
            except Exception as e:
                print("Error", e)
                return []

    def create_language_dict(self, repository_info):
        language_dict = {}
        for name, language in repository_info:
            if language not in language_dict:
                language_dict[language] = {"count": 1, "repositories": [name]}
            else:
                language_dict[language]["count"] += 1
                language_dict[language]["repositories"].append(name)
        return language_dict
