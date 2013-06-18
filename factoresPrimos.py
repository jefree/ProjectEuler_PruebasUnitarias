import unittest
from multiplosTest import es_factor

def es_primo(numero):

	factores = 0

	for i in range(1, int(numero**(0.5))+1):
		if numero % i == 0:
			factores += 1

	return factores == 1

def es_factor_primo(factor, numero):
	return es_factor(factor, numero) and es_primo(factor)


class EsPrimoTest(unittest.TestCase):

	def test_prueba_que_7_es_primo(self):
		self.assertEqual(es_primo(7), True);

	def test_prueba_que_13_es_primo(self):
		self.assertEqual(es_primo(13), True)

	def test_prueba_que_5_es_primo(self):
		self.assertEqual(es_primo(5), True)

	def test_prueba_que_4_no_es_primo(self):
		self.assertEqual(es_primo(4), False)

	def test_prueba_que_20000_no_es_primo(self):
		self.assertEqual(es_primo(20000), False)

	def test_prueba_que_0_no_es_primo(self):
		self.assertEqual(es_primo(0), False)

class EsFactorPrimoTest(unittest.TestCase):

	def test_prueba_que_2_es_factor_primo_de_100(self):
		self.assertEqual(es_factor_primo(2, 100), True)

	def test_prueba_que_13_es_factor_primo_de_91(self):
		self.assertEqual(es_factor_primo(13, 91), True)

	def test_prueba_que_10_no_es_factor_primo_de_2000(self):
		self.assertEqual(es_factor_primo(10, 2000), False)

	def test_prueba_que_7_no_es_factor_primo_de_23(self):
		self.assertEqual(es_factor_primo(7, 23), False)

	def test_prueba_que_29_es_factor_primo_de_13195(self):
		self.assertEqual(es_factor_primo(29, 13195), True)

class FactoresPrimosDeTest(unittest.TestCase):

	def test_prueba_que_los_factores_primos_de_13195_son(self):
		self.assertEqual(factores_primos_de(13195), [5,7,13,29])

if __name__ == '__main__':
	unittest.main()