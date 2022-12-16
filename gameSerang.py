'''Game Saling Serang Sederhana'''

class Hero:

    def __init__(self,name,health,attackPower,armorPower):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorPower = armorPower

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.diserang(self, self.attackPower)

    def diserang(self, lawan, attackNum):
        print(f"{self.name} diserang {lawan.name}")
        attack_yang_diterima = attackNum/self.armorPower
        print(f"Attack yang diterima \t: {attack_yang_diterima:.2f}")
        self.health -= attack_yang_diterima
        print(f"Darah \t\t\t: {self.health:.2f}")


diluc = Hero("Diluc",100,50,30)
ayaka = Hero("Ayaka",100,70,40)
zhongli = Hero("zhongli",110,10,50)

diluc.serang(zhongli)
print("\n")
ayaka.serang(diluc)
print("\n")
zhongli.serang(ayaka)