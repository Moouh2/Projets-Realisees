import unittest
from tests_unitaires.ville_function import ville_pays

class VillePaysTest(unittest.TestCase):
    """Tests pour la fonction ville_pays()"""
    
    def test_ville_pays(self):
        """Test avec des noms comme"""
        chaine_formatee = ville_pays('Senegal', 'Dakar')
        self.assertEqual(chaine_formatee, 'Senegal, Dakar')

if __name__ == '__main__':
    unittest.main()
    