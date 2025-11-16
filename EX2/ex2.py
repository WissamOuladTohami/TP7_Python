import json
from datetime import datetime

class Serializable:
    def to_json(self):
        data = {k: v for k, v in self.__dict__.items() if k != "historique"}
        return json.dumps(data, ensure_ascii=False)

    @classmethod
    def from_json(cls, json_str):
        return cls(**json.loads(json_str))

class Historisable:
    def __init__(self):
        self.historique = []

    def enregistrer_etat(self):
        self.historique.append((datetime.now(), self.__dict__.copy()))

class Journalisable:
    def journaliser(self, message):
        print(f"[Journal] {datetime.now()}: {message}")

class Contrat(Serializable, Historisable, Journalisable):
    def __init__(self, id, description):
        Historisable.__init__(self)
        self.id = id
        self.description = description

    def modifier(self, nouvelle_desc):
        self.journaliser(f"Modification du contrat {self.id}")
        self.enregistrer_etat()
        self.description = nouvelle_desc

c = Contrat(1, "Initial")
c.modifier("Révisé")
print(c.to_json())