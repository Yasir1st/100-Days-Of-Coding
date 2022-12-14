class Hero:
	# class variabel
	jumlah_hero = 0

	def __init__(self, inputName, inputHealth, inputPower, inputArmor):
		#instance variabel
		self.name = inputName
		self.health = inputHealth
		self.power = inputPower
		self.armor = inputArmor
		Hero.jumlah_hero += 1

	# void function, method tanpa return, tanpa argumen
	def siapa(self):
		print("Hero Name \t: ",self.name)
		print("Health \t\t: ",self.health)
		print("Power \t\t: ",self.power)
		print("Armor \t\t: ",self.armor)

	# method dengan argumen, tanpa return
	def healthUp(self,up):
		self.health += up

	# method dengan return
	def getHealth(self):
		return self.health


hero1 = Hero('Ayaka', 100, 150, 50)
hero2 = Hero('Zhongli', 200, 100, 100)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())