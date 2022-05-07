import unittest
import csv




path = 'finanzas2020.csv'

dataset = {}
columnas = []
with open(path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter='\t')
    line_count = 0
    columnas = next(csv_reader)
    # Inicializamos el diccionario con listas vacías
    for i in columnas:
        dataset[i] = []

    for linea in csv_reader:   
        dataset[columnas[0]].append(linea[0])
        # Añadimos cada dato a la lista correspondiente del diccionario
        for i in range(1, len(dataset)):
            dataset[columnas[i]].append(linea[i])
      
    print(f'Processed {line_count} lines.')

        # Creamos las funciones las cuales nos van a sacar los datos que queremos
class Calculador:
    dataset = {}
    def __init__(self):
        self.dataset = dataset

    def MesQueMasSeHaGastado(self):
        total = {}
        for mes in self.dataset:
            total[mes] = (self.ObtenerPerdidadPorMes(mes))
        return min(total, key=total.get)

    def MesQueMasSeHaAhorrado(self):
        total = {}
        for mes in self.dataset:
            total[mes] = (self.ObtenerAhorroPorMes(mes))
        print(total)
        return max(total, key=total.get)
    
    def IngresosAnuales(self):
        total = 0
        for mes in self.dataset:
            total += self.ObtenerIngresosPorMes(mes)
        return total

    def GastosAnuales(self):
        total = 0
        for mes in self.dataset:
            total += self.ObtenerPerdidadPorMes(mes)
        return total

        # Usamos try y except 
    
    def ObtenerPerdidadPorMes(self, mes):
        total = 0
        datosMes = self.dataset[mes]
        for value in datosMes:
            try:
                val =int(value)
                if(val < 0):
                    total += val
            except ValueError:
                print("El valor " + value + " no es numerico, para el mes " + mes) 
        return total

    def ObtenerIngresosPorMes(self, mes):
        total = 0
        datosMes = self.dataset[mes]
        for value in datosMes:
            try:
                val =int(value)
                if(val > 0):
                    total += val
            except ValueError:
                print("El valor " + value + " no es numerico, para el mes " + mes) 
        return total

    def ObtenerAhorroPorMes(self, mes):
        total = 0
        datosMes = self.dataset[mes]
        for value in datosMes:
            try:
                val =int(value)
                total += val
            except ValueError:
                print("El valor " + value + " no es numerico, para el mes " + mes) 
        return total

calculador =  Calculador()
gastosAnuales = calculador.GastosAnuales()
ingresosAnuales = calculador.IngresosAnuales()
MesQueMasSeHaAhorrado = calculador.MesQueMasSeHaAhorrado()
MesQueMasSeHaGastado = calculador.MesQueMasSeHaGastado()
print("GASTOS ANUALES: " + str(gastosAnuales))
print("INGRESOS ANUALES: " + str(ingresosAnuales))
print("MES CON MAS AHORRO: " + str(MesQueMasSeHaGastado))
print("MES CON MAS GASTO: " + str(MesQueMasSeHaAhorrado))


class TestRunner(unittest.TestCase):
    def test_gastosAnuales(self):
        self.assertEqual(Calculador().GastosAnuales(), -296791)

    def test_MesQueMasSeHaAhorrado(self):
        self.assertNotEqual(Calculador().MesQueMasSeHaAhorrado(), "p")

    def test_MesQueMasSeHaGastado(self):
        self.assertTrue(Calculador().MesQueMasSeHaGastado(), "Abril")

    def test_IngresosAnuales(self):
        self.assertFalse(Calculador().IngresosAnuales(), 280961)

        
if __name__ == '__main__':
    unittest.main()
