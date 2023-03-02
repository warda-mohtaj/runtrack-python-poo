class CompteBancaire:
    def __init__(self, num_compte, nom, prenom, solde):
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.decouvert = True
    
    def afficher(self):
        print(f"Bonjour, {self.__nom} {self.__prenom}, le solde de votre compte n°{self.__num_compte} est {self.__solde}")
    
    def afficherSolde(self):
        print(f"Pour le compte n°{self.__num_compte}, le solde est {self.__solde}")
    
    def versement(self, montant):
        self.__solde += montant
    
    def retrait(self, montant):
        self.__solde -= montant
        print(f"Votre nouveau solde est {self.__solde}")
        self.agios()
    
    def agios(self):
        if self.__solde < 0:
            self.__solde *= 1.1
    
    def virement(self, compte, montant):
        if montant <= self.__solde:
            compte.__solde += montant
            self.__solde -= montant
            print(f"Le virement du compte n°{self.__num_compte} vers le compte {compte.__num_compte} a été effectué. \
                  \n Voici les soldes respectifs des compte à jour {self.__solde} et {compte.__solde}")
        
        else:
            print("Le Virement est impossible")


warda = CompteBancaire(1234, "Mohtaj", "Warda", 2500)
warda.afficherSolde()
warda.versement(500)
warda.afficherSolde()
warda.retrait(200)

safa = CompteBancaire(4321, "hand", "safa", 10)

warda.virement(safa, 1000)

safa.afficherSolde()
safa.retrait(2000)
safa.afficherSolde()
safa.versement(3000)
safa.afficherSolde()
safa.retrait(2000)

safa.virement(warda, 200)