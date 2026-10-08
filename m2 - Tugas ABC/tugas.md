# TUGAS KONSEP JARINGAN

---

## Level A — Ingatan dan Pemahaman

### 1. Alasan Komunikasi Berlapis
Memecah kompleksitas sistem komunikasi menjadi modul-modul terisolasi sehingga perubahan atau inovasi pada satu lapisan tidak merusak fungsi lapisan lainnya.

### 2. Perbedaan Layanan, Antarmuka, dan Protokol
* **Layanan (Service):** Fungsi atau kemampuan yang disediakan oleh suatu lapisan untuk lapisan di atasnya.
* **Antarmuka (Interface):** Jalur atau pintu masuk bagi lapisan atas untuk mengakses layanan lapisan di bawahnya.
* **Protokol:** Aturan dan format pesan yang mengatur komunikasi antar-node selevel (*peer entities*).

### 3. Tujuh Lapisan OSI (Bawah ke Atas) & Fungsi Utamanya
1. **Physical:** Transmisi bit mentah melalui media fisik.
2. **Data Link:** Pengiriman frame bebas galat antar-node dalam satu jaringan lokal (MAC).
3. **Network:** Penentuan rute (*routing*) dan pengalamatan logis (IP).
4. **Transport:** Pengiriman data ujung-ke-ujung (*end-to-end*) dan kontrol aliran/keandalan (TCP/UDP).
5. **Session:** Pengelolaan dan sinkronisasi sesi komunikasi antar-aplikasi.
6. **Presentation:** Translasi, enkripsi, dan kompresi format data.
7. **Application:** Antarmuka langsung layanan jaringan ke aplikasi pengguna.

### 4. Empat Lapisan Model TCP/IP
* **Link (Network Interface)**
* **Internet**
* **Transport**
* **Application**

### 5. Mengapa Model TCP/IP Disajikan sebagai 5 Lapisan
Untuk kepentingan akademis/pengajaran, lapisan *Link* dipisah menjadi **Physical** dan **Data Link** agar pemahaman transmisi fisik jaringan menjadi lebih jelas.

### 6. Perbedaan Frame, IP Packet, TCP Segment, dan UDP Datagram
* **Frame:** PDU di Data Link Layer (berisi header/trailer MAC).
* **IP Packet:** PDU di Network Layer (berisi header IP).
* **TCP Segment:** PDU terorientasi koneksi dan andal di Transport Layer (header TCP).
* **UDP Datagram:** PDU *connectionless* tanpa jaminan di Transport Layer (header UDP).

### 7. Definisi Header, Trailer, dan Payload
* **Header:** Informasi kontrol yang ditambahkan di awal data oleh suatu lapisan.
* **Trailer:** Informasi kontrol/validasi (seperti FCS) yang ditambahkan di akhir data (biasanya pada Data Link Layer).
* **Payload:** Data utama/isi bersih yang dibawakan dari lapisan di atasnya.

### 8. Enkapsulasi dan Dekapsulasi
* **Enkapsulasi:** Proses pengemasan data dari lapisan atas dengan tambahan header/trailer saat data bergerak **turun** stack.
* **Dekapsulasi:** Proses pelepasan header/trailer oleh lapisan penerima saat data bergerak **naik** stack.

### 9. Fungsi Multiplexing dan Demultiplexing
* **Multiplexing:** Menggabungkan aliran data dari beberapa aplikasi menjadi satu jalur transmisi tunggal di pengirim.
* **Demultiplexing:** Memisahkan dan mengarahkan data kembali ke aplikasi yang tepat di penerima berdasarkan port.

### 10. Mengapa OSI Tidak Boleh Dianggap sebagai Spesifikasi Implementasi
OSI adalah **model acuan konseptual** (kerangka teori), bukan standar protokol siap pakai seperti TCP/IP yang diimplementasikan langsung pada perangkat lunak/keras.

---

## Level B — Penerapan dan Analisis

### 1. Pemetaan Protokol ke Model TCP/IP (4 Lapisan)
* **Application:** HTTP, DNS, TLS*, QUIC*
* **Transport:** TCP, UDP
* **Internet:** IPv6, ICMP*
* **Link:** Ethernet, Wi-Fi

