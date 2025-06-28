import unittest
from tests_unitaires.sondage_fonction import Sondage

class SondageTest(unittest.TestCase):
	"""test les méthodes de la classe Sondage"""

	def test_add_une_seule_reponse(self):
		question = "Python supporte combien de paradigmes \ de programation?"
		reponse = "Trois paradigmes"
		sondage = Sondage(question)
		sondage.add_reponse(reponse)
		self.assertEqual(sondage.reponses[0], "Trois paradigmes")
  
  
  
if __name__ == '__main__':
    unittest.main()