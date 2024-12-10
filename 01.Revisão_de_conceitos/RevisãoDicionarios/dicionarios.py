
'''
Um dicionário é muito semelhante a uma lista.

Tomemos a lista [10,20,30]. As posições dela são 0,1 e 2.
lista[0] vale 10, lista[1] vale 20 e lista[2] vale 30.

A diferença entre dicionários e listas é que um dicionário
pode ter as posições que a gente quiser.

Um dicionário pode ter as posições 3, 9 e 11
(sem ter as posições 0,1,2,4,5,6,7,8, nem 10)

Na verdade, como podemos ver no exemplo a seguir,
um dicionário pode ter as posições "marcos", "fabio" e "maria".

(oficialmente, um dicionário não tem "posições",
mas sim chaves)
'''
agenda_exemplo = {}
agenda_exemplo['marcos']=32112232
agenda_exemplo['fabio']=988887788
agenda_exemplo['maria']=44554455 

'''

Se quiser, experimente no pythontutor

https://pythontutor.com/visualize.html#code=def%20soma%28a,b%29%3A%0A%20%20%20%20resultado%20%3D%20a%2Bb%0A%20%20%20%20print%28100%29%0A%20%20%20%20return%20resultado%0A%20%20%20%20%0Avalor1%20%3D%20soma%2810,20%29%0Avalor2%20%3D%20soma%28valor1,50%29%0Avalor3%20%3D%20soma%2810,20%29%2B90%0Avalor4%20%3D%20soma%28soma%281,2%29,soma%284,5%29%29%0A%0A%23%20argumentos%3A%20a%20e%20b%0A%23%20ao%20chamar%20uma%20funcao,%20soma%2810,20%29,%20estou%20dizendo%3A%20atribua%20o%20a%3D10,atribua%0A%23%20o%20b%3D20,%20e%20rode%20o%20c%C3%B3digo%20da%20funcao%0A%0A%23%20return%0A%23%20ao%20chamar%20valor3%20%3D%20soma%2810,20%29%2B90,%20estou%20dizendo%3A%20execute%20a%20funcao,%0A%23%20coloque%20a%20resposta%20no%20lugar.%20Em%20algum%20sentido,%20depois%20que%20%0A%23%20a%20funcao%20retorna%20*30*,%20o%20c%C3%B3digo%20fica%20valor3%20%3D%20*30*%2B90&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false


(cuidado: copie a linha toda!)
'''

'''
Crie uma função consulta que recebe uma agenda (um dicionário)
e uma pessoa, e retorna o telefone dessa pessoa

Primeiro, você pode querer lembrar funcoes

https://pythontutor.com/visualize.html#code=def%20soma%28a,b%29%3A%0A%20%20%20%20resultado%20%3D%20a%2Bb%0A%20%20%20%20print%28100%29%0A%20%20%20%20return%20resultado%0A%20%20%20%20%0Avalor1%20%3D%20soma%2810,20%29%0Avalor2%20%3D%20soma%28valor1,50%29%0Avalor3%20%3D%20soma%2810,20%29%2B90%0Avalor4%20%3D%20soma%28soma%281,2%29,soma%284,5%29%29%0A%0A%23%20argumentos%3A%20a%20e%20b%0A%23%20ao%20chamar%20uma%20funcao,%20soma%2810,20%29,%20estou%20dizendo%3A%20atribua%20o%20a%3D10,atribua%0A%23%20o%20b%3D20,%20e%20rode%20o%20c%C3%B3digo%20da%20funcao%0A%0A%23%20return%0A%23%20ao%20chamar%20valor3%20%3D%20soma%2810,20%29%2B90,%20estou%20dizendo%3A%20execute%20a%20funcao,%0A%23%20coloque%20a%20resposta%20no%20lugar.%20Em%20algum%20sentido,%20depois%20que%20%0A%23%20a%20funcao%20retorna%20*30*,%20o%20c%C3%B3digo%20fica%20valor3%20%3D%20*30*%2B90&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

Depois, se quiser, pode ver como fica a resposta

https://pythontutor.com/visualize.html#code=agenda_exemplo%20%3D%20%7B%7D%0Aagenda_exemplo%5B'marcos'%5D%3D32112232%0Aagenda_exemplo%5B'fabio'%5D%3D988887788%0Aagenda_exemplo%5B'maria'%5D%3D44554455%20%0A%0A%0A%23acesso%20no%20braco%0Atel_maria%20%3D%20agenda_exemplo%5B'maria'%5D%0Atel_fabio%20%3D%20agenda_exemplo%5B'fabio'%5D%0A%0Adef%20consulta%28agenda,pessoa%29%3A%0A%20%20%20%20%23tel_maria%20%3D%20agenda_exemplo%5B'maria'%5D%0A%20%20%20%20telefone%20%3D%20agenda%5Bpessoa%5D%0A%20%20%20%20return%20telefone%0A%20%20%20%20%0Atel_maria2%20%3D%20consulta%28agenda_exemplo,'maria'%29%0Atel_fabio2%20%3D%20consulta%28agenda_exemplo,'fabio'%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false


'''

