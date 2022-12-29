class Hero:
	def __init__(self,name,health):
		self.name = name
		self.health = health

	def showInfo(self):
		print("showInfo di class Hero")
		print("{} health: {}".format(
			self.name,
			self.health
			)
		)


class Hero_Hydro(Hero):
	def __init__(self,name):
		super().__init__(name,100)

	# override
	def showInfo(self):
		print("showInfo di subclass Hero_Hydro")
		print("{} \n\tTipe: intelligent, \n\thealth: {}".format(
			self.name,
			self.health
			)
		)


class Hero_Pyro(Hero):
	def __init__(self,name):
		super().__init__(name,200)


Ayato = Hero_Hydro('Ayato')
Thoma = Hero_Pyro('Thoma')

Ayato.showInfo()
Thoma.showInfo()