import unittest

class ParTest(unittest.TestCase):

	def test_prueba_que_2_es_par(self):
		self.assertEqual(es_par(2), True)

	def test_prueba_que_5_no_es_par(self):
		self.assertEqual(es_par(5), False)

	def test_prueba_que_1628_es_par(self):
		self.assertEqual(es_par(2), True)

	def test_prueba_que_818189_no_es_par(self):
		self.assertEqual(es_par(818189), False)

	def test_prueba_que_2_es_par(self):
		self.assertEqual(es_par(2), True)

	def test_prueba_que_5_no_es_par(self):
		self.assertEqual(es_par(5), False)