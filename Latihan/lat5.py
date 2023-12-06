# Import library yang dibutuhkan
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Cara membuat sample data dengan distribusi normal
sample = np.random.normal(loc=50, scale=5, size=1000)

# Menampilkan sample dalam bentuk histogram
plt.figure(figsize=(5, 4))  # Membuat figure dengan ukuran 5x4 inci
plt.hist(sample, bins=10, density=True)  # Membuat histogram dengan 10 bins dan normalisasi density

# Menghitung rata-rata dan standar deviasi dari sampel
sample_mean = np.mean(sample)
sample_std = np.std(sample)
print('Mean=%.3f \nStandard Deviation=%.3f' % (sample_mean, sample_std))

# Mendefinisikan distribusi normal dengan mean dan std dari sampel
dist = norm(sample_mean, sample_std)

# Menentukan nilai-nilai dan probabilitas distribusi
values = [value for value in range(30, 70)]  # Menggunakan list comprehension untuk membuat list nilai
probabilities = [dist.pdf(value) for value in values]  # Menghitung probabilitas distribusi normal pada setiap nilai

# Menampilkan histogram sampel dan distribusi probabilitas
plt.hist(sample, bins=10, density=True, color='blue')  # Menampilkan histogram sampel
plt.plot(values, probabilities, label='Distribusi Normal', color='red')  # Menampilkan kurva distribusi normal
plt.legend()  # Menampilkan legenda
plt.show()  # Menampilkan plot keseluruhan