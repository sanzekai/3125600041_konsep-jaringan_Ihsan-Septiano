# TUGAS 5: ANALISIS CARA KERJA TRACEROUTE & MEKANISME TTL

## 1. Mekanisme Time To Live (TTL)
Time To Live (TTL) adalah nilai pada header paket IPv4 (atau *Hop Limit* pada IPv6) yang berfungsi mencegah paket berputar tanpa henti (*looping*) di dalam jaringan.

### Cara Kerja TTL:
* **Inisialisasi:** Pengirim menetapkan nilai awal TTL pada paket (misalnya 64, 128, atau 255).
* **Dekremen (Pengurangan):** Setiap kali paket melewati sebuah router (*hop*), router mengurangi nilai TTL sebesar 1.
* **Drop & ICMP Error:** Jika nilai TTL mencapai 0 sebelum tiba di tujuan, router akan membuang paket tersebut dan mengirimkan pesan balik ke pengirim berupa **ICMP Time Exceeded (Type 11, Code 0)**.

---

## 2. Cara Kerja Perintah Traceroute
Traceroute memanfaatkan mekanisme penurunan nilai TTL dan pesan balik ICMP Error untuk memetakan setiap router (*hop*) di sepanjang jalur menuju alamat tujuan.

### Langkah-langkah Kerja Traceroute:
1. **Hop Pertama (TTL = 1):**
   * Traceroute mengirim paket pertama (ICMP Echo Request atau UDP probe) dengan nilai **TTL = 1**.
   * Router pertama menerima paket, mengurangi TTL menjadi 0, membuang paket, dan mengirimkan pesan balik **ICMP Time Exceeded** ke pengirim.
   * Pengirim mencatat alamat IP router pertama dan waktu tempuhnya (*Round Trip Time / RTT*).

2. **Hop Berikutnya (TTL = 2, 3, ...):**
   * Traceroute mengirim paket berikutnya dengan nilai **TTL = 2**. Router pertama meneruskannya (TTL menjadi 1), dan router kedua membuang paket tersebut (TTL menjadi 0) lalu membalas dengan **ICMP Time Exceeded**.
   * Proses ini diulang secara sekuensial dengan menaikkan nilai TTL secara bertahap ($TTL = n+1$).

3. **Mencapai Tujuan:**
   * Saat paket mencapai komputer/server tujuan, paket tidak dibuang karena TTL.
   * Jika menggunakan **UDP Probe** (default Linux/macOS), traceroute menggunakan port tujuan acak bernilai tinggi (misal: 33434). Server tujuan akan membalas dengan **ICMP Port Unreachable (Type 3, Code 3)** karena tidak ada layanan di port tersebut.
   * Jika menggunakan **ICMP Echo** (default `tracert` Windows), server tujuan membalas dengan **ICMP Echo Reply (Type 0, Code 0)**.
   * Penerimaan balasan akhir ini menandakan proses traceroute telah selesai.

---

## 3. Kesimpulan Indikator Output Traceroute
* **Angka Hop (1, 2, 3, ...):** Urutan router yang dilewati dari asal ke tujuan.
* **Waktu (ms):** Latensi RTT pengiriman paket ke router tersebut (biasanya diukur 3 kali per hop).
* **Simbol `*` (Asterisk / Request Timed Out):** Menandakan router terkait dibentengi firewall yang memblokir paket ICMP/UDP atau tidak mengirimkan balasan ICMP Time Exceeded.