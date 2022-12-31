import os 
os.system("cls")

## Multiple Inheritance

# Parent Class
class Hero_clan:
    def setClan(self,clan):
        self.clan = clan

    def showClan(self):
        print("\tClan \t: {}".format(self.clan))

class Hero_element:
    def setElement(self,element):
        self.element = element

    def showElement(self):
        print("\tElement : {}".format(self.element))


# Child Class
class Hero(Hero_clan,Hero_element):
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print(f"{self.name} :\n\tHealth \t: {self.health}")


ayato = Hero("Kamisato Ayato",200)

ayato.setClan("Kamisato")
ayato.setElement("Hydro")

ayato.showInfo()
ayato.showElement()
ayato.showClan()
