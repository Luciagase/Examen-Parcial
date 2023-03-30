import unittest
from Ej3 import Alumno

class TestAlumno(unittest.TestCase):
    
    def test_str(self):
        alumno1 = Alumno('Juan', 8)
        resultado = str(alumno1)
        self.assertEqual(resultado, 'Alumno: Juan, Nota: 8')

if __name__ == '__main__':
    unittest.main()