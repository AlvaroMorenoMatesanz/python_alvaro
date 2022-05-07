import unittest
from practica2 import Calculador

class TestRunner(unittest.TestCase):
    def test_gastosAnuales(self):
        self.assertEqual(Calculador().GastosAnuales(), -296791)

    def test_MesQueMasSeHaAhorrado(self):
        self.assertEqual(Calculador().MesQueMasSeHaAhorrado(), "Enero")

    def test_MesQueMasSeHaGastado(self):
        self.assertEqual(Calculador().MesQueMasSeHaGastado(), "Abril")

    def test_IngresosAnuales(self):
        self.assertEqual(Calculador().IngresosAnuales(), 280961)

        
if __name__ == '__main__':
    unittest.main()
