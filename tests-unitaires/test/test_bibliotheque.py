import pytest
from tests_unitaires.bibliotheque import Bibliotheque
from tests_unitaires.livre import Livre
from tests_unitaires.membre import Membre

@pytest.fixture
def bibliotheque():
    return Bibliotheque()

@pytest.fixture
def livre_exemple():
    return Livre("Dune", "Frank Herbert", "111222333")

@pytest.fixture
def membre_exemple():
    return Membre(1, "Jean Martin")

def test_ajouter_livre(bibliotheque, livre_exemple):
    bibliotheque.ajouter_livre(livre_exemple)
    assert livre_exemple.isbn in bibliotheque.catalogue
    assert len(bibliotheque.catalogue) == 1

def test_ajouter_livre_duplique(bibliotheque, livre_exemple):
    bibliotheque.ajouter_livre(livre_exemple)
    with pytest.raises(ValueError, match="Livre déjà dans le catalogue"):
        bibliotheque.ajouter_livre(livre_exemple)

def test_enregistrer_membre(bibliotheque, membre_exemple):
    bibliotheque.enregistrer_membre(membre_exemple)
    assert membre_exemple.id_membre in bibliotheque.membres
    assert len(bibliotheque.membres) == 1

def test_rechercher_livre(bibliotheque):
    livres = [
        Livre("Livre A", "Auteur X", "001"),
        Livre("Livre B", "Auteur Y", "002"),
        Livre("Autre Livre", "Auteur X", "003")
    ]
    for livre in livres:
        bibliotheque.ajouter_livre(livre)
    
    resultats = bibliotheque.rechercher_livre(auteur="Auteur X")
    assert len(resultats) == 2
    assert all(livre.auteur == "Auteur X" for livre in resultats)

def test_emprunter_livre(bibliotheque, livre_exemple, membre_exemple):
    bibliotheque.ajouter_livre(livre_exemple)
    bibliotheque.enregistrer_membre(membre_exemple)
    bibliotheque.emprunter_livre(1, "111222333")
    
    livres_empruntes = bibliotheque.get_livres_empruntes(1)
    assert len(livres_empruntes) == 1
    assert livres_empruntes[0].isbn == "111222333"
    assert livres_empruntes[0].disponible is False