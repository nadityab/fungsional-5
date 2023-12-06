import matplotlib.pyplot as plt
import numpy as np
from functools import reduce

# Data nilai-nilai ujian mahasiswa
nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]

# Menghitung rata-rata menggunakan fungsi reduce
rata_rata = reduce(lambda x, y: x + y, nilai_mahasiswa) / len(nilai_mahasiswa)

# Membuat label mahasiswa (sumbu x) dalam bentuk fungsional dinamis (list-map-lambda)
label_mahasiswa = [f'Mahasiswa-{i + 1}' for i in range(len(nilai_mahasiswa))]

# Visualisasi data dalam bentuk diagram batang dengan jarak yang lebih besar
fig, ax = plt.subplots(figsize=(12, 6))  # Menentukan ukuran figur dan sumbu
bar_width = 0.5  # Lebar batang diagram
bar_positions = np.arange(len(nilai_mahasiswa))

ax.bar(bar_positions, nilai_mahasiswa, color='skyblue', edgecolor='black', linewidth=1.2, width=bar_width)
ax.set_xticks(bar_positions)
ax.set_xticklabels(label_mahasiswa, rotation=45, ha='right', fontsize=10)

ax.set_xlabel('Mahasiswa', fontsize=12)
ax.set_ylabel('Nilai Ujian', fontsize=12)
ax.set_title('Diagram Batang Nilai Ujian Mahasiswa', fontsize=16)
ax.axhline(y=rata_rata, color='red', linestyle='--', label=f'Rata-rata: {rata_rata:.2f}')
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()  # Menata layout agar lebih rapi
plt.show()
