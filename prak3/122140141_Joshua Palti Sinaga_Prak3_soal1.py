class Mobil:
    def __init__(self):
        self.__bensin = 0
        self.__odometer = 0

    def isi_bensin(self):
        self.__bensin = 60

    def mengendarai(self, kilometer):
        if self.__bensin - kilometer >= 0:
            self.__bensin -= kilometer
            self.__odometer += kilometer
        else:
            self.__odometer += self.__bensin
            self.__bensin = 0

    def lihat_info(self):
        print("Odometer berada pada angka", self.__odometer, "km, bensin yang tersisa", self.__bensin, "liter")
        
mobil = Mobil()
mobil.lihat_info()
mobil.isi_bensin()
mobil.lihat_info()
mobil.mengendarai(20)
mobil.lihat_info()
mobil.mengendarai(50)
mobil.lihat_info()
mobil.mengendarai(10)
mobil.lihat_info()
mobil.isi_bensin()
mobil.isi_bensin()
mobil.lihat_info()

