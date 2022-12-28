import os
os.system("cls")

class Hero:
	def __init__(self,name,health):
		self.name = name
		self.health = health

	def showInfo(self):
		print (f"{self.name} dengan health: {self.health}")

class Hero_Geo(Hero):
	def __init__(self,name):
		#Hero.__init__(self, name, 100)
		super().__init__(name, 300)
		super().showInfo()

class Hero_Anemo(Hero):
	def __init__(self,name):
		super().__init__(name, 100)
		super().showInfo()

lina = Hero_Geo('Noelle')
axe = Hero_Anemo('Xiao')