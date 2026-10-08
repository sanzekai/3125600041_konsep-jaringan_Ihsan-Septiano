# KONSEP JARINGAN
## Latihan Konsep Dasar Jaringan Komputer

**DOSEN:**  
Dr. Ferry Astika Saputra, ST, M.Sc. (197708232001121002)

**PENYUSUN:**  
Mohammad Ihsan Septiano Firdaus (3125600041)

**PROGRAM STUDI SARJANA TERAPAN TEKNIK INFORMATIKA**  
**POLITEKNIK ELEKTRONIKA NEGERI SURABAYA**

---

## Level A

### 1. Pengertian Jaringan Komputer & 4 Unsur Pokok
Jaringan komputer adalah sekumpulan perangkat otonom yang saling terhubung untuk berbagi data dan sumber daya.
* **Node (Perangkat):** Komputer, server, printer, atau gawai pintar.
* **Media Transmisi:** Jalur fisik/nirkabel (kabel UTP, serat optik, radio Wi-Fi).
* **Protokol:** Aturan atau bahasa komunikasi yang disepakati bersama (misal: TCP/IP).
* **Layanan/Sumber Daya:** Hal yang dibagikan (berkas, printer, koneksi internet, aplikasi).

### 2. Perangkat Otonom dalam Jaringan
Perangkat yang memiliki kemampuan pemrosesan dan sistem operasi mandiri. Perangkat tersebut dapat bekerja sendiri tanpa harus dikendalikan secara mutlak oleh komputer pusat (bukan sekadar layar monitor pasif atau terminal bodoh).

### 3. Perbedaan Data, Sinyal, dan Paket
* **Data:** Informasi atau representasi biner mentah pada level aplikasi (misal: teks, gambar, berkas).
* **Paket:** Potongan data yang telah dibungkus dengan informasi kontrol (header IP, alamat sumber, dan tujuan) untuk dikirim melintasi jaringan.
* **Sinyal:** Gelombang fisik (listrik, cahaya, atau radio) yang membawa representasi bit melewati media transmisi.

### 4. Perbedaan PAN, LAN, MAN, dan WAN (Non-Jarak)

| Jenis | Kepemilikan & Administrasi | Infrastruktur & Media |
| :--- | :--- | :--- |
| **PAN** | Perorangan (personal) | Bluetooth, USB, kabel personal |
| **LAN** | Satu entitas tunggal (kampus, kantor, rumah) | Kabel privat (Ethernet) atau Wi-Fi internal |
| **MAN** | Konsorsium lokal / pemerintah kota / penyedia regional | Jaringan serat optik metro kota |
| **WAN** | Multi-organisasi lintas batas negara | Menggunakan sirkuit sewa pihak ketiga / ISP global |

### 5. Perbedaan Intranet, Ekstranet, dan Internet Publik
* **Intranet:** Jaringan privat yang hanya dapat diakses oleh anggota internal organisasi.
* **Ekstranet:** Jaringan privat yang diperluas secara terbatas untuk pihak luar tepercaya (mitra, vendor, klien).
* **Internet Publik:** Jaringan global terbuka yang menghubungkan semua jaringan di dunia tanpa batasan keanggotaan.

### 6. Wi-Fi vs Internet
* **Wi-Fi:** Standar teknologi nirkabel (IEEE 802.11) untuk menghubungkan perangkat ke jaringan lokal tanpa kabel (Layer 1 dan 2).
* **Internet:** Jaringan global interkoneksi di seluruh dunia (Layer 3 ke atas).

*Kesimpulan:* Wi-Fi hanya media penghubung lokal; laptop bisa terhubung ke Wi-Fi meski jaringan tersebut tidak terhubung ke Internet.

### 7. Perbedaan Client, Server, dan Peer
* **Client:** Perangkat yang meminta dan menggunakan layanan.
* **Server:** Perangkat terdedikasi yang melayani dan menyediakan sumber daya.
* **Peer:** Perangkat yang setara; dapat bertindak sebagai client sekaligus server pada waktu bersamaan.

