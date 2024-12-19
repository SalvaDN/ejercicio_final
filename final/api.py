import requests
import random


def api_preguntas():
    url = "https://opentdb.com/api.php?amount=15&difficulty=medium&type=multiple"
    respuesta_api = requests.get(url)
    respuestas_ok = respuesta_api.json()
    lista_preguntas = respuestas_ok['results']

    random.shuffle(lista_preguntas)
    return lista_preguntas
