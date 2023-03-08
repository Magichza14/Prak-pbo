class Sepeda:

    def __init__(self):
        # Add attribute
        self.rodaGigi = 1
        self.kecepatan = 0
        self.maxKecepatan = 2
        
    # Method menambahkan roda gigi
    def tambahGigi(self):
        if self.rodaGigi < 4:
            self.rodaGigi += 1
            self.maxKecepatan = self.rodaGigi*2
            print("Berhasil menambah gigi menjadi", self.rodaGigi, ". Kecepatan masimal sekarang", self.maxKecepatan)
        else :
            print("Gigi sudah maksimal, tidak bisa menambah gigi lagi!")
    
    # Method mengurangi roda gigi
    def kurangGigi(self):
        if self.rodaGigi > 1:
            self.rodaGigi -= 1
            self.maxKecepatan = self.rodaGigi*2
            if self.kecepatan > self.maxKecepatan:
                self.kecepatan = self.maxKecepatan
                print("Berhasil mengurangi gigi menjadi", self.rodaGigi, "Kecepatan masimal sekarang", self.maxKecepatan, " dan kecepatan dikurangi menjadi kecepatan maksimal roda gigi saat ini")
            else :
                print("Berhasil mengurangi gigi menjadi", self.rodaGigi, "Kecepatan masimal sekarang", self.maxKecepatan)
        else :
            print("Tidak bisa mengurangi gigi lagi!")

    # Method menambahkan kecepatan
    def tambahKecepatan(self):
        if self.kecepatan < self.maxKecepatan:
            self.kecepatan += 1
            print("Berhasil menambah kecepatan, kecepatan sekarang", self.kecepatan)
        else :
            print("Kecepatan pada roda gigi saat ini sudah maksimal, tidak bisa menambah kecepatan lagi!")

    # Method mengurangi kecepatan 
    def kurangKecepatan(self):
        if self.kecepatan == 0:
            print("Sepedah sudah berhenti, tidak bisa mengurangi kecepatan lagi!")
        else :
            if self.kecepatan > 1:
                self.kecepatan -= 1
                print("Berhasil mengurangi kecepatan menjadi", self.kecepatan)
            else :
                self.kecepatan -= 1
                print("Sepedah berhenti!")

    # Method menampilkan menu dan memanggil method class
    def menuSepeda(self):
        cek = True
        while (cek):
            # Define
            sepedaMenu = ['Tambah gigi', 'Kurang gigi', 'Tambah kecepatan', 'Kurang kecepatan', 'Turun dari sepeda']
        
            for i in range(len(sepedaMenu)):
                print(i+1, sepedaMenu[i])
        
            pilih = int(input("Pilih menu[1/2/3/4/5]: "))
            
            if (pilih == 1):
                self.tambahGigi()
            elif (pilih == 2):
                self.kurangGigi()
            elif (pilih == 3):
                self.tambahKecepatan()
            elif (pilih == 4):
                self.kurangKecepatan()
            elif (pilih == 5):
                cek = False
            else :
                print("Menu tidak tersedia!")