### 8. Perbedaan Bandwidth, Throughput, dan Goodput
* **Bandwidth:** Kapasitas maksimal teoritis dari suatu jalur transmisi data.
* **Throughput:** Jumlah data aktual yang berhasil terkirim melewati media dalam waktu tertentu (termasuk header protokol dan data transmisi ulang).
* **Goodput:** Jumlah data bersih aplikasi (payload berguna) yang berhasil sampai ke tujuan tanpa menghitung overhead header dan paket retransmisi.

### 9. Empat Komponen Nodal Delay
* **Processing Delay:** Waktu router memeriksa header paket dan memverifikasi integritas bit.
* **Queuing Delay:** Waktu paket mengantre di buffer sebelum diproses/ditransmisikan.
* **Transmission Delay:** Waktu untuk mendorong semua bit paket ke media (panjang paket dibagi bandwidth).
* **Propagation Delay:** Waktu tempuh sinyal fisik melintasi media dari titik asal ke tujuan (jarak dibagi kecepatan rambat).

### 10. Web vs Internet
* **Internet:** Infrastruktur fisik dan sistem jaringan komputer global yang saling terhubung (jalan raya).
* **Web (World Wide Web):** Layanan/aplikasi sistem dokumen multimedia (HTTP/HTTPS) yang berjalan di atas infrastruktur Internet (salah satu jenis kendaraan di jalan raya). Layanan lain di Internet meliputi email (SMTP), transfer file (FTP), dan remote login (SSH).

---

## Level B

### 1. Perhitungan Transmission Delay dan Delay Lainnya
* **Ukuran paket ($L$):** $1.000\text{ byte} = 8.000\text{ bit}$
* **Kecepatan link ($R$):** $10\text{ Mbps} = 10.000.000\text{ bps}$
* **Rumus:** $d_{\text{trans}} = \frac{L}{R} = \frac{8.000}{10.000.000} = 0,0008\text{ detik} = 0.8\text{ milidetik (ms)}$

**Komponen delay lain yang belum dihitung:**
* **Processing delay:** Waktu router memeriksa header dan mencari rute.
* **Queuing delay:** Waktu paket menunggu giliran di antrean router.
* **Propagation delay:** Waktu tempuh sinyal fisik melewati kabel atau udara dari titik awal ke tujuan.

### 2. Lima Kemungkinan Penyebab Internet Lambat di Satu Lantai Kampus
1. **Masalah Wi-Fi:** Terlalu banyak orang terhubung ke satu Access Point (AP) atau saluran frekuensinya bertabrakan dengan AP lain.
2. **Kabel LAN bermasalah:** Kabel penghubung antar-switch terjepit atau konektornya longgar, sehingga kecepatannya turun otomatis dari 1 Gbps ke 100 Mbps.
3. **Pembatasan kuota/kecepatan:** Konfigurasi bandwidth per port atau per VLAN di lantai tersebut dibatasi terlalu kecil oleh admin jaringan.
4. **Switch lantai kelebihan beban:** Switch mengalami hang atau memorinya penuh karena ada komputer yang terkena virus dan mengirim broadcast terus-menerus.
5. **DNS internal lambat:** Server DNS kampus lambat merespons alamat website, sehingga pengguna merasa koneksinya lambat padahal jalurnya normal.

### 3. Perbandingan Kebutuhan: Backup File vs Video Call

| Kebutuhan | Backup File | Video Call |
| :--- | :--- | :--- |
| **Kehilangan Paket (Packet Loss)** | Tidak boleh hilang sama sekali (pakai TCP). | Boleh hilang sedikit, gambar/suara patah sebentar tidak masalah (pakai UDP). |
| **Sensitivitas Jeda (Delay/Jitter)** | Tidak masalah jika jedanya tidak stabil. | Sangat sensitif, jeda sedikit saja membuat suara saling tabrakan. |
| **Metrik Paling Penting** | Bandwidth/Throughput tinggi agar cepat selesai. | Delay dan Jitter rendah agar komunikasi lancar tanpa jeda. |