def consulta(agenda,pessoa):
    pass


'''
Crie uma função adiciona que recebe uma agenda
(um dicionário)
uma pessoa e um telefone, e adiciona o
telefone dessa pessoa na agenda

Adicionar um item num dicionário é simples
dicionario['chave'] = valor

teste sua funcao no pythontutor (colocando ela no lugar indicado)

https://pythontutor.com/python-debugger.html#code=agenda1%20%3D%20%7B%7D%0Aagenda1%5B'maria'%5D%3D22222%0A%0Aagenda2%20%3D%20%7B%7D%0Aagenda2%5B'fabio'%5D%3D%2033333%0A%0A%0Adef%20adiciona%28agenda,%20pessoa,%20telefone%29%3A%0A%20%20%20%20pass%20%23TODO%3A%20coloque%20aqui%20a%20funcao!%0A%0Aadiciona%28agenda1,%20'marcos',%205555555%29%0Aadiciona%28agenda2,%20'fernando',%20444333%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
'''

def adiciona(agenda,pessoa,telefone):
  return 'adicionei'

'''
Depois que terminar a funcao, e testar no pythontutor, coloque de volta no arquivo e rode ele, 
pra ver se o teste passou
'''

'''
Uma terceira feature que precisamos para a nossa agenda é
a possibilidade de verificar se uma pessoa já está na base de dados.

Simplesmente verificar agenda['pessoa'] não funciona:
se você acessar uma pessoa que não existe,
o python dará um KeyError.

Precisamos, então usar o seguinte: 'chave' in dicionario.keys() 
    isso é um teste que retorna True se a chave
    está no dicionário, e False caso contrário.

Temos, por exemplo, os prints seguintes,
que verificam se algumas pessoas estao na agenda
'''
# print('maria esta na agenda?')
# print('maria' in agenda_exemplo.keys() )

# print('damiao esta na agenda?')
# print('damiao' in agenda_exemplo.keys() )

# pessoa = 'marcos'
# print('a string da variavel pessoa é uma chave da agenda?')
# print(pessoa in agenda_exemplo.keys() )

'''
Crie uma função verifica, que recebe uma agenda
e um nome de pessoa, e verifica se a pessoa
está na agenda (retorna True se
a pessoa está e False caso contrário)

Teste no pythontutor (colocando no lugar indicado) e depois com o runtests

https://pythontutor.com/python-debugger.html#code=agenda1%20%3D%20%7B%7D%0Aagenda1%5B'maria'%5D%3D22222%0Aagenda1%5B'fabio'%5D%3D22222%0A%0A%0Aagenda2%20%3D%20%7B%7D%0Aagenda2%5B'fabio'%5D%3D%2033333%0A%0A%0Adef%20verifica%28agenda,pessoa%29%3A%0A%20%20%20%20pass%20%23TODO%3A%20coloque%20aqui%20a%20funcao!%0A%0Aachei_maria1%20%3D%20verifica%28agenda1,'maria'%29%0Aachei_maria2%20%3D%20verifica%28agenda2,'maria'%29%0Aachei_fabio1%20%3D%20verifica%28agenda1,'fabio'%29%0Aachei_fabio2%20%3D%20verifica%28agenda2,'fabio'%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
'''

