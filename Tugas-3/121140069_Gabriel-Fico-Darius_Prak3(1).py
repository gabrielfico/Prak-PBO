class AkunBank:
    listpel = 0

    def __init__(self, nopel, napel, jumsal):
        self.__nopel = nopel
        self.__napel = napel
        self.__jumsal = jumsal
        AkunBank.listpel += 1

    def lihat_saldo():
        print(Akun1.__napel, "memiliki saldo Rp", Akun1.__jumsal)

    def tarik_tunai():
        while True:
            tarik = int(input("Masukan jumlah nominal yang ingin ditarik : "))

            if tarik > Akun1.__jumsal:
                print("Nominal saldo yang Anda punya tidak cukup!")
            else:
                Akun1.__jumsal -= tarik
                print("Saldo berhasil ditarik!")
                break
    
    def transfer():
        transfer = int(input("Masukan nominal yang ingin ditransfer : "))
        tujuan = int(input("Masukan no rekening tujuan : "))
        
        if tujuan == Akun2.__nopel:
            Akun2.__jumsal += transfer
            Akun1.__jumsal -= transfer
            print("Transfer Rp ", transfer, " ke ", Akun2.__napel, " sukses!")
        elif tujuan == Akun3.__nopel:
            Akun3.___jumsal += transfer
            Akun1.__jumsal -= transfer
            print("Transfer Rp ", transfer, " ke ", Akun3.__napel, " sukses!")
        else:
            print("No rekening tujuan tidak dikenal!")

    def lihat_menu():
        print("Selamat datang di Bank Jago")
        print("Halo Gabriel Fico, ingin melakukan apa?")
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")
        n = int(input("Masukan nomor input : "))

        print()
        if n == 1:
            AkunBank.lihat_saldo()
        elif n == 2:
            AkunBank.tarik_tunai()
        elif n == 3:
           AkunBank.transfer()
        elif n == 4:
            exit(0)
 
        print()
        print()
        AkunBank.lihat_menu()

Akun1 = AkunBank(1234, "Gabriel Fico", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

AkunBank.lihat_menu()