### 4. Analisis Dua ISP Lewat Tiang dan Saluran yang Sama
* **Kelebihan:** Ada cadangan sistem. Jika ISP pertama mengalami gangguan server atau rute, koneksi bisa dialihkan ke ISP kedua.
* **Kekurangan fatal:** Tidak ada redundansi fisik. Karena kabel kedua ISP berada di tiang atau pipa gorong-gorong yang sama, jika tiang roboh atau jalurnya terputus galian jalan, kedua koneksi akan putus secara bersamaan.

### 5. Alasan Menambah Bandwidth Tidak Mengurangi Waktu Akses Server Jauh
* Bandwidth hanya menentukan seberapa banyak data yang bisa dikirim bersamaan, bukan kecepatan jalannya sinyal.
* Waktu akses (latensi/ping) ke server yang jauh ditentukan oleh jarak fisik dan kecepatan rambat cahaya di kabel serat optik.
* Berapa pun besarnya bandwidth yang dibeli, sinyal tetap butuh waktu fisik untuk bolak-balik melintasi jarak ribuan kilometer.

### 6. Perhitungan Batas Maksimal Layanan Mati (Downtime) per Tahun
Total menit dalam 1 tahun (365 hari) = $525.600\text{ menit}$.

* **Ketersediaan $99,9\%$:**  
  $\text{Waktu mati} = 0,1\% \times 525.600\text{ menit} = 525,6\text{ menit}$ (sekitar 8 jam 45 menit per tahun).
* **Ketersediaan $99,99\%$:**  
  $\text{Waktu mati} = 0,01\% \times 525.600\text{ menit} = 52,56\text{ menit}$ (sekitar 52 menit per tahun).

### 7. Distribusi File Besar: Client-Server vs P2P
* **Client-Server:**
  * *Kelebihan:* Pengaturan hak akses mudah dan file dijamin asli dari satu sumber resmi.
  * *Kekurangan:* Beban server sangat berat. Jika ribuan orang mengunduh bersamaan, server bisa down dan biaya bandwidth membengkak.
* **Peer-to-Peer (P2P):**
  * *Kelebihan:* Semakin banyak orang yang mengunduh, download justru bisa makin cepat karena pengguna saling berbagi potongan file.
  * *Kekurangan:* Sulit mengatur keamanan file dan memakai bandwidth upload milik pengguna.

### 8. Contoh Topologi Fisik dan Logis yang Berbeda
**Di Ruang Lab Komputer:**
* **Topologi Fisik:** Star (Bintang). Semua kabel dari komputer ditancapkan ke satu switch di pojok ruangan.
* **Topologi Logis:** Jaringan tersebut bekerja seperti Bus. Saat satu komputer mengirim pesan broadcast, switch akan menyebarkannya ke seluruh komputer lain di lab tersebut.

**Contoh Lain (VLAN):** Dua komputer duduk bersebelahan dan dicolok ke switch yang sama, tetapi secara logis dipisah VLAN sehingga tidak bisa saling kirim data tanpa lewat router.

---

## Level C (Tambahan)

### 1. Klasifikasi Kebutuhan Jaringan Kampus & Segmentasi
* **Rancangan Segmentasi:**
  * **Mahasiswa & Tamu:** VLAN terpisah, *bandwidth throttle*, hanya akses internet publik.
  * **Staf Administrasi:** VLAN privat + autentikasi 802.1X, akses terbatas ke server data kampus.
  * **Kamera Pengawas (CCTV):** VLAN terisolasi tanpa akses internet, hanya terhubung ke NVR.
  * **Laboratorium Riset:** VLAN dedicated dengan firewall internal untuk transmisi data intensif.
* **Alasan & Aturan Utama:** Menerapkan prinsip *Least Privilege* dan mengisolasi domain *broadcast* guna mencegah akses tak berizin serta membatasi penyebaran malware (*lateral movement*).

