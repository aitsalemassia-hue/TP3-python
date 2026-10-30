from Livre import Livre
from magazine import Magazine

if __name__ == "__main__":

     documents=[
          Livre("les misérables", "Victor Hugo", 1862),
          Magazine("Science et Vie", 1234, 2020),
          Livre("palastine", "Amin Maalouf", 2000),
          Magazine("programming", 5678, 2021)
     ]

     for document in documents:
          document.afficher()
          