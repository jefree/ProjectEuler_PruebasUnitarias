import unittest
import multiplosTest

class EsPrimoTest(unittest.TestCase):

	def test_prueba_que_7_es_primo(self):
		self.assertEqual(es_primo(7), True);

	def test_prueba_que_13_es_primo(self):
		self.assertEqual(es_primo(13), True)

	def test_prueba_que_5_es_primo(self):
		self.assertEqual(es_primo(5), True)

	def test_prueba_que_4_no_es_primo(self):
		self.assertEqual(es_primo(2), False)

	def test_prueba_que_20000_no_es_primo(self):
		self.assertEqual(es_primo(20000), False)

	def test_prueba_que_0_no_es_primo(self):
		self.assertEqual(es_primo(0), False)

if __name__ == '__main__':
	unittest.main()