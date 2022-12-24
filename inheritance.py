# Inharktance

class Hero:
    
    def __init__(self,name,health,power):
        self.name = name
        self.health = health
        self.power = power

class HeroAnemo(Hero):
    pass

class HeroCryo(Hero):
    pass

# Tanpa Inheritance
diluc = Hero("Diluc",100,50)
print(diluc.name)

# Manggunakan Inheritance
Kazuha = HeroAnemo("Kazuha",100,60)
print(Kazuha.name)
print(help(Kazuha))

Ayaka = HeroCryo("Ayaka",100,100)
print(Ayaka.__dict__)