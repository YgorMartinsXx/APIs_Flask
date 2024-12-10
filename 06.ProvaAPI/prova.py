
import requests

'''
A prova tem 8 testes, cada um valendo 1 ponto,
e mais uma questao livre no final, valendo 2 pontos
'''

'''
A primeira coisa a fazer é ir ao site http://www.omdbapi.com/
e clicar no link API key.

Assim, você terá uma chave de API, uma string que você vai mandar com
todos as suas requisições

Cadastre-se, abra o e-mail e valide sua chave. Depois, você
poderá acessar o OMDb.
'''

'coloque aqui a sua chave de acesso à api'
api_key = 'f656b475'


'''
Antes de fazer qualquer função, vamos experimentar
consultar o OMDb pelo navegador.

Digite, por exemplo, a seguinte URL no Firefox:
    http://www.omdbapi.com/?s=star%20wars&apikey={SUA-CHAVE-VEM-AQUI}

Observe que vemos uma lista de 10 filmes, mas há mais resultados.

Para ver a página 2, acesse
    http://www.omdbapi.com/?s=star%20wars&page=2&apikey={SUA-CHAVE-VEM-AQUI}
'''


'''
Observe que nas URLs acima, estamos passando parâmetros.
Na URL http://www.omdbapi.com/?s=star%20wars&page=2&apikey={SUA-CHAVE-VEM-AQUI}
definimos 3 parâmetros:
 * s=star wars
 * page=2
 * apikey={SUA-CHAVE-VEM-AQUI}
'''

'''
Vou deixar uns exemplos aqui pra vocês
'''

def busca_por_id(film_id):
    url = f"http://www.omdbapi.com/?apikey={api_key}&i={film_id}"
    retorno = requests.get(url).json()
    return retorno

def busca_por_texto(texto_buscar):
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={texto_buscar}"
    retorno = requests.get(url).json()
    return retorno

class FilmeNaoEncontrado (Exception):
    pass

#f656b475
'''
http://www.omdbapi.com/?t=menace&y=2003&apikey={SUA-CHAVE-VEM-AQUI}

A busca acima acha um unico filme, cujo titulo contém "menace",
lançado em 2003. Utilize ela para implementar a função abaixo,
que recebe o nome do filme, o ano, e devolve o diretor do filme. 
Se nao houver resultado, lance uma excessao chamada FilmeNaoEncontrado
'''

def diretor(nome_filme, ano):
    try:
        url = f"http://www.omdbapi.com/?t={nome_filme}&y={ano}&apikey={api_key}" 
        dataGetter = requests.get(url)

        if dataGetter.status_code == 200:
            dici = dataGetter.json()
        else:
            raise FilmeNaoEncontrado
        diretor_filme = dici["Director"]
        return diretor_filme 
        
    except :
        raise FilmeNaoEncontrado

'''
usando a mesma URL, crie uma funcao que retorne a quantidade de ratings de um filme]
ratings são os tipos de avaliação diferentes, veja no firefox se quiser entender melhor

Novamente lance FilmeNaoEncontrado, se for o caso
'''
#f656b475

def quantos_ratings(nome_filme, ano):
    try:
        url = f"http://www.omdbapi.com/?t={nome_filme}&y={ano}&apikey={api_key}" 
        dataGetter = requests.get(url)

        if dataGetter.status_code == 200:
            dici = dataGetter.json()
        else:
            raise FilmeNaoEncontrado
        ratings = dici["Ratings"]
        quantidade_rate = len(ratings)
        return quantidade_rate  
    except :
        raise FilmeNaoEncontrado


'''
https://pokeapi.co/api/v2/pokemon/39/

Usando a URL acima como referencia, crie uma funcao que recebe
o nome de um pokemon, e retorna a sua altura (height)

(nao se preocupe com maiusculas e minusculas)

Se o pokemon nao existir, lance a excessao PokemonNaoEncontrado
'''
#f656b475
class PokemonNaoEncontrado(Exception):
    pass

def altura_pokemon(nome_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}/"
    dataGetter = requests.get(url)

    if dataGetter.status_code==200:
        dici = dataGetter.json()
    else:
        raise PokemonNaoEncontrado
    
    altura = dici["height"]

    return altura

'''na mesma URL da pokeapi, olhando em stats,
temos os dados de todas as estatisticas do pokemon

Por exemplo, o HP do diglett aparece na posicao 0 como 10
verifique a imagem
https://drive.google.com/file/d/1RmHRtg6NGLnvpqPxdg8nE2PTMckMUOGd/view?usp=drive_link

crie uma funcao habilidade, que recebe: o nome do pokemon e o nome da habilidade
devolve: o valor da habilidade, se o pokemon tiver
lanca a excessao: HabilidadeNaoEncontrada se o pokemon nao tiver a habilidade
'''
#f656b475

class HabilidadeNaoEncontrada(Exception):
    pass

def habilidade(nome_pokemon,nome_stat):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}/"
    dataGetter = requests.get(url)
    
    if dataGetter.status_code==200:
        dici = dataGetter.json()
    else:
        raise PokemonNaoEncontrado
    
    count = 0

    for number in range(0, len(dici["stats"])):
        if dici["stats"][number]["stat"]["name"] == nome_stat:
            return dici["stats"][number]["base_stat"]
        else:
            count +=1
    if count == len(dici["stats"]):
        raise HabilidadeNaoEncontrada


'''
A ultima questao da prova é livre:
entre em https://github.com/public-apis/public-apis
e veja uma grande lista de APIs

Escolha uma API qualquer, que não seja de pokemons nem de filmes, e crie uma funcao consulta que de alguma forma consulta essa API.
Requisitos:
* A funcao recebe e usa parametros como o 'nome'
(não faça uma função que sempre retorna os dados do mesmo pokemon, ou do mesmo filme. Se a funcionalidade que voce pensou nao utiliza parametros, por favor, escolha outra funcionalidade)
* A funcao lanca uma excessao quando o pedido foi invalido, consultando a resposta HTTP para isso (nao vale, por exemplo, saber qual o maior numero de pokemon e fazer um if
que nao usa a API)
(nas minhas explicacoes, usei o pokemon, mas a sua consulta nao deve usar o pokemon nem os filmes)


A funcao tem que chamar 'consulta', caso contrario, vai passar batido na hora de corrigir,
você não vai ter os ultimos dois pontos, e vai ter que falar comigo na vista de prova
'''
class BaguioNaoEncontrado(Exception):
    pass

def consulta(id):
    url = f"https://api.thecatapi.com/v1/images/{id}"
    dataGetter = requests.get(url)

    if dataGetter.status_code == 200:
        dici = dataGetter.json()
    else:
        raise BaguioNaoEncontrado
    return dici["width"]

#f656b475

if __name__ == "__main__":
    print("para testar a sua prova, rode o arquivo runtests_prova")