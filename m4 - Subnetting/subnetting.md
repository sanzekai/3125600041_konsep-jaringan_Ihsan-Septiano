# LAPORAN PRAKTIKUM JARINGAN KOMPUTER
**Desain Topologi, Alokasi Pengalamatan IP, dan Simulasi Subnetting pada Cisco Packet Tracer**

---

### Rumus Dasar Subnetting
* **Cari bit pinjaman ($n$):** $2^n \ge \text{target subnet}$
* **Prefix baru:** $\text{prefix lama} + n$
* **Blok lompatan:** $\frac{\text{sisa bit host}}{2^n}$
* **Sisa bit host:** $256 - \text{subnet mask awal pada oktet tersebut}$
* **Host pertama:** $\text{Network address} + 1$
* **Host terakhir:** $\text{Broadcast} - 1$
* **Broadcast:** $\text{Alamat terakhir dari network } (\text{next network} - 1)$

---

### Kasus 1: Network 192.168.1.0/24 Dijadikan 4 Subnet

#### Analisis Kebutuhan Subnet
* $2^n \ge 4 \implies 2^2 \ge 4 \implies n = 2$
* **Sisa bit host:** $2^8 = 256 \implies \text{Blok lompatan} = \frac{256}{4} = 64$
* **Prefix baru:** $/24 + 2 = /26$
* **Subnet mask baru:** `255.255.255.192`

#### Hasil Alokasi Subnet
* **Subnet Pertama:** `192.168.1.0/26`
  * **Host Pertama:** `192.168.1.1`
  * **Host Terakhir:** `192.168.1.62`
  * **BC Address:** `192.168.1.63`
* **Subnet Kedua:** `192.168.1.64/26`
  * **Host Pertama:** `192.168.1.65`
  * **Host Terakhir:** `192.168.1.126`
  * **BC Address:** `192.168.1.127`
* **Subnet Ketiga:** `192.168.1.128/26`
  * **Host Pertama:** `192.168.1.129`
  * **Host Terakhir:** `192.168.1.190`
  * **BC Address:** `192.168.1.191`
* **Subnet Keempat:** `192.168.1.192/26`
  * **Host Pertama:** `192.168.1.193`
  * **Host Terakhir:** `192.168.1.254`
  * **BC Address:** `192.168.1.255`

---

### Kasus 1 (Alternatif / Pengerjaan 6 Subnet): Network 192.168.1.0/24 Dijadikan 6 Subnet
*(Dikerjakan sebagai alternatif skenario pemenuhan 6 subnet karena saya dengernya 6 subnet tapi temen2 dengernya 4 subnet, jadi saya kerjakan keduanya)*

#### Analisis Kebutuhan Subnet
* $2^n \ge 6 \implies 2^3 \ge 6 \implies n = 3$
* **Sisa bit host:** $2^8 = 256 \implies \text{Blok lompatan} = \frac{256}{2^3} = \frac{256}{8} = 32$
* **Prefix baru:** $/24 + 3 = /27$
* **Subnet mask baru:** `255.255.255.224`

#### Hasil Alokasi Subnet

| Subnet | Network Address | Host Pertama | Host Terakhir | BC Address |
| :--- | :--- | :--- | :--- | :--- |
| **Subnet Pertama** | `192.168.1.0/27` | `192.168.1.1` | `192.168.1.30` | `192.168.1.31` |
| **Subnet Kedua** | `192.168.1.32/27` | `192.168.1.33` | `192.168.1.62` | `192.168.1.63` |
| **Subnet Ketiga** | `192.168.1.64/27` | `192.168.1.65` | `192.168.1.94` | `192.168.1.95` |
| **Subnet Keempat** | `192.168.1.96/27` | `192.168.1.97` | `192.168.1.126` | `192.168.1.127` |
| **Subnet Kelima** | `192.168.1.128/27` | `192.168.1.129` | `192.168.1.158` | `192.168.1.159` |
| **Subnet Keenam** | `192.168.1.160/27` | `192.168.1.161` | `192.168.1.190` | `192.168.1.191` |

---

### Kasus 2: Network 132.10.0.0/16 Dijadikan 10 Subnet

#### Analisis Kebutuhan Subnet
* $2^n \ge 10 \implies 2^4 \ge 10 \implies n = 4$
* **Sisa bit host:** $2^8 \times 2^8 = 256 \times 2^8$
* **Blok lompatan:** $\frac{256}{2^4} = 16$ *(pada oktet ke-3)*
* **Prefix baru:** $/16 + n = /16 + 4 = /20$
* **Subnet mask baru:** `255.255.240.0`

