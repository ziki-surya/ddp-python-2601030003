panjang = float(input("Masukkan panjang (m): "))
lebar = float(input("Masukkan lebar (m): "))

luas = panjang * lebar
keliling = 2 * (panjang + lebar)

print(f"Luas     : {luas} m2")
print(f"Keliling : {keliling} m")

# Trace table (contoh input panjang = 8, lebar = 5)
# | Langkah | panjang | lebar | luas | keliling |
# |---------|---------|-------|------|----------|
# | 1       | 8.0     | -     | -    | -        |
# | 2       | 8.0     | 5.0   | -    | -        |
# | 3       | 8.0     | 5.0   | 40.0 | -        |
# | 4       | 8.0     | 5.0   | 40.0 | 26.0     |
# | 5       | output = luas 40.0 dan keliling = 26.0