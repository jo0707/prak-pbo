bawah = int(input("Batas bawah : "))
atas = int(input("Batas atas : "))

if bawah < 0 or atas < 0:
    print("Batas bawah dan atas yang dimasukkan tidak boleh di bawah nol")
    exit()

print(f"Total : {sum([number if number % 2 != 0 else 0 for number in range(bawah, atas+1)])}")
