class Livre:
    def __init__(self, titre: str, auteur: str, isbn: str):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        return f"{self.titre} par {self.auteur}"

    def emprunter(self):
        if not self.disponible:
            raise ValueError("Livre déjà emprunté")
        self.disponible = False

    def retourner(self):
        if self.disponible:
            raise ValueError("Livre déjà disponible")
        self.disponible = True