
class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa


    def getNim(self):
        return self.__nim
    
    def getNama(self):
        return self.__nama
    
    def setNim(self, nim):
        self.__nim = nim
        
    def setNama(self, nama):
        self.__nama = nama

    # custom method 
    def getNimNama(self):
        return f"NIM : {self.__nim}, Nama : {self.__nama}"

    def getAngkatanIsMahasiswa(self):
        return f"Angkatan : {self.angkatan}, Mahasiswa : {self.isMahasiswa}"

    def getNimNamaAngkatan(self):
        return f"NIM : {self.__nim}, Nama : {self.__nama}, Angkatan : {self.angkatan}"
    
josh = Mahasiswa(122140142, "Joshua", 2014, False)
rika = Mahasiswa(122140141, "Rika", 2014)

print(josh.getNimNama())
print(rika.getNimNama())

print(josh.getAngkatanIsMahasiswa())
print(rika.getAngkatanIsMahasiswa())

print(josh.getNimNamaAngkatan())
print(rika.getNimNamaAngkatan())