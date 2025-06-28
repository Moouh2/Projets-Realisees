class Sondage:
    """Permet de collecter des réponses sur des questions anonymes"""

    def __init__(self, question):
        """Initialiseur des attributs"""
        self.question = question
        self.reponses = []

    def affichez_question(self):
        print(self.question)

    def add_reponse(self, reponse):
        self.reponses.append(reponse)

    def get_resultat(self):
        print("Les réponses du sondage\n")
        print(f"Question: {self.question}")
        print("-------------------------------------------")
        for i in self.reponses:
            print(i)
            print("=====================================================")