def verifica(agenda,pessoa):
    return False


''' 
Para definir um dicionário vazio, fazemos o seguinte:
'''
vazio = {}


'''
Usando seus conhecimentos de dicionário até agora, 
crie uma função conta_letras que recebe uma palavra e retorna
um dicionário com o número de ocorrências de cada letra.

por exemplo, conta_letras('abacaxi') deve
retornar o dicionário {'a':3,'b':1,'c':1,'x':1}

NAO USE nenhuma função mágica do python. Escreva a lógica
usando dicionários.

O seguinte trecho de codigo pode ser util:
>>> palavra='ganancia'
>>> for letra in palavra:
	print('estou olhando para',letra)

		
estou olhando para g
estou olhando para a
estou olhando para n
estou olhando para a
estou olhando para n
estou olhando para c
estou olhando para i
estou olhando para a

verifique, colocando a funcao no local indicado

https://pythontutor.com/python-debugger.html#code=def%20conta_letras%28palavra%29%3A%0A%20%20%20%20pass%20%23coloque%20sua%20funcao%20no%20lugar%20dessa%20conta_letras!%0A%0Aconta_letras%28%22banana%22%29%0Aconta_letras%28%22abacaxi%22%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
'''

def conta_letras(palavra):
    conta={}
    return conta


'''
Agora, vamos usar listas e dicionários para criar uma agenda 
um pouco mais completa. Veja o exemplo
'''

agenda_melhor1 = {
        'lucas': {
            'email': 'pf1561@fiap.com.br',
            'telefones': [11999888999, 1177788899]
            }, #meu email está correto, meus telefones nao :P
        'maria' : {
            'email':'maria.aparecida@exemplo.com',
            'telefones':[84999777444]
            },
        'marta': {
            'telefones':[1177788899]     
            }
        }


'''
Crie uma função email, que recebe uma agenda (dessas melhoradas)
e uma pessoa.

Ela retorna o email da pessoa. 

Não precisa se preocupar com
o caso do registro da pessoa nao ter email (faremos isso
mais pra frente)

talvez o seguinte pythontutor seja util
https://pythontutor.com/visualize.html#code=agenda_melhor1%20%3D%20%7B%0A%20%20%20%20%20%20%20%20'lucas'%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20'email'%3A%20'lucas.goncalves%40faculdadeimpacta.com.br',%0A%20%20%20%20%20%20%20%20%20%20%20%20'telefones'%3A%20%5B11999888999,%201177788899%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D,%20%23meu%20email%20est%C3%A1%20correto,%20meus%20telefones%20nao%20%3AP%0A%20%20%20%20%20%20%20%20'maria'%20%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20'email'%3A'maria.aparecida%40exemplo.com',%0A%20%20%20%20%20%20%20%20%20%20%20%20'telefones'%3A%5B84999777444%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D,%0A%20%20%20%20%20%20%20%20'marta'%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20'telefones'%3A%5B1177788899%5D%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%0Aagenda_lucas%20%3D%20agenda_melhor1%5B'lucas'%5D&cumulative=false&heapPrimitives=false&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

'''

def email(agenda,pessoa):
    return 'maria@exemplo.com'

'''
Crie uma função telefone_principal, que recebe uma agenda 
(nessa versão mais nova) e uma pessoa.

Ela retorna o primeiro telefone da lista de telefones da 
pessoa
'''
def telefone_principal(agenda,pessoa):
    return 1122233322

'''
Se você quiser verificar todas as chaves de um dicionário,
pode fazer como a seguir
>>> for chave in agenda_melhor1.keys():
	print(chave)
lucas
maria
marta

Lembrando de qual a cara da agenda_melhor1:

{'marta': {'telefones': [1177788899]},
 'lucas': {'email': 'lucas.goncalves@faculdadeimpacta.com.br',
                       'telefones': [11999888999, 1177788899]},
 'maria': {'email': 'maria.aparecida@exemplo.com', 'telefones': [84999777444]}}

(ela realmente só tem essas 3 chaves)
'''
'''
Crie uma função sem_email, que recebe uma agenda (nessa versão
mais nova) e retorna uma lista de todos os contatos sem email.

Por exemplo, sem_email(agenda_melhor1) deve retornar uma
lista com um único contato: ['marta']
'''

