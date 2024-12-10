
import unittest

class TestStringMethods(unittest.TestCase):
    def test_001a_diretor(self):
        self.assertEqual(diretor("menace", 2003),"Ron Smith")
        self.assertEqual(diretor("Joker", 2019),"Todd Phillips")

    def test_001b_diretor_filme_nao_encontrado(self):
        self.assertRaises(FilmeNaoEncontrado,diretor,nome_filme="banananana",ano=2023)
        self.assertRaises(FilmeNaoEncontrado,diretor,nome_filme="memorias_de_fulano",ano=1986)

    def test_002a_quantos_ratings(self):
        self.assertEqual(quantos_ratings("menace", 2003),1)
        self.assertEqual(quantos_ratings("Joker", 2019),3)

    def test_002b_quantos_ratings_filme_nao_encontrado(self):
        self.assertRaises(FilmeNaoEncontrado,quantos_ratings,nome_filme="banananana",ano=2023)
        self.assertRaises(FilmeNaoEncontrado,quantos_ratings,nome_filme="memorias_de_fulano",ano=1986)


    def test_003a_altura_pokemon(self):
        self.assertEqual(altura_pokemon('jigglypuff'),5)
        self.assertEqual(altura_pokemon('diglett'),2)

    def test_003b_altura_pokemon_nao_existe(self):
        self.assertRaises(PokemonNaoEncontrado,altura_pokemon,nome_pokemon='bob esponja')
        self.assertRaises(PokemonNaoEncontrado,altura_pokemon,nome_pokemon='batima')

    def test_004a_habilidade_pokemon(self):
        self.assertEqual(habilidade('diglett','hp'),10)
        self.assertEqual(habilidade('diglett','defense'),25)
        self.assertEqual(habilidade('mew','speed'),100)


    def test_004b_habilidade_pokemon(self):
        self.assertRaises(HabilidadeNaoEncontrada,habilidade,'diglett','vigor')
        self.assertRaises(HabilidadeNaoEncontrada,habilidade,'mew','CHA')
        self.assertRaises(HabilidadeNaoEncontrada,habilidade,'mew','STR')
        self.assertRaises(HabilidadeNaoEncontrada,habilidade,'mew','WIS')
        self.assertRaises(HabilidadeNaoEncontrada,habilidade,'mew','INT')
        self.assertRaises(HabilidadeNaoEncontrada,habilidade,'mew','DEX')
        self.assertRaises(HabilidadeNaoEncontrada,habilidade,'mew','CON')

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity = 2, failfast = True).run(suite)




from prova import *
#from omdb_gabarito import *    
runTests()
