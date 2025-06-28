class GestionnaireTaches:
    def __init__(self):
        self.taches = []
        self.taches_completees = []

    def ajouter_tache(self, description: str):
        if not description.strip():
            raise ValueError("La description ne peut pas être vide")
        self.taches.append(description)

    def completer_tache(self, index: int):
        if index < 0 or index >= len(self.taches):
            raise IndexError("Index de tâche invalide")
        tache = self.taches.pop(index)
        self.taches_completees.append(tache)

    def supprimer_tache(self, index: int):
        if index < 0 or index >= len(self.taches):
            raise IndexError("Index de tâche invalide")
        self.taches.pop(index)

    def lister_taches(self):
        return self.taches.copy()

    def lister_taches_completees(self):
        return self.taches_completees.copy()

    def nombre_total_taches(self):
        return len(self.taches) + len(self.taches_completees)