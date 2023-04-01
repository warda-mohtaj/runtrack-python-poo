class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def setRectangle(self, longueur):
        self.__longueur = longueur
    
    def getRectangle(self):
        return self.__longueur
    
    def setRectangle(self, largeur):
        self.__largeur = largeur

    def getRectangle(self):
        return self.__largeur
    
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
    
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.surface() * self.__hauteur
    
rectangle1 = Rectangle(14, 8)
print("mon rectangle a un périmètre de", rectangle1.perimetre(), "cm et une surface de", rectangle1.surface(), "cm²")
parallelepipede1 = Parallelepipede(14, 8, 10)
print("mon parallélépipède a un volume de", parallelepipede1.volume(), "cm³")