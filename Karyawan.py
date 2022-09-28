class Karyawan :
    _jenisKelamin = None
    _upahPerHari = None

    def __init__(self, nama, umur):
        self._nama = nama
        self._umur = umur

    def getNama(self):
        return self._nama
    
    def getUmur(self):
        return self._umur
    
    def getJenisKelamin(self):
        return self._jenisKelamin

    def getUpahPerHari(self):
        return self._upahPerHari
    
    def setNama(self,nama):
        self._nama = nama
    
    def setUmur(self,umur):
        self._umur = umur

    def setJenisKelamin(self,jk):
        self._jenisKelamin = jk

    def setUpahPerHari(self, upahPerHari):
        self._upahPerHari = upahPerHari

    def hitungGajiBulanan(self,hari):
        if self.getUpahPerHari() == None:
            print("ERROR! Upah per Hari belum di Inputkan")
        else:
            print(f"Gaji Bulan Ini : {self.getUpahPerHari() * hari}")

    def printInfo(self):
        print("="*9," INFO ", "="*9)
        print(f"Nama            : {self.getNama()}")
        print(f"Umur            : {self.getUmur()}")
        print(f"Jenis Kelamin   : {self.getJenisKelamin()}")
        print(f"Upah per Hari   : {self.getUpahPerHari()}")


nama = Karyawan("Haniif", 90)
nama.printInfo()

nama2 = Karyawan("Sindu", 190)
nama2.setJenisKelamin("Laki - Laki")
nama2.setUpahPerHari(30000)
nama2.printInfo()

nama.hitungGajiBulanan(28)
nama2.hitungGajiBulanan(30)