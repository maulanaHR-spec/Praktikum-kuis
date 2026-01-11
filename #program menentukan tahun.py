#program menentukan tahun
tahun = int(input("Masukkan tahun: "))

if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print("Tahun Kabisat")
else:
    print("Bukan Tahun Kabisat")