### 2. Evaluasi Enkripsi Jaringan Internal (CIA Triad)
Pernyataan *“Jaringan internal tidak memerlukan enkripsi karena sudah dilindungi firewall”* adalah **SALAH**.
* **Kerahasiaan (Confidentiality):** Firewall tidak melindungi data dari *eavesdropping/sniffing* oleh ancaman internal (karyawan/malware di dalam LAN).
* **Integritas (Integrity):** Tanpa enkripsi (seperti TLS/IPsec), paket data internal dapat diubah melalui serangan *Man-in-the-Middle* (MitM).
* **Ketersediaan (Availability):** Firewall tidak mencegah serangan Layer 2 seperti *ARP Spoofing* yang dapat memutus konektivitas internal.

### 3. Perkembangan Internet Tanpa Otoritas Terpusat
* **Mengapa Terjadi:** Internet berkembang berbasis standar terbuka (*open standards*) yang dirancang oleh konsorsium independen (IETF, ICANN, W3C) serta model kedaulatan *Autonomous System* (BGP) yang terdesentralisasi.
* **Manfaat:** Inovasi sangat cepat, skalabilitas tinggi, tidak ada *single point of failure*, dan bebas dari kontrol tunggal negara tertentu.
* **Risiko:** Fragmentasi regulasi, kesulitan dalam penegakan hukum siber lintas negara, serta kerentanan keamanan infrastruktur dasar seperti *BGP Hijacking*.

### 4. Circuit Switching vs Packet Switching untuk Layanan Suara
* **Perbandingan:** *Circuit switching* menyediakan jalur komunikasi terdedikasi (*guaranteed bandwidth* & latensi tetap) tetapi tidak efisien. *Packet switching* memecah data menjadi paket-paket independen yang berbagi jalur bersama.
* **Mengapa Suara Modern Dapat Berjalan pada Jaringan Paket:**
  * Adanya mekanisme *Quality of Service* (QoS) untuk memprioritaskan paket suara (*DiffServ/CoS*).
  * Penggunaan buffer *anti-jitter* dan *codec* adaptif untuk mengatasi variasi delay serta *packet loss*.

### 5. Prosedur Troubleshooting "Internet Lambat"
* **Pengumpulan Bukti:** Kumpulkan nilai latensi RTT, *packet loss*, *throughput* aktual, serta tangkapan layar *traceroute* dan log pengujian koneksi.
* **Pengujian Hipotesis:** Uji koneksi kabel LAN langsung vs Wi-Fi. Jika LAN normal namun Wi-Fi lambat, hipotesis awal dipfokuskan pada korupsi sinyal RF, ko-interferensi saluran, atau kepadatan pengguna pada Access Point.
* **Kriteria Keberhasilan:** Latensi RTT lokal $<10\text{ ms}$, *packet loss* $0\%$, dan *throughput* rata-rata memenuhi minimum $90\%$ dari batas *bandwidth* berlangganan.

### 6. Statistik Pengukuran IPv6 Indonesia
* **Pengukuran Google vs APNIC:** APNIC mengukur ketersediaan/kemampuan IPv6 dari perspektif *pemasangan iklan rute* & sampel kueri DNS di tingkat AS/negara, sedangkan Google mengukur persentase trafik pengguna yang secara aktif mengakses layanan Google menggunakan IPv6.
* **Penyebab Perbedaan:** Adanya perbedaan pada populasi sampel, cakupan domain pengguna, dan kriteria trafik yang dihitung oleh masing-masing penyedia statistik.

### 7. Analisis Satelit Orbit Rendah (LEO) untuk Kampus Terpencil
* **Kinerja:** Latensi jauh lebih rendah ($20\text{–}50\text{ ms}$) dibanding satelit GEO ($>500\text{ ms}$), sangat layak untuk aktivitas akademis real-time.
* **Biaya:** Biaya perangkat keras terminal dan langganan lebih tinggi dibandingkan kabel fiber optik darat (jika tersedia), namun jauh lebih murah daripada pembentangan fiber optik baru ke area terpencil.
* **Cuaca, Pengelolaan, & Keamanan:** Sensitif terhadap hujan lebat (*rain fade*), pengelolaan perangkat relatif mudah (*plug-and-play*), namun memerlukan enkripsi tambahan (VPN/IPsec) untuk mengamankan komunikasi nirkabel jarak jauh.

