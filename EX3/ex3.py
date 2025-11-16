from datetime import datetime
import copy

class ValidationMixin:
    def valider_titre(self):
        if not hasattr(self, "titre") or not self.titre.strip():
            raise ValueError("Le titre de la tâche est obligatoire et ne peut pas être vide.")

class HistoriqueMixin:
    def __init__(self):
        self._historique = []

    def enregistrer_historique(self, description):
        self._historique.append(copy.deepcopy(description))

    def afficher_historique(self):
        for i, desc in enumerate(self._historique, 1):
            print(f"{i}: {desc}")

class JournalisationMixin:
    def journaliser(self, message):
        print(f"[Journal] {datetime.now()}: {message}")

class Tache(ValidationMixin, HistoriqueMixin, JournalisationMixin):
    def __init__(self, titre, description):
        HistoriqueMixin.__init__(self)
        self.titre = titre
        self.valider_titre()
        self.description = description
        self.date_creation = datetime.now()
        self.journaliser(f"Tâche créée: {self.titre}")

    def mettre_a_jour(self, nouvelle_description):
        self.enregistrer_historique(self.description)
        self.description = nouvelle_description
        self.journaliser(f"Tâche mise à jour: {self.titre}")
        
t = Tache("Préparer rapport", "Rédiger le rapport annuel")
t.mettre_a_jour("Rédiger et relire le rapport annuel")
t.mettre_a_jour("Finaliser le rapport annuel")
print("Historique des descriptions :")
t.afficher_historique()