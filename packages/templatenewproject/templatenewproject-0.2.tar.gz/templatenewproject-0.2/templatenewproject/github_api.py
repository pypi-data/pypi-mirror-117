import requests


def buscar_avatar_usuario(usuario):
    """
    Busca o avatar do usuário
    :param usuario: str contendo o nome do usuário
    :return: str com o link do avator do mesmo usuário
    """

    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar_usuario('JoaoZati'))
