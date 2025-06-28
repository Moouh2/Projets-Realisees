from typing import List, Dict
from .livre import Livre
from .membre import Membre

class Bibliotheque:
    def __init__(self):
        self.catalogue: Dict[str, Livre] = {}
        self.membres: Dict[int, Membre] = {}

    def ajouter_livre(self, livre: Livre):
        if livre.isbn in self.catalogue:
            raise ValueError("Livre déjà dans le catalogue")
        self.catalogue[livre.isbn] = livre

    def enregistrer_membre(self, membre: Membre):
        if membre.id_membre in self.membres:
            raise ValueError("Membre déjà enregistré")
        self.membres[membre.id_membre] = membre

    def rechercher_livre(self, titre: str = None, auteur: str = None) -> List[Livre]:
        resultats = []
        for livre in self.catalogue.values():
            if (titre is None or titre.lower() in livre.titre.lower()) and \
               (auteur is None or auteur.lower() in livre.auteur.lower()):
                resultats.append(livre)
        return resultats

    def emprunter_livre(self, id_membre: int, isbn: str):
        if id_membre not in self.membres:
            raise ValueError("Membre non enregistré")
        if isbn not in self.catalogue:
            raise ValueError("Livre non trouvé")
        
        membre = self.membres[id_membre]
        livre = self.catalogue[isbn]
        membre.emprunter_livre(livre)

    def get_livres_empruntes(self, id_membre: int) -> List[Livre]:
        if id_membre not in self.membres:
            raise ValueError("Membre non enregistré")
        return self.membres[id_membre].livres_empruntes