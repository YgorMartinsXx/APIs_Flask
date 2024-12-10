database = {} #um dicionário, que tem a chave interesses para o controle
#dos interesses (que pessoa se interessa por que outra), e pessoas para o controle de pessoas (quem sao as pessoas e quais sao os dados pessoais de cada pessoa no sistema)
#voce pode controlar as pessoas de outra forma se quiser, nao precisa mudar nada
#do seu código para usar essa váriavel
database['interesses'] = {
    100: [101, 102, 103],
    200: [100,9],
    9 : [200]
}
(database['interesses'])[100]
database['PESSOA'] = [
        {
            "id": 100,
            "nome": "maximus"
        },
        {
            "id": 200,
            "nome": "aurelia"
        },
        {
            "id": 9,
            "nome": "fernando"
        },
    ]


#em todo esse codigo que estou compartilhando, as variaveis interessado, alvo de interesse, pessoa, pessoa1 e pessoa2 sao sempre IDs de pessoas


class NotFoundError(Exception):
    pass


def todas_as_pessoas():
    return database['PESSOA']


def adiciona_pessoa(dic_pessoa):
    pessoa_id = dic_pessoa['id']
    database['interesses'][pessoa_id] = []
    database['PESSOA'].append(dic_pessoa)


def adiciona_interesse(id_interessado, id_alvo_de_interesse):
    localiza_pessoa(id_interessado)
    localiza_pessoa(id_alvo_de_interesse)
    database['interesses'][id_interessado].append(id_alvo_de_interesse)


def consulta_interesses(pessoa_id):
    localiza_pessoa(pessoa_id)
    return database['interesses'][pessoa_id]


def remove_interesse(id_interessado,id_alvo_de_interesse):
    localiza_pessoa(id_interessado)
    localiza_pessoa(id_alvo_de_interesse)
    database['interesses'][id_interessado].remove(id_alvo_de_interesse)


def localiza_pessoa(id_pessoa):
    lista_pessoas = todas_as_pessoas()
    for dic_pessoa in lista_pessoas:
        if dic_pessoa['id'] == id_pessoa:
            return dic_pessoa
    raise NotFoundError


def reseta():
    database["PESSOA"] = []
    database['interesses'] = {}
#Um detalhe: uma consulta por id pode falhar. Talvez a id não exista.
#Nesse caso, espero que você de um raise em um erro NotFoundError, definido
#no arquivo estrutura_interesses.




   


#essa funcao diz se o 1 e o 2 tem match. (retorna True se eles tem, False se não)
#ela não está testada, só existe para fazer aquecimento para a próxima
def verifica_match(id1,id2):
    lista1 = consulta_interesses(id1)
    lista2 = consulta_interesses(id2)
    o1gostaDo2 = id2 in lista1
    o2gostaDo1 = id1 in lista2
    if o1gostaDo2 and o2gostaDo1:
        return True
    else:
        return False
    return o1gostaDo2 and o2gostaDo1
verifica_match(9,200)


def lista_matches(id_pessoa):
    lista1 = consulta_interesses(id_pessoa)
    resposta = []
    for id_outro in lista1:
        if id_pessoa in consulta_interesses(id_outro):
            resposta.append(id_outro)
    return resposta


def pessoa_existe(id_pessoa):
    lista_pessoas = todas_as_pessoas()
    for dic_pessoa in lista_pessoas:
        if dic_pessoa['id'] == id_pessoa:
            return True
    return False
