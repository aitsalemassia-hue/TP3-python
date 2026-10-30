

class Employe:
     #constructor
     def __init__(self, nom, salaire_base):
          self.nom=nom
          self.salaire_base=salaire_base

     #methode salaire_total 
     def salaire_total(self):
          return self.salaire_base
     def __str__(self):
          return f"Employe - Nom: {self.nom}, Salaire de base: {self.salaire_base} DH"


