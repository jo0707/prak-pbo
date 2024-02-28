r = int(input("Jari-jari : "))

if r < 0:
    print("Jari-jari yang dimasukkan tidak boleh di bawah nol")
    exit()

print(f"Luas : {3.14 * r ** 2}")
print(f"Keliling : {2 * 3.14 * r}")
