class Mangga:

	#magic method
	def __init__(self,nama,jumlah):
		self.nama = nama
		self.jumlah = jumlah

    # repr dan str memiliki kegunaan yang sama namun jika keduanya digunakan maka str yang akan dieksekusi
	def __repr__(self):
		return "Debug - Mangga: {} dengan jumlah: {}".format(self.nama,self.jumlah)

	def __str__(self):
		return "Mangga: {} dengan jumlah: {}".format(self.nama,self.jumlah)

	def __add__(self,objek):
		return f"Total Jumlah Mangga : {self.jumlah + objek.jumlah}"

	@property
	def __dict__(self):
		return "objek ini mempunyai nama dan jumlah"


belanja1 = Mangga("Macan",10)
belanja2 = Mangga("Manalagi",30)
print(belanja1)
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)