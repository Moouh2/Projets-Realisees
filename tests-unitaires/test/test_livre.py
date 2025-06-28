import pytest
from tests_unitaires.livre import Livre

@pytest.fixture
def livre_exemple():
    return Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "123456789")

def test_creation_livre(livre_exemple):
    assert livre_exemple.titre == "Le Petit Prince"
    assert livre_exemple.auteur == "Antoine de Saint-Exupéry"
    assert livre_exemple.isbn == "123456789"
    assert livre_exemple.disponible is True

def test_emprunter_livre(livre_exemple):
    livre_exemple.emprunter()
    assert livre_exemple.disponible is False

def test_emprunter_livre_deja_emprunte(livre_exemple):
    livre_exemple.emprunter()
    with pytest.raises(ValueError, match="Livre déjà emprunté"):
        livre_exemple.emprunter()

def test_retourner_livre(livre_exemple):
    livre_exemple.emprunter()
    livre_exemple.retourner()
    assert livre_exemple.disponible is True

def test_retourner_livre_deja_disponible(livre_exemple):
    with pytest.raises(ValueError, match="Livre déjà disponible"):
        livre_exemple.retourner()