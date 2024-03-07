
class Anjing:
    # comstructor
    def __init__(self, nama, jenis, umur):
        self.nama = nama
        self.jenis = jenis
        self.umur = umur
        print("Constructor : Hewan baru telah lahir")
    
    # desctructor
    def __del__(self):
        print("Destructor : Hewan telah mati")
    
    @property
    def getNama(self):
        return self.nama
    
    @property
    def getJenis(self):
        return self.jenis
    
    @property
    def getUmur(self):
        return self.umur
    
    @getNama.setter
    def setNama(self, nama):
        self.nama = nama
    
    @getJenis.setter
    def setJenis(self, jenis):
        self.jenis = jenis
    
    @getUmur.setter
    def setUmur(self, umur):
        self.umur = umur
        
bino = Anjing("Bino", "Golden Retriever", 3)
print(bino.getNama)

bino.setNama = "Bino2"
print(bino.getNama)

del bino

try:
    print(bino.getNama)
except:
    print("Error, karena bino sudah tidak terdefinisi lagi")