# Web Simulasi AES-128

Aplikasi **Web Simulasi Advanced Encryption Standard (AES-128)** berbasis **Python Flask** yang dibuat sebagai pemenuhan tugas Mata Kuliah **Kriptografi** Semester Genap 2025/2026. Aplikasi ini mengimplementasikan algoritma AES-128 secara mandiri tanpa menggunakan library kriptografi sebagai proses utama, sehingga seluruh tahapan algoritma dapat dipelajari secara rinci.

---

# Deskripsi Aplikasi

Web Simulasi AES-128 merupakan aplikasi edukasi yang digunakan untuk mempelajari proses kerja algoritma **Advanced Encryption Standard (AES-128)**. Aplikasi mampu melakukan proses **enkripsi** maupun **dekripsi** terhadap satu blok data (128-bit / 16 byte) menggunakan mode operasi **ECB (Electronic Codebook)**.

Selain menghasilkan ciphertext dan plaintext, aplikasi juga menampilkan seluruh proses internal algoritma AES, seperti **Key Expansion**, **Round Key**, **State Matrix**, serta proses pada setiap ronde sehingga pengguna dapat memahami bagaimana algoritma AES bekerja secara bertahap.

---

# Fitur Aplikasi

Aplikasi memiliki beberapa fitur utama, yaitu:

* Input plaintext dalam bentuk **teks maksimal 16 karakter**.
* Input plaintext dalam bentuk **hexadecimal 32 karakter**.
* Input key AES-128 sebanyak **32 karakter hexadecimal**.
* Mode **Enkripsi (Encrypt)**.
* Mode **Dekripsi (Decrypt)**.
* Tombol **Reset** untuk menghapus seluruh input.
* Tombol **Copy Output** untuk menyalin hasil enkripsi maupun dekripsi.
* Visualisasi **State Matrix 4×4** pada setiap tahapan AES.
* Menampilkan proses **Key Expansion** mulai dari **Word W[0] hingga W[43]**.
* Menampilkan **Round Key RK0 sampai RK10**.
* Menampilkan proses **RotWord**, **SubWord**, dan **XOR Rcon**.
* Menampilkan proses **Initial Round**.
* Menampilkan proses **Round 1 sampai Round 10** secara lengkap.
* Menampilkan proses **InvShiftRows**, **InvSubBytes**, **InvMixColumns**, dan **AddRoundKey** pada proses dekripsi.
* Fitur **Show / Hide Detail** agar pengguna dapat menampilkan maupun menyembunyikan detail perhitungan.

---

# Struktur Project

```text
project-aes/
│
├── app.py
├── aes.py
├── requirements.txt
├── README.md
├── vercel.json
│
├── templates/
│   ├── index.html
│   └── partials/
│       └── matrix.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── app.js
```

---

# Persyaratan Sistem

Sebelum menjalankan aplikasi, pastikan komputer telah memiliki:

* Python 3.10 atau lebih baru
* pip (Python Package Manager)

---

# Instalasi

Clone repository GitHub terlebih dahulu.

```bash
git clone https://github.com/USERNAME/NAMA-REPOSITORY.git
```

Masuk ke folder project.

```bash
cd NAMA-REPOSITORY
```

Install seluruh dependency.

```bash
pip install -r requirements.txt
```

---

# Menjalankan Aplikasi

Jalankan aplikasi menggunakan perintah berikut.

```bash
python app.py
```

Apabila aplikasi berhasil dijalankan, terminal akan menampilkan informasi seperti berikut.

```text
* Running on http://127.0.0.1:5000
```

atau

```text
* Running on http://localhost:5000
```

---

# Cara Mengakses Aplikasi

Setelah server Flask berhasil dijalankan, buka browser seperti:

* Google Chrome
* Microsoft Edge
* Mozilla Firefox

Kemudian ketik alamat berikut pada address bar browser.

```text
http://localhost:5000
```

atau

```text
http://127.0.0.1:5000
```

Selanjutnya tekan **Enter**.

Halaman utama Web Simulasi AES-128 akan ditampilkan sehingga pengguna dapat langsung menggunakan aplikasi untuk melakukan proses enkripsi maupun dekripsi.

---

# Cara Menggunakan Aplikasi

## Enkripsi

1. Jalankan aplikasi Flask.
2. Buka browser menuju **http://localhost:5000**.
3. Pilih mode **Enkripsi**.
4. Pilih jenis input:

   * Plaintext Hex 32 karakter, atau
   * Plaintext Teks maksimal 16 karakter.
5. Masukkan plaintext.
6. Masukkan key AES-128 sebanyak 32 karakter hexadecimal.
7. Klik tombol **ENCRYPT**.
8. Aplikasi akan menghasilkan ciphertext beserta seluruh proses perhitungan AES.

---

## Dekripsi

1. Pilih mode **Dekripsi**.
2. Masukkan ciphertext 32 karakter hexadecimal.
3. Masukkan key AES-128 yang sama.
4. Klik tombol **DECRYPT**.
5. Aplikasi akan menghasilkan plaintext beserta seluruh proses dekripsi AES.

---

# Contoh Data Uji (AES Standard Test Vector)

## Plaintext

```text
00112233445566778899AABBCCDDEEFF
```

## Key

```text
000102030405060708090A0B0C0D0E0F
```

## Ciphertext

```text
69C4E0D86A7B0430D8CDB78070B4C55A
```

---

# Teknologi yang Digunakan

* Python
* Flask
* HTML5
* CSS3
* JavaScript
* Jinja2 Template Engine

---

# Catatan Akademik

Implementasi algoritma AES-128 pada aplikasi ini dibuat secara mandiri sebagai bagian dari tugas Mata Kuliah Kriptografi. Seluruh proses utama algoritma, seperti Key Expansion, SubBytes, ShiftRows, MixColumns, AddRoundKey, serta operasi invers pada dekripsi diimplementasikan sendiri pada file `aes.py`.

Library kriptografi pihak ketiga **tidak digunakan sebagai implementasi utama**, melainkan hanya dapat digunakan untuk proses verifikasi hasil sesuai ketentuan tugas.

---

# Author

**Nama :** Intan Telaumbanua

**NIM :** 301230016

**Kelas :** 6B

**Mata Kuliah :** Kriptografi

**Semester :** Genap 2025/2026
