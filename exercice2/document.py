class Document :
     def __init__(self,titre,annee):
          self.titre=titre
          self.annee=annee



     def afficher(self):
          print(f"Document - Titre: {self.titre}, Année: {self.annee}")

     