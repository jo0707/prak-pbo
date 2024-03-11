class Dagangan:
    jumlah_barang = 0
    list_barang = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        Dagangan.jumlah_barang += 1
        Dagangan.list_barang.append((self.__nama, self.__stok, self.__harga))

    def __del__(self):
        Dagangan.jumlah_barang -= 1
        Dagangan.list_barang.remove((self.__nama, self.__stok, self.__harga))
        print(self.__nama, "dihapus dari toko!")

    @classmethod
    def lihat_barang(cls):
        print("Jumlah barang dagangan pada toko:", cls.jumlah_barang, "buah")
        for i in range(cls.jumlah_barang):
            print(i+1, cls.list_barang[i][0], "seharga Rp", cls.list_barang[i][2], "(stok:", cls.list_barang[i][1], ")")
            
Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)

Dagangan.lihat_barang()
del Dagangan1
Dagangan.lihat_barang()