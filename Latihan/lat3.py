# modifikasi percobaan 3 untuk menggambar 3/lebih garis
# dengan corak garis yang berbeda-beda.
# tunjukkan pada asisten bagaimana kalian menambahkan garis
# dan mengubah corak garis secara LANGSUNG

import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([4, 4, 2, 1])
# Membuat plot untuk garis y1 dan y2
plt.plot(y1, label='Garis 1')
plt.plot(y2, label='Garis 2')
plt.plot(y3, label='Garis 3 Percobaan')
# Menambahkan judul dan label sumbu
plt.title('Plot Dua Garis') # title memberi judul
plt.xlabel('Nilai x') # label di x
plt.ylabel('Nilai y') # label di y

# Menambahkan keterangan (legend)
plt.legend() #menambahkan keterangan plot
plt.show()