### 8. Otomatisasi Jaringan: Konsistensi vs Risiko
* **Dampak:** Otomatisasi menjamin konsistensi konfigurasi pada ratusan perangkat sekaligus, namun kesalahan kecil pada skrip dapat berdampak sistemik (*network-wide outage*).
* **Kontrol Teknis & Proses:**
  * **Teknis:** Linting skrip, pengujian *dry-run*, pengujian otomatis pada lingkungan *staging/digital twin*, serta sistem *automated rollback*.
  * **Proses:** Terapkan pipeline CI/CD, mekanisme *peer code review*, dan penyebaran bertahap (*canary deployment*).

---

# TUGAS TEORI PERTEMUAN 2

**DOSEN:**  
Dr. Ferry Astika Saputra, ST, M.Sc. (197708232001121002)

**PENYUSUN:**  
Mohammad Ihsan Septiano Firdaus (3125600041)

**PROGRAM STUDI SARJANA TERAPAN TEKNIK INFORMATIKA**  
**POLITEKNIK ELEKTRONIKA NEGERI SURABAYA**

---

### 1. Tabel Kategori Kabel UTP/STP (Cat 1 - Cat 9)
Kabel tembaga pilin diklasifikasikan ke dalam berbagai kategori oleh TIA/EIA dan ISO/IEC berdasarkan batas frekuensi kerja, transmisi data, dan konstruksi perlindungannya (UTP tanpa pelindung atau STP/FTP dengan lapisan pelindung foil/anyaman logam).

| Kategori | Bandwidth Maksimal | Kecepatan Maksimal | Panjang Efektif | Penerapan dan Catatan Teknis |
| :--- | :--- | :--- | :--- | :--- |
| **Cat 1** | $< 1\text{ MHz}$ | $\le 1\text{ Mbps}$ | Fleksibel | Transmisi suara analog telepon kabel konvensional (POTS). Tidak dirancang untuk data digital. |
| **Cat 2** | $4\text{ MHz}$ | $4\text{ Mbps}$ | Hingga $100\text{ m}$ | Sistem PBX dan jaringan IBM Token Ring generasi awal. Berstatus usang (*obsolete*). |
| **Cat 3** | $16\text{ MHz}$ | $10\text{ Mbps}$ | Hingga $100\text{ m}$ | Standar awal 10BASE-T Ethernet pada dekade 1990-an dan instalasi interkom suara lawas. |
| **Cat 4** | $20\text{ MHz}$ | $16\text{ Mbps}$ | Hingga $100\text{ m}$ | Diperuntukkan bagi jaringan Token Ring 16 Mbps sebelum tergantikan oleh Ethernet. |
| **Cat 5** | $100\text{ MHz}$ | $100\text{ Mbps}$ | Hingga $100\text{ m}$ | Standar baku Fast Ethernet (100BASE-TX) menggunakan 2 pasang kawat tembaga. |
| **Cat 5e** | $100\text{ MHz}$ | $1\text{ Gbps}$ ($1.000\text{ Mbps}$) | Hingga $100\text{ m}$ | Cat 5 Enhanced dengan reduksi crosstalk untuk Gigabit Ethernet (1000BASE-T). |
| **Cat 6** | $250\text{ MHz}$ | $1\text{ Gbps}$ / $10\text{ Gbps}$ | $100\text{ m}$ ($1\text{ Gbps}$) / $55\text{ m}$ ($10\text{ Gbps}$) | Lilitan kawat lebih rapat dengan pemisah silang (*spline*); standar LAN perkantoran modern. |
| **Cat 6a** | $500\text{ MHz}$ | $10\text{ Gbps}$ | Hingga $100\text{ m}$ | Cat 6 Augmented yang mendukung transmisi 10GBASE-T pada panjang kabel penuh 100 meter. |
| **Cat 7** | $600\text{ MHz}$ | $10\text{ Gbps}$ | Hingga $100\text{ m}$ | Spesifikasi ISO/IEC Class F berpelindung ganda (S/FTP) dengan konektor GG45/TERA atau RJ-45. |
| **Cat 8** | $2.000\text{ MHz}$ ($2\text{ GHz}$) | $25\text{ Gbps}$ - $40\text{ Gbps}$ | Maksimal $30\text{ - }36\text{ m}$ | Dirancang untuk interkoneksi peladen pusat data (Top-of-Rack/switch-to-server) STP/FTP. |
| **Cat 9** | Konseptual ($> 2\text{ GHz}$) | Eksperimental ($> 40\text{ Gbps}$) | Sangat terbatas | Belum diratifikasi TIA/EIA maupun ISO/IEC resmi; berupa prototipe riset berpelindung rapat. |

