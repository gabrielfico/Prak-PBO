class Robot:
    jumlah_turn = 0
    def __init__(self, nama, health, damage):
        self.nama = nama
        self.health = health
        self.damage = damage

class Antares(Robot):
    def __init__(self):
        super().__init__(self)
        self.nama = "Antares"
        self.health = 50000
        self.damage = 5000

class Alphasetia(Robot):
    def __init__(self):
        super().__init__(self)
        self.nama = "Alphasetia"
        self.health = 40000
        self.damage = 6000

class Lecalicus(Robot):
    def __init__(self):
        super().__init__(self)
        self.nama = "Lecalicius"
        self.health = 45000
        self.damage = 5500

print("Selamat datang di pertandingan robot Yamako")
n = int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) : "))
if n == 1:
    Mine = Antares()
elif n == 2:
    Mine = Alphasetia()
elif n == 3:
    Mine = Lecalicus()

n = int(input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) : "))
if n == 1:
    Enemy = Antares()
elif n == 2:
    Enemy = Alphasetia()
elif n == 3:
    Enemy = Lecalicus()

print("Selanjutnya, pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting")
