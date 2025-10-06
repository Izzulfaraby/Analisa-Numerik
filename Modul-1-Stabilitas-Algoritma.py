# Hasil sebenarnya
H_sebenarnya = 100001.0

# Algoritma A
#step 1: Input nilai awal adalah angka yang paling besar
x_awalA = 100000.0
#Step 2: input nilai selanjutnya adalah angka yang kecil
x_selanjutnnyaA = 0.00001
# Step 3: Melakukan perulangan
for _ in range (100000):
  x_awalA += x_selanjutnnyaA
# Cetak hasil

# Algoritma B
total = 0
#step 1: Input nilai awal adalah angka yang paling kecil
x_awalB  = 0.00001
#Step 2: input nilai selanjutnya adalah angka yang besar
x_selanjutnnyaB = 100000.0
# Step 3: Melakukan perulangan
for _ in range (100000):
  total += x_awalB
total += x_selanjutnnyaB
# Cetak hasil
print ("Hasil sebenarnya            :",H_sebenarnya)
print ("Hasil algoritma A adalah    :",x_awalA)
print ("Hasil algoritma B adalah    :",total)
print ("Galat algoritma A           :",x_awalA-H_sebenarnya)
print ("Galat algoritma B           :",total-H_sebenarnya)
print ("Perbedaan algoritma A dan B  :",x_awalA-total)