---

### 2. Standar Wi-Fi IEEE (Protokol a/b/g/n/ac/ax/be)
Standar komunikasi nirkabel berbasis WLAN dikembangkan oleh IEEE dalam rumpun 802.11 menggunakan media gelombang Radio Frequency (RF). Berikut rincian generasinya:

| Standar IEEE | Versi Aliansi | Tahun Rilis | Pita Frekuensi | Laju Kecepatan Maksimal | Karakteristik & Modulasi |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **802.11a** | Wi-Fi 1 (Legacy) | 1999 | $5\text{ GHz}$ | $54\text{ Mbps}$ | Modulasi OFDM pertama di pita 5 GHz; bebas interferensi 2,4 GHz, penetrasi terbatas. |
| **802.11b** | Wi-Fi 2 (Legacy) | 1999 | $2,4\text{ GHz}$ | $11\text{ Mbps}$ | Modulasi DSSS; perangkat nirkabel pertama yang diadopsi publik secara luas. |
| **802.11g** | Wi-Fi 3 (Legacy) | 2003 | $2,4\text{ GHz}$ | $54\text{ Mbps}$ | Modulasi OFDM di frekuensi 2,4 GHz; kompatibel mundur dengan 802.11b. |
| **802.11n** | Wi-Fi 4 | 2009 | $2,4\text{ GHz}$ & $5\text{ GHz}$ | $600\text{ Mbps}$ | Teknologi MIMO (Multiple-Input Multiple-Output), lebar kanal 40 MHz, pita ganda. |
| **802.11ac** | Wi-Fi 5 | 2013 | $5\text{ GHz}$ | $6,93\text{ Gbps}$ | Modulasi 256-QAM, kanal hingga 160 MHz, dan MU-MIMO downlink. |
| **802.11ax** | Wi-Fi 6/6E | 2019/2021 | $2,4\text{ GHz}$, $5\text{ GHz}$, $6\text{ GHz}$ | $9,6\text{ Gbps}$ | OFDMA untuk kepadatan tinggi, 1024-QAM, Target Wake Time (TWT), spektrum baru 6 GHz. |
| **802.11be** | Wi-Fi 7 | 2024 | $2,4\text{ GHz}$, $5\text{ GHz}$, $6\text{ GHz}$ | $46\text{ Gbps}$ | Kanal ultra-lebar 320 MHz, 4096-QAM (4K-QAM), dan fitur Multi-Link Operation (MLO). |

---

### 3. Garis Waktu Tonggak Perkembangan Internet
Kronologi tonggak penting dalam sejarah perancangan jaringan komputer global dari ARPANET hingga arsitektur modern:

