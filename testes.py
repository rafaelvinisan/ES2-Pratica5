import unittest
from utils import calcular_fatorial, calcular_media, verificar_palindrome

class TestPrograma(unittest.TestCase):

    def test_calcular_fatorial(self):
        self.assertEqual(calcular_fatorial(0), 1)
        self.assertEqual(calcular_fatorial(1), 1)
        self.assertEqual(calcular_fatorial(5), 120)
        self.assertEqual(calcular_fatorial(10), 3628800)
        self.assertRaises(ValueError, calcular_fatorial, -1)

    def test_calcular_media(self):
        self.assertEqual(calcular_media([1, 2, 3, 4, 5]), 3)
        self.assertAlmostEqual(calcular_media([1.5, 2.5, 3.5, 4.5]), 3.0)
        self.assertEqual(calcular_media([10]), 10)
        self.assertRaises(ValueError, calcular_media, [])

    def test_verificar_palindrome(self):
        self.assertTrue(verificar_palindrome("radar"))
        self.assertTrue(verificar_palindrome("A man a plan a canal Panama"))
        self.assertFalse(verificar_palindrome("hello"))
        self.assertFalse(verificar_palindrome("python"))

    def test_calcular_fatorial_grande(self):
        self.assertEqual(calcular_fatorial(20), 2432902008176640000)
        self.assertEqual(calcular_fatorial(25), 15511210043330985984000000)

    def test_calcular_media_decimais(self):
        self.assertAlmostEqual(calcular_media([1.1, 2.2, 3.3, 4.4]), 2.75)
        self.assertAlmostEqual(calcular_media([0.5, 1.5, 2.5, 3.5]), 2.0)

if __name__ == '__main__':
    unittest.main()
