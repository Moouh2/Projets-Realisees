import unittest

class calcultsTest(unittest.TestCase):
    
    def test_add(self):
        nombre1 = 5
        nombre2 = 10
        resultat_attendu = 15
        resultat_obtenu = add(nombre1, nombre2)
        
        self.assertEqual(resultat_obtenu, resultat_attendu)
        
    def test_soustract(self):
        nombre1 = 20
        nombre2 = 6
        resultat_attendu = 14
        resultat_obtenu = add(nombre1, nombre2)
        
        self.assertEqual(resultat_obtenu, resultat_attendu)
        

if __name__ == "__main__":
    unittest.main()