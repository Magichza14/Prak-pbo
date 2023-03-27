class AkunBank:

    # Dipake buat nyimpen daftar pelanggan
    list_pelanggan = []

    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo

        # Biar nambah jumlah listnya pelanggannya
        AkunBank.list_pelanggan.append(self)

    def jalankan(self):
        while True:
            daftar_menu = ["Lihat Saldo", "Tarik Tunai", "Transfer Saldo", "Keluar"]
            for i in range(len(daftar_menu)):
                print(i+1, daftar_menu[i])

            pilih = int(input("Pilih Menu [1/2/3/4]:"))
            if pilih > len(daftar_menu) or pilih <= 0:
                print("Menu tidak tersedia, silahkan pilih menu yang tersedia saja ya!")
            else :
                if pilih == 1:
                    self.lihat_saldo()
                elif pilih == 2:
                    nominal_tarik = int(input("Masukkan nominal:"))
                    self.tarik_tunai(nominal_tarik)
                elif pilih == 3:
                    nominal_tf = int(input("Masukkan nominal transfer:"))
                    nomor_tujuan_tf = int(input("Masukkan nomor tujuan:"))
                    self.transfer(nominal_tf, nomor_tujuan_tf)
                elif pilih == 4:
                    print("Terimakasih sudah menggunakan bank kami")
                    break            
            print()

    # Cetak jumlah saldo 
    def lihat_saldo(self):
        print("Hai,", self.get_nama(), "! Sisa saldo kamu Rp.", self.get_saldo())

    # Tarik tunai fungsi paling gampang kedua setelah cek saldo
    def tarik_tunai(self, tarik):
        if tarik > self.get_saldo():
            print("Jumlah saldo tidak mencukupi!")
        else :
            self.__jumlah_saldo -= tarik
            print("Berhasil melakukan tarik tunai, sisa saldo Rp.", self.__jumlah_saldo)

    # Fungsi transfer perlu parameter nominal transfer sekaligus nomor tujuan transfer
    def transfer(self, nominal, tujuan):
        n = 0
        if nominal > self.__jumlah_saldo or nominal == 0:
            print("Jumlah saldo tidak mencukupi untuk melakukan transfer!")
        else :
            for i in range(len(AkunBank.list_pelanggan)):
                if tujuan == AkunBank.list_pelanggan[i].get_no_pelanggan():
                    AkunBank.list_pelanggan[i].tambah_saldo(nominal)
                    print("Berhasil transfer ke", AkunBank.list_pelanggan[i].get_nama(), "sejumlah Rp.", nominal)
                else :
                    n+=1

            if n == len(AkunBank.list_pelanggan):
                print("Nomor tujuan tidak ditemukan!")

    # Jalan keluar untuk fungsi transfer biar saldo target nya nambah
    def tambah_saldo(self, nominal):
        self.__jumlah_saldo += nominal

    # Dapetin atribut nama pelanggan dalam class
    def get_nama(self):
        return self.__nama_pelanggan

    # Dapetin atribut nomor pelanggan dalam class
    def get_no_pelanggan(self):
        return self.__no_pelanggan
    
    # Dapetin atribut saldo pelanggan dalam class
    def get_saldo(self):
        return self.__jumlah_saldo
