import unittest


class CalculTest(unittest.TestCase):
    """Ma deuxième classe de test unitaire"""

    def test_addition_nombre_entiers_positif(self):
        """Test l'addition de deux nombres entiers"""

        nombre1 = 5
        nombre2 = 10
        resultat_attendu = 15
        resultat_obtenue = nombre1 + nombre2
        self.assertEqual(resultat_attendu, resultat_obtenue)


if __name__ == '__main__':
    unittest.main()