import unittest


class TestClass01(unittest.TestCase):
    """Ma première classe test unitaire"""

    def test_case01(self):
        """Mon premier cas test"""
        une_chaine = "PYTHON"
        nombre_entier = 25

        self.assertTrue(isinstance(une_chaine, str))
        self.assertTrue(isinstance(nombre_entier, int))

if __name__ == "__main__":
    unittest.main()