| Periode / Tahun | Fokus Utama | Rincian Penjelasan |
| :--- | :--- | :--- |
| **1960-an** | Riset packet switching | Riset pemecahan data menjadi paket independen (Baran, Davies, Kleinrock) sebagai fondasi arsitektur jaringan terdistribusi. |
| **1969** | ARPANET menghubungkan 4 node awal | Empat simpul awal (UCLA, SRI, UC Santa Barbara, University of Utah) berhasil terhubung di bawah proyek DARPA. |
| **1970-an - 1983** | Pengembangan internetworking & Transisi ke TCP/IP | Vint Cerf dan Bob Kahn merancang arsitektur komunikasi data lintas jaringan heterogen (cikal bakal TCP/IP). Peristiwa Flag Day (1 Januari 1983) beralih wajib ke TCP/IP; ditetapkan sebagai hari lahir internet. |
| **1984** | DNS mulai digunakan | Paul Mockapetris menciptakan Domain Name System untuk menerjemahkan nama domain hierarkis ke alamat IP numerik. |
| **1989-1991** | World Wide Web dikembangkan di CERN | Tim Berners-Lee merancang HTTP, HTML, URL, dan peramban web pertama untuk repositori dokumen informasi global. |
| **1990-an** | Komersialisasi & pertumbuhan akses publik | Pencabutan larangan komersial NSFNET, rilis peramban grafis NCSA Mosaic/Netscape, dan ledakan ekonomi digital (*dot-com boom*). |
| **2000-an** | Broadband, Wi-Fi, & layanan web berkembang | Migrasi ke pita lebar ADSL/Kabel, penetrasi Wi-Fi residensial massal, serta kemunculan platform interaktif Web 2.0. |
| **2010-an** | Awan, seluler, IoT, dan IPv6 | Ekosistem komputasi awan skala besar, konektivitas 4G LTE/5G awal, sensor pintar IoT, dan implementasi alamat IPv6 128-bit. |
| **2020-an** | QUIC/HTTP/3, edge, LEO, dan otomasi jaringan | Adopsi protokol HTTP/3 via QUIC, komputasi tepi (*edge computing*), konstelasi satelit LEO (Starlink), dan otomasi SDN berbasis AI. |

---

### 4. Interpretasi Metrik Pengujian Fast.com dan Hasil Pengujian

#### Definisi Parameter Teknikal:
* **Download Speed (Kecepatan Unduh):** Kapasitas koneksi menarik data dari peladen pengujian ke perangkat per satuan detik (Mbps/Gbps). Menentukan kelancaran streaming resolusi tinggi dan unduhan berkas besar.
* **Upload Speed (Kecepatan Unggah):** Laju pengiriman data keluar dari perangkat menuju internet (Mbps/Gbps). Esensial untuk video conference (Meet/Zoom), live streaming, dan backup cloud.
* **Unloaded Latency (Latensi Tanpa Beban):** Waktu tempuh bolak-balik (RTT / Round-Trip Time) sebuah paket data saat kondisi jaringan tenang tanpa transmisi data aktif lainnya.
* **Loaded Latency (Latensi Terbebani):** Nilai RTT saat jaringan sedang digunakan secara penuh. Lonjakan ekstrem dibanding unloaded latency mengindikasikan Bufferbloat (penumpukan antrean buffer router).
* **Client & Server Location:** Menampilkan alamat IP publik pengguna, nama ISP (Internet Service Provider), serta letak kota server pengujian terdekat yang melayani koneksi.

#### Hasil Pengujian Koneksi Pribadi (Fast.com)

| Parameter Pengujian | Satuan | Hasil Pengujian | Analisis / Keterangan |
| :--- | :--- | :--- | :--- |
| **Kecepatan Unduh (Download)** | Kbps / Mbps / Gbps | 270 Kbps | Sangat Buruk |
| **Kecepatan Unggah (Upload)** | Kbps / Mbps / Gbps | 810 Kbps | Asimetris, namun kecepatan upload relatif lebih tinggi dari kecepatan download. |
| **Unloaded Latency (Ping Bebas)** | Milidetik (ms) | 90 ms | Cukup tinggi untuk peladen domestik/lokal, menandakan respons awal transmisi jaringan relatif lambat. |
| **Loaded Latency (Ping Terbebani)** | Milidetik (ms) | 681 ms | Terjadi lonjakan sangat besar (selisih > 590 ms), mengindikasikan masalah Bufferbloat parah; koneksi akan terasa sangat lag jika dipakai bersamaan. |
| **Penyedia Layanan (ISP / ASN)** | Teks | Telkom | Nama operator / provider |
| **Alamat IP Klien (Publik)** | IPv4 / IPv6 | IPv4 | 125.164.81.6 |
| **Lokasi Peladen (Server)** | Kota / Negara | Kota Surabaya, ID \| Singapore, SG | Pengujian dilakukan dari Driyorejo menuju titik peladen CDN pengujian di Surabaya dan Singapura. |