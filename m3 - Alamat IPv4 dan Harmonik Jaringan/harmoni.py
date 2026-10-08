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