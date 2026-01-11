#Program yang menampilkan Grade Nilai Plus Keterangan 
nilai = float(input("Masukkan nilai: "))

if nilai >= 85:
    grade = "A"
elif nilai >= 70:
    grade = "B"
elif nilai >= 60:
    grade = "C"
else:
    grade = "D"

if grade in ["A", "B", "C"]:
    keterangan = "Lulus"
else:
    keterangan = "Tidak Lulus"

print("Grade :", grade)
print("Keterangan :", keterangan)
