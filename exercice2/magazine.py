
from document import Document
class Magazine(Document):
     def __init__(self, titre, numero, annee):
          super().__init__(titre, annee)
          self.numero = numero


     def afficher(self):
          print(f"Magazine - Titre: {self.titre}, Numéro: {self.numero}, Année: {self.annee}")