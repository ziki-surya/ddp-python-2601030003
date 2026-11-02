nama_barang = input("Nama barang: ")
harga = float(input("Harga satuan: "))
jumlah = int(input("Jumlah barang: "))

subtotal = harga * jumlah
ppn = subtotal * 0.11
total = subtotal + ppn

print(f"Barang   : {nama_barang}")
print(f"Subtotal : {subtotal:.0f}")
print(f"PPN 11%  : {ppn}")
print(f"Total    : {total}")