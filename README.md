# Web Simulasi AES-128

Aplikasi Flask untuk simulasi Advanced Encryption Standard (AES-128) sesuai instruksi tugas Kriptografi.

## Fitur

- Input manual plaintext dalam bentuk teks maksimal 16 karakter atau hex 32 karakter.
- Input key AES-128 32 karakter hex.
- Mode enkripsi dan dekripsi satu blok ECB.
- Output hex dapat disalin.
- Visualisasi State Matrix 4x4.
- Key Expansion lengkap W[0] sampai W[43].
- Round Key RK0 sampai RK10.
- Detail Initial Round, Round 1-10, dan proses dekripsi invers.
- UI responsif dengan show/hide detail.

## Cara Menjalankan Lokal

```bash
pip install -r requirements.txt
python app.py
```

Buka browser ke:

```text
http://127.0.0.1:5000
```

## Test Vector AES-128

Plaintext:

```text
00112233445566778899AABBCCDDEEFF
```

Key:

```text
000102030405060708090A0B0C0D0E0F
```

Ciphertext:

```text
69C4E0D86A7B0430D8CDB78070B4C55A
```

## Catatan Akademik

Implementasi AES dibuat manual pada `aes.py` dan tidak menggunakan library kriptografi untuk proses inti.