def sem_email(agenda):
    return ['pessoa1','pessoa2']


'''
Crie uma função conta telefones, que recebe uma agenda (nessa versão
mais nova) e retorna a quantidade de números de telefone registrados.

Se houver telefones repetidos (o exemplo agenda_melhor1 tem!), 
conte as repetições (então, para agenda_melhor1 a resposta deve
ser 4, por mais que o mesmo número apareça no item marta
e no item lucas
'''

def conta_telefones(agenda):
    return 12

'''
Por ultimo, vamos criar uma funcao conta_ocorrencias
que dirá quantas vezes um telefone ocorre na agenda.

Ela recebe uma agenda melhorada (um dicionário nesse formato
que estamos usando) e devolve um dicionário. As chaves são
os números de telefone, e os valores, as vezes que cada 
número apareceu na agenda
'''

def conta_ocorrencias(agenda):
    return {1122224444:3}


#nao mexa a partir daqui
#pode ler, mas não altere, para não zoar seus testes
import unittest

agenda_testes1 = {
        'joao':22222222,
        'jose':33333333,
        }

#agendas melhoradas
agenda1 = {}
agenda1['a'] = {'telefones':[1122233344]}
agenda1['b'] = {'telefones':[1122233344]}
agenda1['c'] = {'telefones':[1122233344]}
agenda1['d'] = {'telefones':[1122233344]}
agenda1['e'] = {'telefones':[1122233344]}

agenda2 = {}
agenda2['a'] = {'telefones':[11321321321]}
agenda2['e'] = {'telefones':[11321321321]}
agenda2['i'] = {'telefones':[11321321321]}
agenda2['o'] = {'telefones':[11321321321]}
agenda2['u'] = {'telefones':[11321321321]}
agenda2['y'] = {'telefones':[11321321321]}
agenda2['fulano'] = {'email':'fulano@exemplo.com', 'telefones':[1144440000]}

agenda3 = {}
agenda3['marcia'] = {'telefones':[1123232323]}
agenda3['ana'] = {'telefones':[1123232323]}
agenda3['marcos'] = {'telefones':[1123232323]}
agenda3['heitor'] = {'telefones':[1123232323]}
agenda3['fulano'] = {'email':'fulano@exemplo.com','telefones':[11777888999,1122222222]}

agenda_melhor2 = {
        'lucas': {
            'email': 'lucas.goncalves@faculdadeimpacta.com.br',
            'telefones': [11999888999, 1177788899]
            },
        'maria' : {
            'email':'maria.aparecida@exemplo.com',
            'telefones':[84999777444]
            },
        'marta': {
            'telefones':[1177788899]     
            }
        }

