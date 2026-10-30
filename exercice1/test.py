
#test
from employe import Employe
from manager import Manager
from devloppeur import Developpeur

if __name__=="__main__":
     #creation d'un employe
     employe1=Employe("Ahmed", 5000)
     print(employe1)
     print("Salaire total:", employe1.salaire_total(), "DH")

     #creation d'un manager
     manager1=Manager("Mohamed", 8000, 2000)
     print(manager1)
     print("Salaire total:", manager1.salaire_total(), "DH")

     #creation d'un developpeur
     developpeur1=Developpeur("Assiya", 6000, "Python")
     print(developpeur1)
     print("Salaire total:", developpeur1.salaire_total(), "DH")