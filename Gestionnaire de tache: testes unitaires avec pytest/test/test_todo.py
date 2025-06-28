import pytest
from src.todo import GestionnaireTaches

@pytest.fixture
def gestionnaire():
    return GestionnaireTaches()

def test_ajout_tache(gestionnaire):
    gestionnaire.ajouter_tache("Faire les courses")
    assert "Faire les courses" in gestionnaire.lister_taches()
    assert gestionnaire.nombre_total_taches() == 1

def test_ajout_tache_vide(gestionnaire):
    with pytest.raises(ValueError, match="La description ne peut pas être vide"):
        gestionnaire.ajouter_tache("")

def test_completer_tache(gestionnaire):
    gestionnaire.ajouter_tache("Faire du sport")
    gestionnaire.completer_tache(0)
    assert len(gestionnaire.lister_taches()) == 0
    assert "Faire du sport" in gestionnaire.lister_taches_completees()

def test_completer_tache_invalide(gestionnaire):
    with pytest.raises(IndexError, match="Index de tâche invalide"):
        gestionnaire.completer_tache(0)

def test_supprimer_tache(gestionnaire):
    gestionnaire.ajouter_tache("Appeler maman")
    gestionnaire.supprimer_tache(0)
    assert len(gestionnaire.lister_taches()) == 0
    assert gestionnaire.nombre_total_taches() == 0

def test_listes_separees(gestionnaire):
    gestionnaire.ajouter_tache("Tache 1")
    gestionnaire.ajouter_tache("Tache 2")
    gestionnaire.completer_tache(0)
    
    assert gestionnaire.lister_taches() == ["Tache 2"]
    assert gestionnaire.lister_taches_completees() == ["Tache 1"]
    assert gestionnaire.nombre_total_taches() == 2

def test_plusieurs_operations(gestionnaire):
    # Ajout
    gestionnaire.ajouter_tache("A")
    gestionnaire.ajouter_tache("B")
    gestionnaire.ajouter_tache("C")
    
    # Completion
    gestionnaire.completer_tache(1)  # Complete B
    
    # Suppression
    gestionnaire.supprimer_tache(0)  # Supprime A
    
    # Vérifications
    assert gestionnaire.lister_taches() == ["C"]
    assert gestionnaire.lister_taches_completees() == ["B"]
    assert gestionnaire.nombre_total_taches() == 2