class TestPartOne(unittest.TestCase):

    def test_01_consulta(self):
        self.assertEqual(consulta(agenda_testes1,'joao'),22222222)
        self.assertEqual(consulta(agenda_testes1,'jose'),33333333)
    
    def test_02_adiciona(self):
        agenda_testes1 = {
           'joao':2,
           'jose':3,
        }
        adiciona(agenda_testes1,'marcia',55555555)
        self.assertEqual(consulta(agenda_testes1,'marcia'),55555555)
        adiciona(agenda_testes1,'antonio',88888888)
        self.assertEqual(consulta(agenda_testes1,'antonio'),88888888)
    
    def test_03_verifica(self):
        self.assertFalse(verifica(agenda_testes1,'marcia'))
        self.assertFalse(verifica(agenda_testes1,'antonio'))
        self.assertTrue(verifica(agenda_testes1,'joao'))
        self.assertTrue(verifica(agenda_testes1,'jose'))

      
    def test_04_conta_letras(self):
        self.assertEqual(conta_letras('banana'),{'b':1,'n':2,'a':3})
        self.assertEqual(conta_letras(''),{})
        self.assertEqual(conta_letras('a'*5+'b'*3+'c'*10+'a'),{'a':6,'b':3,'c':10})

    def test_05_email(self):
        self.assertEqual(email(agenda_melhor2,'lucas'),'lucas.goncalves@faculdadeimpacta.com.br')
        self.assertEqual(email(agenda_melhor2,'maria'),'maria.aparecida@exemplo.com')
        self.assertEqual(email(agenda2,'fulano'),'fulano@exemplo.com')
        self.assertEqual(email(agenda3,'fulano'),'fulano@exemplo.com')


    def test_06a_telefone_principal(self):
        self.assertEqual(telefone_principal(agenda_melhor2,'lucas'),11999888999)
        self.assertEqual(telefone_principal(agenda_melhor2,'maria'),84999777444)
        self.assertEqual(telefone_principal(agenda_melhor2,'marta'),1177788899)

    # essa divisão foi feita para termos exatamente 10 testes.
    # não há nenhum motivo a mais. Os testes 06a e 06b poderiam
    # perfeitamente ser um só
    def test_06b_telefone_principal(self):
        self.assertEqual(telefone_principal(agenda1,'a'),1122233344)
        self.assertEqual(telefone_principal(agenda2,'a'),11321321321)
        self.assertEqual(telefone_principal(agenda3,'ana'),1123232323)
        self.assertEqual(telefone_principal(agenda3,'fulano'),11777888999)

    def test_07_sem_email(self):
        self.assertEqual(set(sem_email(agenda1)),set('abcde')) #a lista sem_email(agenda1) tem que ter os
        #elementos 'a','b','c','d','e', e mais nenhum
        # um set é um conjunto, ele é caracterizado pelos elementos, mas ignora ordem,
        # por isso usamos para comparar as listas --- pra nós tanto faz a ordem, desde que
        # voce tenha os elementos certos
        self.assertEqual(set(sem_email(agenda2)),set('aeiouy'))
        self.assertEqual(set(sem_email(agenda3)),set(['marcia','ana','marcos','heitor']))

    def test_08_conta_telefones(self):
        self.assertEqual(conta_telefones(agenda1),5)
        self.assertEqual(conta_telefones(agenda2),7)
        self.assertEqual(conta_telefones(agenda3),6)
    
    def test_09_conta_ocorrencias(self):
        self.assertEqual(conta_ocorrencias(agenda1),{1122233344:5})
        self.assertEqual(conta_ocorrencias(agenda2),{11321321321:6, 1144440000:1})
        self.assertEqual(conta_ocorrencias(agenda3),{1123232323:4, 11777888999:1,1122222222:1})

    

        


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPartOne)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

try:
  from dicionarios_gabarito import *
except:
  pass

runTests()

