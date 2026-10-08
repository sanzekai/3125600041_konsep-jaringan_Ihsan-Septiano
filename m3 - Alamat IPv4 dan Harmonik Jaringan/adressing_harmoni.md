# KONSEP JARINGAN
## Pengalamatan IPv4 & Simulasi Sinyal Harmonik Jaringan

**DOSEN:**  
Dr. Ferry Astika Saputra, ST, M.Sc. (197708232001121002)

**PENYUSUN:**  
Mohammad Ihsan Septiano Firdaus (3125600041)

**PROGRAM STUDI SARJANA TERAPAN TEKNIK INFORMATIKA**  
**POLITEKNIK ELEKTRONIKA NEGERI SURABAYA**

---

## Konversi IP Address dan Konsep Harmonisasi Sampling Jaringan
Dokumen ini merangkum materi teknis mengenai pengalamatan jaringan menggunakan metode *classful* serta prinsip fisik harmonisasi gelombang dan teori sampling dalam transmisi data.

---

### 1. Konversi IP Address (Classful Addressing)

| IP Address | Kelas | Network & Host Part | Range Host / Broadcast |
| :--- | :---: | :--- | :--- |
| **21.26.8.5** | **A** | **Network:** 21.0.0.0<br>**Host:** 0.26.8.5 | **First:** 21.0.0.1<br>**Last:** 21.255.255.254<br>**Broadcast:** 21.255.255.255 |
| **212.6.8.3** | **C** | **Network:** 212.6.8.0<br>**Host:** 0.0.0.3 | **First:** 212.6.8.1<br>**Last:** 212.6.8.254<br>**Broadcast:** 212.6.8.255 |
| **103.24.56.32** | **A** | **Network:** 103.0.0.0<br>**Host:** 0.24.56.32 | **First:** 103.0.0.1<br>**Last:** 103.255.255.254<br>**Broadcast:** 103.255.255.255 |
| **1.1.1.1** | **A** | **Network:** 1.0.0.0<br>**Host:** 0.1.1.1 | **First:** 1.0.0.1<br>**Last:** 1.255.255.254<br>**Broadcast:** 1.255.255.255 |
| **172.31.16.8** | **B** | **Network:** 172.31.0.0<br>**Host:** 0.0.16.8 | **First:** 172.31.0.1<br>**Last:** 172.31.255.254<br>**Broadcast:** 172.31.255.255 |

#### Aturan dan Konsep Batas Pengalamatan
Dalam menentukan batas-batas alamat di atas, digunakan standar perhitungan berikut:
* **Network Address:** Ditentukan dengan menetapkan seluruh bit pada porsi host menjadi 0.
* **First Usable Host:** Alamat pertama yang dapat diberikan kepada perangkat, dihitung dari $\text{Network Address} + 1$.
* **Broadcast Address:** Alamat yang digunakan untuk mengirim data ke seluruh host dalam jaringan, ditentukan dengan menetapkan seluruh bit porsi host menjadi 1 (desimal 255 pada setiap oktet host).
* **Last Usable Host:** Alamat terakhir yang valid untuk perangkat, dihitung dari $\text{Broadcast Address} - 1$.
* **Host Address Part:** Identitas spesifik host di dalam jaringan, didapatkan dengan menolkan porsi network pada alamat IP tersebut.

---

### 2. Harmonisasi Gelombang dan Sampling (Physical Layer)

```python
import matplotlib.pyplot as plt
import numpy as np

# Parameter waktu dan frekuensi
t = np.linspace(0, 2, 1000)
f0 = 1
harmonics = [1, 3, 5, 7, 9, 10]
fs = 25

# Waktu sampling
t_s = np.arange(0, 2, 1/fs)

# Inisialisasi sinyal
s_cont = np.zeros_like(t)
s_disc = np.zeros_like(t_s)

# Penjumlahan gelombang harmonik
for h in harmonics:
    s_cont += (1/h) * np.sin(2 * np.pi * h * f0 * t)
    s_disc += (1/h) * np.sin(2 * np.pi * h * f0 * t_s)

# Plotting sinyal
plt.figure(figsize=(9, 5))
plt.plot(t, s_cont, color="navy", label="Sinyal Kontinu")
plt.stem(t_s, s_disc, linefmt='r-', markerfmt='ro', basefmt='k-', label="Sampling")
plt.xlabel("Waktu (s)")
plt.ylabel("Amplitudo")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()