#### Hasil Alokasi Subnet (10 Segmen)

| Segmen | Network Address | Usable IP Range | BC Address |
| :--- | :--- | :--- | :--- |
| **Segmen 1** | `132.10.0.0/20` | `132.10.0.1` - `132.10.15.254` | `132.10.15.255` |
| **Segmen 2** | `132.10.16.0/20` | `132.10.16.1` - `132.10.31.254` | `132.10.31.255` |
| **Segmen 3** | `132.10.32.0/20` | `132.10.32.1` - `132.10.47.254` | `132.10.47.255` |
| **Segmen 4** | `132.10.48.0/20` | `132.10.48.1` - `132.10.63.254` | `132.10.63.255` |
| **Segmen 5** | `132.10.64.0/20` | `132.10.64.1` - `132.10.79.254` | `132.10.79.255` |
| **Segmen 6** | `132.10.80.0/20` | `132.10.80.1` - `132.10.95.254` | `132.10.95.255` |
| **Segmen 7** | `132.10.96.0/20` | `132.10.96.1` - `132.10.111.254` | `132.10.111.255` |
| **Segmen 8** | `132.10.112.0/20` | `132.10.112.1` - `132.10.127.254` | `132.10.127.255` |
| **Segmen 9** | `132.10.128.0/20` | `132.10.128.1` - `132.10.143.254` | `132.10.143.255` |
| **Segmen 10** | `132.10.144.0/20` | `132.10.144.1` - `132.10.159.254` | `132.10.159.255` |

---

### Kasus 3: Network 17.8.0.0/16 Dijadikan 4 Subnet

#### Analisis Kebutuhan Subnet
* $2^n \ge 4 \implies 2^2 \ge 4 \implies n = 2$
* **Sisa bit host:** $2^8 \times 2^8 = 256 \times 2^8$
* **Blok lompatan:** $\frac{256}{2^2} = 64$ *(pada oktet ke-3)*
* **Prefix baru:** $/16 + n = /16 + 2 = /18$
* **Subnet mask baru:** `255.255.192.0`

#### Hasil Alokasi Subnet

| Subnet | Network Address | Usable IP Range | BC Address |
| :--- | :--- | :--- | :--- |
| **Subnet 1** | `17.8.0.0/18` | `17.8.0.1` - `17.8.63.254` | `17.8.63.255` |
| **Subnet 2** | `17.8.64.0/18` | `17.8.64.1` - `17.8.127.254` | `17.8.127.255` |
| **Subnet 3** | `17.8.128.0/18` | `17.8.128.1` - `17.8.191.254` | `17.8.191.255` |
| **Subnet 4** | `17.8.192.0/18` | `17.8.192.1` - `17.8.255.254` | `17.8.255.255` |

---

### Kasus 4: Network 8.32.0.0/12 Dijadikan 6 Subnet

#### Analisis Kebutuhan Subnet
* $2^n \ge 6 \implies 2^3 \ge 6 \implies n = 3$
* **Bit network oktet ke-2 asal:** `0010 0000` ($= 32$)
* **3 bit yang diubah pada oktet ke-2:**
  * `0010 0000` = 32
  * `0010 0010` = 34
  * `0010 0100` = 36
  * `0010 0110` = 38
  * `0010 1000` = 40
  * `0010 1010` = 42
* **Prefix baru:** $/12 + 3 = /15$
* **Subnet mask baru:** `255.254.0.0`

#### Hasil Alokasi Subnet

| Subnet | Network Address | Usable IP Range | BC Address |
| :--- | :--- | :--- | :--- |
| **Subnet 1** | `8.32.0.0/15` | `8.32.0.1` - `8.33.255.254` | `8.33.255.255` |
| **Subnet 2** | `8.34.0.0/15` | `8.34.0.1` - `8.35.255.254` | `8.35.255.255` |
| **Subnet 3** | `8.36.0.0/15` | `8.36.0.1` - `8.37.255.254` | `8.37.255.255` |
| **Subnet 4** | `8.38.0.0/15` | `8.38.0.1` - `8.39.255.254` | `8.39.255.255` |
| **Subnet 5** | `8.40.0.0/15` | `8.40.0.1` - `8.41.255.254` | `8.41.255.255` |
| **Subnet 6** | `8.42.0.0/15` | `8.42.0.1` - `8.43.255.254` | `8.43.255.255` |