import unittest
import vehiculos

class TestVehiculo(unittest.TestCase):
    def test_existencia_vehiculo(self):
        v = vehiculos.Vehiculo()
        self.assertIsNotNone(v)

    def test_existencia_atributos(self):
        t = vehiculos.Vehiculo('coche', 60, 3000)
        self.assertEqual(t.nombre, 'coche')
        self.assertEqual(t.velocidad_maxima, 60)
        self.assertEqual(t.kilometraje, 3000)
