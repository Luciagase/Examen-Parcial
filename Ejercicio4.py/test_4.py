import unittest
from Ej4 import Alumno

class TestAlumno(unittest.TestCase):
    
    def test_str(self):
        alumno1 = Alumno('David', 7)
        resultado = str(alumno1)
        self.assertEqual(resultado, 'Alumno: David, Nota: 7')

if __name__ == '__main__':
    unittest.main()