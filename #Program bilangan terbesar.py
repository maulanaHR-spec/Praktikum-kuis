#Program bilangan terbesar
a = float(input("Masukan bilangan pertama : "))
b = float(input("Masukan bilangan kedua : "))
c = float(input("Masukan bilangan ketiga : "))

if a >= b and a >= c:
    terbesar = a
elif b >= a and b >= c:
    terbesar = b
else:
    terbesar = c

print("Bilangan terbesar adalah :", terbesar)