*\*Catatan Tambahan:*
* **TLS:** Berada di antara Application & Transport (dulu dianggap Presentation).
* **QUIC:** Berjalan di atas UDP tetapi menangani fungsi enkripsi/transport (aplikasi rasa transport).
* **ICMP:** Membantu Network layer tetapi menumpang pada IP packet.

### 2. Enkapsulasi DNS melalui UDP, IPv4, dan Ethernet
* **Urutan Enkapsulasi:**  
  `[Ethernet Header | IPv4 Header | UDP Header | DNS Data | Ethernet Trailer]`
* **Pengenal/Batas pada Setiap Batas:**
  * Ethernet Header $\to$ IPv4 Header: `EtherType (0x0800)`
  * IPv4 Header $\to$ UDP Header: `Protocol Number (17)`
  * UDP Header $\to$ DNS Data: `Destination Port (53)`

### 3. Enkapsulasi HTTP/3 (QUIC) & Alasan QUIC Tetap Transport
* **Urutan Enkapsulasi:**  
  `[Ethernet | IPv4 | UDP | QUIC | HTTP/3 Data]`
* **Mengapa QUIC Tetap Transport:** Karena QUIC menyediakan fungsi *multiplexing*, retransmisi, kontrol kongesti, dan enkripsi *end-to-end* mandiri meskipun dikemas di dalam UDP port 443.

### 4. Perubahan Header Saat Paket Melewati Satu Router (Non-NAT)
* **Berubah:** Header Ethernet/Data Link (MAC asal & MAC tujuan diperbarui sesuai hop berikutnya) dan IP TTL (berkurang 1, IP Checksum berubah).
* **Tetap:** Header IP asal, IP tujuan, serta seluruh Header Transport (TCP/UDP) dan Data Aplikasi.

### 5. Perubahan Analisis Jika Router Melakukan NAT/PAT
Selain MAC dan TTL yang berubah, **IP Asal/Tujuan** dan/atau **Port Transport Asal/Tujuan** pada header L3 & L4 ikut dimodifikasi oleh router. Checksum IP dan Transport juga ikut dihitung ulang.

### 6. Hipotesis Checksum TCP Salah pada Capture Paket Keluar
Terjadi **TCP Checksum Offload**. Kartu jaringan (NIC) menghitung checksum secara *hardware* saat paket fisik dikirim, sehingga *packet capture* di tingkat OS menangkap paket sebelum checksum diisi oleh NIC.

### 7. Diagnosis Portal Bisa Diakses Lewat IP tapi Tidak Lewat Nama
* **Physical s.d. Transport Layer:** Normal (konektivitas L1–L4 terbukti berjalan lancar lewat tes IP).
* **Application Layer:** Terjadi kegagalan resolusi nama pada **DNS Server** (Port 53), baik karena konfigurasi DNS kueri salah, server DNS *down*, atau blokir FQDN.

### 8. Enam Hipotesis HTTPS Gagal (Padahal Ping Berhasil)
1. **L4 (Transport):** Port 443 diblokir oleh firewall.
2. **L4 (Transport):** *SYN-ACK* dari server hilang karena *socket starvation*.
3. **L5/L6 (Session/Presentation):** TLS/SSL Handshake gagal karena sertifikat kedaluwarsa atau tidak dipercaya.
4. **L5/L6 (Session/Presentation):** Ketidakcocokan *Cipher Suite* antara klien dan server.
5. **L7 (Application):** Web server (Nginx/Apache) mati atau mengalami error internal (5xx).
6. **L7 (Application):** Blokir berdasarkan SNI oleh sistem SNI-filtering/WAF.

### 9. Sesi Aplikasi vs Koneksi TCP
* **Koneksi TCP:** Saluran komunikasi L4 bersifat *stateful* dan sementara.
* **Sesi Aplikasi:** Identitas & status interaksi L7 (misal: login akun).
* **Contoh:** Beralih dari Wi-Fi ke Mobile Data membuat IP & koneksi TCP putus-sambung (TCP baru dibuat), tetapi sesi aplikasi (seperti video streaming/login e-commerce) tetap bertahan menggunakan *session token/cookie*.

