# Nilai sebenarnya
N_sebenarnya = 100001.0

# Algoritma 1
#step 1: Input nilai awal adalah angka yang paling besar
x_awal1 = 100000.0
#Step 2: input nilai selanjutnya adalah angka yang kecil
x_selanjutnnya1 = 0.00001
# Step 3: Melakukan perulangan
for _ in range (100000):
  x_awal1 += x_selanjutnnya1
# Cetak hasil

# Algoritma 2
total = 0
#step 1: Input nilai awal adalah angka yang paling kecil
x_awal2  = 0.00001
#Step 2: input nilai selanjutnya adalah angka yang besar
x_selanjutnnya2 = 100000.0
# Step 3: Melakukan perulangan
for _ in range (100000):
  total += x_awal2
total += x_selanjutnnya2
# Cetak hasil
print ("Nilai yang sebenarnya       :",N_sebenarnya)
print ("Hasil algoritma 1 adalah    :",x_awal1)
print ("Hasil algoritma 2 adalah    :",total)
print ("Galat Algoritma 1           :",x_awal1-N_sebenarnya)
print ("Galat Algoritma 2           :",total-N_sebenarnya)
print ("Perbedaan 1 dan 2           :",x_awal1-total)
