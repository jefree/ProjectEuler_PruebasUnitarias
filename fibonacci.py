import unittest

def es_par(num):
	return num % 2 == 0

def fibo(num, lista=[]):

	if num == 1:
		return [1]

	if num == 2:	
		lista = fibo(1)
		return lista + [2]

	lista = fibo(num-1)

	return lista+[lista[-1]+lista[-2]]

def fiboHasta(limite):

	continuar = True
	contador = 1

	while continuar:

		lista = fibo(contador)

		if lista[-1] > limite:
			continuar = False
			lista = lista[:-1]
		else:
			contador += 1

	return lista

def sumaFiboParesHasta(num):

	lista = fiboHasta(num)

	pares = []

	for n in lista:
		if es_par(n):
			pares.append(n)

	return sum(pares)

class ParTest(unittest.TestCase):

	def test_prueba_que_2_es_par(self):
		self.assertEqual(es_par(2), True)

	def test_prueba_que_5_no_es_par(self):
		self.assertEqual(es_par(5), False)

	def test_prueba_que_1628_es_par(self):
		self.assertEqual(es_par(1628), True)

	def test_prueba_que_818189_no_es_par(self):
		self.assertEqual(es_par(818189), False)

	def test_prueba_que_10000_es_par(self):
		self.assertEqual(es_par(10000), True)

	def test_prueba_que_99999_no_es_par(self):
		self.assertEqual(es_par(99999), False)

class NTerminosFibonacciTest(unittest.TestCase):

	def test_prueba_que_los_3_primeros_terminos_fibonacci_son(self):
		self.assertEqual(fibo(3), [1,2,3])

	def test_prueba_que_los_7_primeros_terminos_fibonacci_son(self):
		self.assertEqual(fibo(7), [1,2,3,5,8,13,21])

	def test_prueba_que_los_15_primeros_terminos_fibonacci_son(self):
		self.assertEqual(fibo(15), [1,2,3,5,8,13,21,34,55,89,144,233,377,610,987])

class TerminosFibonacciHasta(unittest.TestCase):

	def test_prueba_que_los_terminos_fibonacci_hasta_12_son(self):
		self.assertEqual(fiboHasta(12), [1,2,3,5,8])

	def test_prueba_que_los_terminos_fibonacci_hasta_40_son(self):
		self.assertEqual(fiboHasta(40), [1,2,3,5,8,13,21,34])

	def test_prueba_que_los_terminos_fibonacci_hasta_1000_son(self):
		self.assertEqual(fiboHasta(1000), [1,2,3,5,8,13,21,34,55,89,144,233,377,610,987])

class SumaTerminosFibonacciParesHasta(unittest.TestCase):

	def test_prueba_que_los_terminos_fibonacci_pares_hasta_10_suman_10(self):
		self.assertEqual(sumaFiboParesHasta(10),10)

	def test_prueba_que_los_terminos_fibonacci_pares_hasta_1000_suman_798(self):
		self.assertEqual(sumaFiboParesHasta(1000),798)

if __name__ == '__main__':
	unittest.main()