### 10. Alasan Enkripsi Tidak Selalu Ditempatkan di Presentation Layer
Karena kebutuhan titik enkripsi bervariasi: enkripsi L2 (MACsec) melindungi link fisik, L3 (IPsec) melindungi antar-jaringan, L4/L5 (TLS) melindungi transportasi data, dan L7 melindungi *payload* hingga ke *database* terisolasi.

---

## Level C — Evaluasi dan Sintesis

### 1. Evaluasi Pernyataan Relevansi Model OSI
Pernyataan **kurang tepat**. Secara komersial OSI memang dikalahkan oleh TCP/IP, tetapi secara **pedagogis dan teoritis**, OSI tetap sangat relevan sebagai kerangka acuan modular untuk memahami fungsi jaringan, abstraksi keamanan, dan *troubleshooting*.

### 2. Keuntungan & Kerugian Strict Layering serta Cross-Layer Information
* **Keuntungan:** Modularitas tinggi, pemeliharaan mudah, dan interoperabilitas luas.
* **Kerugian:** Biaya *overhead* header dan potensi duplikasi fungsi (misal: error control di L2 dan L4).
* **Cross-Layer Information:**
  * *Membantu:* Meningkatkan efisiensi jaringan nirkabel/seluler (misal: memberikan status sinyal L1 ke L4 untuk penyesuaian kongesti).
  * *Merusak:* Merusak modularitas, membuat kode sulit diubah, dan memicu efek samping yang tidak terprediksi pada protokol lain.

### 3. Prosedur Troubleshooting Wi-Fi Jam Sibuk (4 Lapisan)
1. **L1 (Physical):** Cek *Interferensi RF* dan *Channel Saturation* menggunakan Wi-Fi Analyzer.
2. **L2 (Data Link):** Analisis nilai *Retry Rate*, *Frame Loss*, dan *Airtime Fairness* pada AP.
3. **L3 (Network):** Jalankan `ping` berulang untuk melihat lonjakan *jitter* dan *packet loss*.
4. **L7 (Application):** Pantau penyesuaian *bitrate* otomatis pada aplikasi video konferensi (Zoom/Meet).

### 4. Skenario Lab Perekaman Paket Aman (Tanpa Data Sensitif)
* **Langkah:** Jalankan `curl -v https://example.com` sambil merekam paket dengan Wireshark/tcpdump menggunakan filter `host example.com`.
* **Elemen Terekam:** Frame Ethernet (L2), Alamat IP Publik (L3), Handshake TCP (L4), TLS Handshake (L5/L6), dan Header GET HTTP/2 / payload terenkripsi (L7).
* **Keamanan:** Tidak menggunakan autentikasi, menggunakan TLS 1.3, dan data publik tanpa isi rahasia.

### 5. Urutan Header VXLAN + IPsec Tunnel & Risiko MTU
* **Urutan Header:**  
  `[Outer Ethernet | Outer IP | IPsec ESP | Outer UDP (4789) | VXLAN Header | Inner Ethernet | Inner IP | Payload]`
* **Risiko MTU:** Akumulasi header tambahan yang besar dapat memicu masalah **Path MTU Discovery (PMTUD)** dan fragmentasi IP yang parah jika nilai MTU/MSS pada interface tidak disesuaikan.

### 6. Perbandingan Enkripsi: MACsec, IPsec, TLS, dan End-to-End App

| Teknologi | Titik Terminasi | Cakupan Kepercayaan |
| :--- | :--- | :--- |
| **MACsec** | Antar-port fisik (Switch to Switch) | Hanya melintasi satu tautan kabel/nirkabel tunggal (L2). |
| **IPsec** | Antar-gateway/router (Site-to-Site) | Melintasi seluruh jaringan antar-router (L3). |
| **TLS** | Antar-aplikasi (Browser to Web Server) | Melintasi seluruh jalur end-to-end L4-L7. |
| **End-to-End App** | Antar-pengguna (Client A to Client B) | Melindungi data hingga ke dalam aplikasi penerima (bahkan proxy/server