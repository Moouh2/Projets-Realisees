class Membre:
    def __init__(self, id_membre: int, nom: str):
        self.id_membre = id_membre
        self.nom = nom
        self.livres_empruntes = []

    def __str__(self):
        return f"Membre {self.id_membre}: {self.nom}"

    def emprunter_livre(self, livre):
        if livre in self.livres_empruntes:
            raise ValueError("Livre déjà emprunté par ce membre")
        self.livres_empruntes.append(livre)
        livre.emprunter()

    def retourner_livre(self, livre):
        if livre not in self.livres_empruntes:
            raise ValueError("Livre non emprunté par ce membre")
        self.livres_empruntes.remove(livre)
        livre.retourner()