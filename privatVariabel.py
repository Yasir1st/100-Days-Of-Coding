class Hero:

	# class variabel
	jumlah = 0
	__privateJumlah = 0

	def __init__(self,name,health):
		self.name = name
		self.health = health

		# variabel instance private
		self.__private = "private"
		# variabel instance protected
		self._protected = "protected" # Pror=tected variabel dapat di akses sama dengan public variabel namun biasanya hanya digunakan di sebuah class tanpa merubah isinya
        



lina = Hero("lina",100)

print(lina.__dict__)
print(Hero.__dict__)
# print(Hero.__privateJumlah) , privat variabel tidak dapat diakses

# Jadi variabel private dapat ditulisan dengan __privatNamaVariabel