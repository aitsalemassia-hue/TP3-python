

from employe import Employe


class Developpeur(Employe):
     def __init__(self,nom,salaire_base,langage):
          super().__init__(nom,salaire_base)
          self.langage=langage

     def salaire_total(self):
          bonus=500 if self.langage=="Python" else 0
          return self.salaire_base + bonus
     def __str__(self):
          return f"Developpeur - Nom: {self.nom}, Salaire de base: {self.salaire_base} DH, Langage: {self.langage}"




