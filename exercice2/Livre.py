from document import Document

class Livre(Document):
     def __init__(self, titre, auteur, annee):
          super().__init__(titre, annee)
          self.auteur = auteur
          self.annee = annee


     def afficher(self):
          print(f"Livre - Titre: {self.titre}, Auteur: {self.auteur}, Année: {self.annee}")