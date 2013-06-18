import unittest

def es_factor(num1, num2):
	return False if num1==0 else num2 % num1 == 0

def es_factor_de_tres_o_cinco(num1):
	
	if es_factor(3, num1):
		return True

	if es_factor(5, num1):
		return True

	return False

def suma_factores_de_tres_o_cinco_hasta(limit):

	result = 0

	for i in range(0, limit):
		if es_factor_de_tres_o_cinco(i):
			result += i

	return result

class FactorTest(unittest.TestCase):

	def test_prueba_que_uno_deberia_ser_factor_de_cero(self):
		self.assertEqual(es_factor(1,0),True)

	def test_prueba_que_dos_no_deberia_ser_factor_de_tres(self):
		self.assertEqual(es_factor(2,3), False)

	def test_prueba_que_diez_deberia_ser_factor_de_veinte(self):
		self.assertEqual(es_factor(10, 20), True)

	def test_prueba_que_dos_no_deberia_ser_factor_de_siete(self):
		self.assertEqual(es_factor(2,7), False)

	def test_prueba_que_uno_deberia_ser_factor_de_siete(self):
		self.assertEqual(es_factor(1,7), True)

	def test_prueba_que_tres_no_deberia_ser_factor_de_siete(self):
		self.assertEqual(es_factor(3,7), False)	

class FactorDeTresoCincoTest(unittest.TestCase):

	def test_prueba_que_tres_deberia_ser_factor(self):
		self.assertEqual(es_factor_de_tres_o_cinco(3), True)

	def test_prueba_que_5_deberia_ser_factor(self):
		self.assertEqual(es_factor_de_tres_o_cinco(5), True)

	def test_prueba_que_17_no_deberia_ser_factor(self):
		self.assertEqual(es_factor_de_tres_o_cinco(17), False)

	def test_prueba_que_21_deberia_ser_factor(self):
		self.assertEqual(es_factor_de_tres_o_cinco(21), True)

	def test_prueba_que_16_no_deberia_ser_factor(self):
		self.assertEqual(es_factor_de_tres_o_cinco(16), False)

	def test_prueba_que_15_deberia_ser_factor(self):
		self.assertEqual(es_factor_de_tres_o_cinco(15), True)

	def test_prueba_que_19638_deberia_ser_factor(self):
		self.assertEqual(es_factor_de_tres_o_cinco(19638), True)

	def test_prueba_que_45018_deberia_ser_factor(self):
		self.assertEqual(es_factor_de_tres_o_cinco(45019), False)

class SumaFactoreesdeTresoCincoTest(unittest.TestCase):

	def test_prueba_que_la_suma_de_los_factores_hasta_10_deberia_ser_23(self):
		self.assertEqual(suma_factores_de_tres_o_cinco_hasta(10), 23)

if __name__ == '__main__':
	#unittest.main()
	print suma_factores_de_tres_o_cinco_hasta(1000)