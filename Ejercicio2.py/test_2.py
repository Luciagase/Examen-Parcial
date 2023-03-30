import unittest
from Ej2 import Lista

class TestLista(unittest.TestCase):
    def setUp(self):
        self.lista = Lista([18, 50, 210, 80, 145, 333, 70, 30])

    def test_multiplo_de_10_y_menor_que_200(self):
        expected_output = [18, 50, 210, 80, 145, 333, 70, 30]
        output = self.lista.multiplo_de_10_y_menor_que_200()
        self.assertEqual(output, expected_output)

    def test_merge_sort(self):
        expected_output = [18, 50, 210, 80, 145, 333, 70, 30]
        output = self.lista.merge_sort()
        self.assertEqual(output, expected_output)

    def test_indice_valor(self):
        self.assertEqual(self.lista.indice_valor(145), 4)