'''
mais pythontutors

listas versus dicionarios

https://pythontutor.com/visualize.html#code=def%20soma%28a,b%29%3A%0A%20%20%20%20resultado%20%3D%20a%2Bb%0A%20%20%20%20print%28100%29%0A%20%20%20%20return%20resultado%0A%20%20%20%20%0Avalor1%20%3D%20soma%2810,20%29%0Avalor2%20%3D%20soma%28valor1,50%29%0Avalor3%20%3D%20soma%2810,20%29%2B90%0Avalor4%20%3D%20soma%28soma%281,2%29,soma%284,5%29%29%0A%0A%23%20argumentos%3A%20a%20e%20b%0A%23%20ao%20chamar%20uma%20funcao,%20soma%2810,20%29,%20estou%20dizendo%3A%20atribua%20o%20a%3D10,atribua%0A%23%20o%20b%3D20,%20e%20rode%20o%20c%C3%B3digo%20da%20funcao%0A%0A%23%20return%0A%23%20ao%20chamar%20valor3%20%3D%20soma%2810,20%29%2B90,%20estou%20dizendo%3A%20execute%20a%20funcao,%0A%23%20coloque%20a%20resposta%20no%20lugar.%20Em%20algum%20sentido,%20depois%20que%20%0A%23%20a%20funcao%20retorna%20*30*,%20o%20c%C3%B3digo%20fica%20valor3%20%3D%20*30*%2B90&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

funcoes

https://pythontutor.com/visualize.html#code=def%20soma%28a,b%29%3A%0A%20%20%20%20resultado%20%3D%20a%2Bb%0A%20%20%20%20print%28100%29%0A%20%20%20%20return%20resultado%0A%20%20%20%20%0Avalor1%20%3D%20soma%2810,20%29%0Avalor2%20%3D%20soma%28valor1,50%29%0Avalor3%20%3D%20soma%2810,20%29%2B90%0Avalor4%20%3D%20soma%28soma%281,2%29,soma%284,5%29%29%0A%0A%23%20argumentos%3A%20a%20e%20b%0A%23%20ao%20chamar%20uma%20funcao,%20soma%2810,20%29,%20estou%20dizendo%3A%20atribua%20o%20a%3D10,atribua%0A%23%20o%20b%3D20,%20e%20rode%20o%20c%C3%B3digo%20da%20funcao%0A%0A%23%20return%0A%23%20ao%20chamar%20valor3%20%3D%20soma%2810,20%29%2B90,%20estou%20dizendo%3A%20execute%20a%20funcao,%0A%23%20coloque%20a%20resposta%20no%20lugar.%20Em%20algum%20sentido,%20depois%20que%20%0A%23%20a%20funcao%20retorna%20*30*,%20o%20c%C3%B3digo%20fica%20valor3%20%3D%20*30*%2B90&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

funcao adiciona

https://pythontutor.com/visualize.html#code=agenda_exemplo%20%3D%20%7B%7D%0Aagenda_exemplo%5B'marcos'%5D%3D32112232%0Aagenda_exemplo%5B'fabio'%5D%3D988887788%0Aagenda_exemplo%5B'maria'%5D%3D44554455%20%0A%0A%0A%23acesso%20no%20braco%0Atel_maria%20%3D%20agenda_exemplo%5B'maria'%5D%0Atel_fabio%20%3D%20agenda_exemplo%5B'fabio'%5D%0A%0Adef%20consulta%28agenda,pessoa%29%3A%0A%20%20%20%20%23tel_maria%20%3D%20agenda_exemplo%5B'maria'%5D%0A%20%20%20%20telefone%20%3D%20agenda%5Bpessoa%5D%0A%20%20%20%20return%20telefone%0A%20%20%20%20%0Atel_maria2%20%3D%20consulta%28agenda_exemplo,'maria'%29%0Atel_fabio2%20%3D%20consulta%28agenda_exemplo,'fabio'%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

consulta, adiciona, verifica

https://pythontutor.com/visualize.html#code=agenda1%20%3D%20%7B%7D%0Aagenda1%5B'marcos'%5D%3D32112232%0Aagenda1%5B'fabio'%5D%20%3D988887788%0Aagenda1%5B'maria'%5D%20%3D44554455%20%0A%0Aagenda2%20%3D%20%7B%7D%0Aagenda2%5B'fernanda'%5D%3D4444444%0Aagenda2%5B'manoel'%5D%20%20%3D5555555%0Aagenda2%5B'adriana'%5D%20%3D6666666%0A%0Adef%20consulta%28agenda,pessoa%29%3A%0A%20%20%20%20%23tel_maria%20%3D%20agenda_exemplo%5B'maria'%5D%0A%20%20%20%20telefone%20%3D%20agenda%5Bpessoa%5D%0A%20%20%20%20return%20telefone%0A%20%20%20%20%0Atel_fernanda%20%3D%20consulta%28agenda2,%20'fernanda'%29%0Atel_fabio%20%20%20%20%3D%20consulta%28agenda1,%20'fabio'%29%0A%20%20%20%20%0Adef%20adiciona%28agenda,pessoa,telefone%29%3A%0A%20%20%20%20agenda%5Bpessoa%5D%20%3D%20telefone%0A%20%20%20%20return%20agenda%0A%20%20%20%20%0Aadiciona%28agenda1,'mario',6666666%29%0Aadiciona%28agenda1,'mario',6565656%29%0A%20%20%0Adef%20verifica%28agenda,pessoa%29%3A%0A%20%20%20%20lista%20%3D%20agenda.keys%28%29%0A%20%20%20%20if%20pessoa%20in%20lista%3A%0A%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20%20%20%20%20%0Averifica%28agenda1,'mario'%29%0Averifica%28agenda2,'mario'%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

verifica v2
https://pythontutor.com/render.html#code=agenda1%20%3D%20%7B%7D%0Aagenda1%5B'marcos'%5D%3D32112232%0Aagenda1%5B'fabio'%5D%20%3D988887788%0Aagenda1%5B'maria'%5D%20%3D44554455%20%0A%0Aagenda2%20%3D%20%7B%7D%0Aagenda2%5B'fernanda'%5D%3D4444444%0Aagenda2%5B'manoel'%5D%20%20%3D5555555%0Aagenda2%5B'adriana'%5D%20%3D6666666%0A%0Adef%20adiciona%28agenda,pessoa,telefone%29%3A%0A%20%20%20%20agenda%5Bpessoa%5D%20%3D%20telefone%0A%20%20%20%20return%20agenda%0A%20%20%20%20%0Aadiciona%28agenda1,'mario',6666666%29%0Aadiciona%28agenda1,'mario',6565656%29%0A%20%20%0Adef%20verifica%28agenda,pessoa%29%3A%0A%20%20%20%20lista%20%3D%20agenda.keys%28%29%0A%20%20%20%20return%20pessoa%20in%20lista%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%0Averifica%28agenda1,'mario'%29%0Averifica%28agenda2,'mario'%29&cumulative=false&curInstr=20&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

verifica v3
https://pythontutor.com/render.html#code=agenda1%20%3D%20%7B%7D%0Aagenda1%5B'marcos'%5D%3D32112232%0Aagenda1%5B'fabio'%5D%20%3D988887788%0Aagenda1%5B'maria'%5D%20%3D44554455%20%0A%0Aagenda2%20%3D%20%7B%7D%0Aagenda2%5B'fernanda'%5D%3D4444444%0Aagenda2%5B'manoel'%5D%20%20%3D5555555%0Aagenda2%5B'adriana'%5D%20%3D6666666%0A%0Adef%20adiciona%28agenda,pessoa,telefone%29%3A%0A%20%20%20%20agenda%5Bpessoa%5D%20%3D%20telefone%0A%20%20%20%20return%20agenda%0A%20%20%20%20%0Aadiciona%28agenda1,'mario',6666666%29%0Aadiciona%28agenda1,'mario',6565656%29%0A%20%20%0Adef%20verifica%28agenda,pessoa%29%3A%0A%20%20%20%20lista%20%3D%20agenda.keys%28%29%0A%20%20%20%20return%20pessoa%20in%20lista%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%0Averifica%28agenda1,'mario'%29%0Averifica%28agenda2,'mario'%29&cumulative=false&curInstr=20&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

conta_letras

https://pythontutor.com/visualize.html#code=def%20conta_letras%28palavra%29%3A%0A%20%20%20%20contador%20%3D%20%7B%7D%0A%20%20%20%20for%20letra%20in%20palavra%3A%0A%20%20%20%20%20%20%20%20contador%5Bletra%5D%20%3D%200%0A%20%20%20%20for%20letra%20in%20palavra%3A%0A%20%20%20%20%20%20%20%20contador%5Bletra%5D%20%2B%3D%201%0A%20%20%20%20return%20contador%0A%0A%0Adef%20conta_letras2%28palavra%29%3A%0A%20%20%20%20contador%20%3D%20%7B%7D%0A%20%20%20%20for%20letra%20in%20palavra%3A%0A%20%20%20%20%20%20%20%20if%20letra%20not%20in%20contador.keys%28%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20contador%5Bletra%5D%20%3D%200%0A%20%20%20%20%20%20%20%20contador%5Bletra%5D%20%2B%3D%201%0A%20%20%20%20return%20contador%0A%0A%0Aconta_letras2%28%22banana%22%29%0Aconta_letras%28%22abacaxi%22%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

'''