import matplotlib.pyplot as plt
import numpy as np

data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

# TODO 1: Ekstrak harga produk dan jumlah produk terjual untuk visualisasi pertama
harga_produk, jumlah_terjual = zip(*map(lambda x: (x[1], x[2]), data_transaksi))

# TODO 2: Buat scatter plot untuk hubungan antara harga produk dan jumlah produk terjual
plt.figure(figsize=(10, 6))
plt.scatter(harga_produk, jumlah_terjual, color='blue', marker='o')
plt.title('Hubungan Harga dan Jumlah Terjual')
plt.xlabel('Harga Produk')
plt.ylabel('Jumlah Terjual')

# TODO 3: Hitung total pendapatan untuk setiap produk
total_pendapatan = list(map(lambda x: x[1] * x[2], data_transaksi))

# TODO 4: Tambahkan bar chart untuk menyajikan pendapatan produk
fig, ax = plt.subplots(figsize=(10, 6))
bar_positions = np.arange(len(data_transaksi))
bar_width = 0.5

ax.bar(bar_positions, total_pendapatan, color='green', edgecolor='black', linewidth=1.2, width=bar_width)
ax.set_xticks(bar_positions)
ax.set_xticklabels(map(lambda x: x[0], data_transaksi), rotation=45, ha='right', fontsize=10)
ax.set_title('Pendapatan Produk')
ax.set_xlabel('Produk')
ax.set_ylabel('Pendapatan')

plt.tight_layout()
plt.show()
