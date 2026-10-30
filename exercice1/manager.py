
from employe import Employe
class Manager(Employe):
     #constructor
     def __init__(self, nom, salaire_base, prime):
          super().__init__(nom, salaire_base)
          self.prime=prime

     #methode salaire_total 
     def salaire_total(self):
          return self.salaire_base + self.prime
     def __str__(self):
          return f"Manager - Nom: {self.nom}, Salaire de base: {self.salaire_base} DH, Prime: {self.prime} DH"



