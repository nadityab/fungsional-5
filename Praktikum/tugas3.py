import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Data tinggi badan individu dalam sentimeter
tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10  # Misalnya interval ukuran per 10 sentimeter

# TODO 1: Fungsi untuk mengelompokkan tinggi badan ke dalam interval tertentu
def kelompokkan_ke_interval(data, interval_size):
    bins = np.arange(min(data), max(data) + interval_size, interval_size)
    return bins

# TODO 2: Menghitung frekuensi tinggi badan dalam interval
def hitung_frekuensi(data, bins):
    return np.histogram(data, bins=bins)[0]

# TODO 3: Visualisasi data dalam bentuk histogram
def visualisasi_histogram(data, bins):
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, edgecolor='black', alpha=0.7)
    plt.title('Histogram Tinggi Badan')
    plt.xlabel('Tinggi Badan (cm)')
    plt.ylabel('Frekuensi')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# TODO 4: Menambahkan kurva pdf pada hasil visualisasi data
def visualisasi_histogram_dan_pdf(data, bins):
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, density=True, edgecolor='black', alpha=0.7, label='Histogram')
    
    mean, std_dev = np.mean(data), np.std(data)
    x = np.linspace(min(data), max(data), 100)
    plt.plot(x, norm.pdf(x, mean, std_dev), label='PDF (Normal Distribution)', color='red', linewidth=2)

    plt.title('Histogram Frekuensi Tinggi Badan')
    plt.xlabel('Tinggi Badan (cm)')
    plt.ylabel('Frekuensi')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Mengelompokkan tinggi badan ke dalam interval
bins = kelompokkan_ke_interval(tinggi_badan, interval_size)

# Menghitung frekuensi tinggi badan dalam interval
frekuensi = hitung_frekuensi(tinggi_badan, bins)

# Visualisasi data dalam bentuk histogram
visualisasi_histogram(tinggi_badan, bins)

# Menambahkan kurva pdf pada hasil visualisasi data
visualisasi_histogram_dan_pdf(tinggi_badan, bins)
