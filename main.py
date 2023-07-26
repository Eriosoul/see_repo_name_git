from template.scrap_git import RepositoryGit

if __name__ == '__main__':
    rep: RepositoryGit = RepositoryGit()
    rep.get_status()
    repository_names = rep.get_repository()
    repository_info = rep.get_repository()
    for name, language in repository_info:
        print("Nombre del repositorio:", name)
        print("Lenguaje:", language)

    language_dict = rep.create_language_dict(repository_info)

    # Imprimir el diccionario de lenguajes y repositorios
    print("\nDiccionario de lenguajes y repositorios:")
    for language, info in language_dict.items():
        print(f"Lenguaje: {language}")
        print("Cantidad de repositorios:", info["count"])
        print("Nombres de repositorios:")
        for name in info["repositories"]:
            print(f"  - {name}")

