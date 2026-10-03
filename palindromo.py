import unicodedata


def normalizar(texto):
    """Remove acentos, espaços e pontuação, e converte para minúsculas."""
    sem_acentos = unicodedata.normalize("NFD", texto)
    sem_acentos = "".join(c for c in sem_acentos if unicodedata.category(c) != "Mn")
    return "".join(c.lower() for c in sem_acentos if c.isalnum())


def eh_palindromo(palavra):
    """Retorna True se a palavra for um palíndromo."""
    texto = normalizar(palavra)
    return texto == texto[::-1]


if __name__ == "__main__":
    palavra = input("Digite uma palavra: ")
    if eh_palindromo(palavra):
        print(f'"{palavra}" é um palíndromo.')
    else:
        print(f'"{palavra}" não é um palíndromo.')
