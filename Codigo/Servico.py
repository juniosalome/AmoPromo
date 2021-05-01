import requests
import json


'''
http://stub.2xt.com.br/air/search/:apikey:/:departure_airport:/:arrival_airport:/:departure_date:
http://stub.2xt.com.br/air/search/rE7JIG4MimQREUtWY5h5Ez9gRdPchrul/POA/MAO/2019-12-01

http://stub.2xt.com.br/air/airports/pCuxInwy3vYOvlDrqdEl9vN6mLgmOzte

username: junio
api key: pCuxInwy3vYOvlDrqdEl9vN6mLgmOzte
senha: szqxIn


'''
'''
Acessa o repositorio
'''
class ListaDeRepositorios():
    
    def __init__(self, caminho,tipo ,metodo,username,apikey,pwd):
        self._caminho = caminho
        self._tipo = tipo
        self._metodo = metodo
        self._username = username
        self._pwd = pwd
        self._apikey = apikey

    def requisicao_api(self):

        resposta = requests.get(f'{self._caminho}/{self._tipo}/{self._metodo}/{self._apikey}',
         auth=(self._username,self._pwd))

        
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code

    def imprime_repositorios(self):
        dados_api = self.requisicao_api()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                print(dados_api[i]['name'])
        else:
            print(dados_api)


repositorios = ListaDeRepositorios('http://stub.2xt.com.br','air','airports','junio','pCuxInwy3vYOvlDrqdEl9vN6mLgmOzte','szqxIn')
repositorios.imprime_repositorios()
