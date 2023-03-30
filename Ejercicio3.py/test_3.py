import unittest
from Ej3 import Alumno

class TestAlumno(unittest.TestCase):
    
    def test_alumno_aprobado(self):
        alumno1 = Alumno('David', 7)
        resultado = alumno1.calificacion()
        self.assertEqual(resultado, 'El alumno Juan ha aprobado con un 7.')
        
    def test_alumno_suspendido(self):
        alumno2 = Alumno('Marieta', 4)
        resultado = alumno2.calificacion()
        self.assertEqual(resultado, 'El alumno Marieta ha suspendido con un 4.')

if __name__ == '__main__':
    unittest.main()
