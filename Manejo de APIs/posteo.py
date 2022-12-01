import requests
import json

#Nombre: Fermín Isaí Estrada Vera
#Matrícula: 2006470

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    argumentos = {'nombre':'Fermín', 'matricula':'2006470', 'curso':'Programación para Ciberseguridad'}

    response = requests.post(url, params=argumentos)

    if response.status_code == 200:
        print(response.content)