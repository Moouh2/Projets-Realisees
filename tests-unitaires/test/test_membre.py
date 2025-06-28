import pytest
from tests_unitaires.membre import Membre
from tests_unitaires.livre import Livre

@pytest.fixture
def membre_exemple():
    return Membre(1, "Alice Dupont")

@pytest.fixture
def livre_exemple():
    return Livre("1984", "George Orwell", "987654321")

def test_creation_membre(membre_exemple):
    assert membre_exemple.id_membre == 1
    assert membre_exemple.nom == "Alice Dupont"
    assert membre_exemple.livres_empruntes == []

def test_emprunter_livre(membre_exemple, livre_exemple):
    membre_exemple.emprunter_livre(livre_exemple)
    assert livre_exemple in membre_exemple.livres_empruntes
    assert livre_exemple.disponible is False

def test_emprunter_livre_deja_emprunte(membre_exemple, livre_exemple):
    membre_exemple.emprunter_livre(livre_exemple)
    with pytest.raises(ValueError, match="Livre déjà emprunté par ce membre"):
        membre_exemple.emprunter_livre(livre_exemple)

def test_retourner_livre(membre_exemple, livre_exemple):
    membre_exemple.emprunter_livre(livre_exemple)
    membre_exemple.retourner_livre(livre_exemple)
    assert livre_exemple not in membre_exemple.livres_empruntes
    assert livre_exemple.disponible is True

def test_retourner_livre_non_emprunte(membre_exemple, livre_exemple):
    with pytest.raises(ValueError, match="Livre non emprunté par ce membre"):
        membre_exemple.retourner_livre(livre_exemple)