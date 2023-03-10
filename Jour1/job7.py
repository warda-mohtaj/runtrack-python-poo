class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def gauche(self):
        self.x -= 1
    
    def droite(self):
        self.x += 1
    
    #pour les axes haut et bas
    def haut(self):
        self.y -= 1
    
    def bas(self):
        self.y += 1
    
    def position(self):
        return(self.x, self.y)

point1 = Personnage(100, 200)
point1.droite()
point1.bas()
print(point1.position())

point2 = Personnage(100, 200)
point2.gauche()
point2.haut()
print(point2.position())