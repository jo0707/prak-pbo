class Hewan:
    def __init__(self, nama, jenis_kelamin):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin

    def bersuara(self):
        pass

    def makan(self):
        pass

    def minum(self):
        pass
    
class Kucing(Hewan):
    def bersuara(self):
        print("Kucing", self.nama, "bersuara: Meong!")
    
    def makan(self):
        print("Kucing", self.nama, "sedang makan: tulang")
        
class Anjing(Hewan):
    def bersuara(self):
        print("Anjing", self.nama, "bersuara: Guk Guk!")
    
    def makan(self):
        print("Anjing", self.nama, "sedang makan: tulang")
        
hewan1 = Kucing("Kiki", "Betina")
hewan2 = Anjing("Ichi", "Jantan")
print(hewan1.nama)
print(hewan2.nama)
hewan1.bersuara()
hewan1.makan()
hewan2.bersuara()
hewan2.makan()