# modifikasi percobaan 2 untuk menambahkan beberapa variasi
# untuk melengkapi grafik agar lebih informatif dan mudah dipahami
# tunjukkan pada asisten bagaimana kalian menambahkan variasi tertentu
# dan dapat mengubah nya secara LANGSUNG

#pastikan kalian sudah melakukan import library yang dibutuhkan
#sebelum menjalankan kode ini

import matplotlib.pyplot as plt #as itu kita bisa namai bebas tapi panggilnya sesuai nama
import numpy as np

xpoints = np.array([4, 6, 10])
ypoints = np.array([2, 5, 3])

plt.figure(figsize=(2,2)) # figsize ukuran figure (kotakannya)
plt.plot(xpoints, ypoints, color='green') # color ganti warna
plt.xlim([0,15])
plt.ylim([0,15])
plt.show()