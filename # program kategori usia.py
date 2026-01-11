usia = int(input("Masukkan usia: "))

if usia < 13:
    print("Anak-anak")
elif usia <= 17:
    print("Remaja")
elif usia <= 59:
    print("Dewasa")
else:
    print("Lansia")
