#rodar no cmd
#windows:   python -m pip install requests
#linux/mac: python3 -m pip install requests


# instalamos a biblioteca requests, que vai permitir acesso a servidores
# por exemplo vamos poder baixar os dados do viacep
# (se quiser experimentar, abra no firefox: https://viacep.com.br/ws/03685020/json/)


import requests


def bairro(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    # nessa string URL, eu preenchi com a variavel cep
    # repare no f antes das aspas, é isso que me deixou colocar a variavel
    print(url)
    #url = "https://viacep.com.br/ws/"+cep+"/json/" #faz a mesma coisa, mas é mais feio
    r = requests.get(url) #existe tb requests.post, você vai ver isso no exercicio
    # do pokemon
    r.text #é a string que eu baixei, mas eu quero um dicionario
    # a gente nao vai usar r.text pra basicamente nada
    dici = r.json() #pego a string e transformo num dicionario
    return dici['bairro']


print(bairro("05775200"))

