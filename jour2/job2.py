class Personne:
    def __init__(self):
        age = 14
        self.age = age

    def afficherAge(self):
        print (self.age)

    def bonjour(self):
        print ("Hello")

    def modifierAge(self, age):
        self.age = age
        print("L'age de l'eleve est de", self.age, "ans")

class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)
        self.bonjour()
        self.allerEnCours()
        self.modifierAge(15)


    def allerEnCours(self):
        print ("Je vais en cours")

    def affichageAge(self):
        print ("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self, age, matiereEnseignée):
        self.bonjour()
        self.age = age
        self.matiereEnseignée = matiereEnseignée

        self.enseigner(self)

    def enseigner(self, matiereEnseignée):
        print("Le cours de", self.matiereEnseignée, "va commencer")

eleve1 = Eleve()
eleve1.bonjour

prof1 = Professeur(40, "maths")