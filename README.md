# FREEDOG AUTO COLLECT

**FREEDOG AUTO COLLECT** adalah sebuah program otomatisasi untuk mengumpulkan koin pada game FREEDOG. Program ini berjalan menggunakan Python dan melakukan pengumpulan koin secara acak berdasarkan jumlah koin yang tersisa dalam pool.

## Fitur
- **Pengumpulan Koin Otomatis**: Program akan mengumpulkan koin secara otomatis dengan jeda tertentu.
- **Pengaturan Jumlah Minimum Koin**: Hanya akan mengumpulkan koin jika jumlah yang tersisa di pool lebih dari batas minimal yang ditentukan.
- **Randomisasi Jumlah Koin**: Untuk menghindari deteksi, jumlah koin yang dikumpulkan dipilih secara acak.
- **Retry Otomatis**: Jika gagal mengumpulkan koin, program akan mencoba lagi setelah beberapa detik.
- **Pengaturan Interval Koleksi**: Mengatur waktu tunggu sebelum mengumpulkan koin berikutnya.

## Instalasi
1. **Clone Repository**:
    ```bash
    git clone https://github.com/Semutireng22/pridog.git
    cd pridog
    ```

2. **Instalasi Dependensi**:
    Pastikan kamu sudah menginstal Python 3.x. Jalankan perintah berikut untuk menginstal dependensi yang dibutuhkan:
    ```bash
    pip install -r requirements.txt
    ```

3. **Konfigurasi**:
    Buat file `config.json` dan `auth.txt` berdasarkan format berikut:

    - **`config.json`**:
      ```json
      {
          "MIN_COINS_REQUIRED": 100,
          "MAX_COLLECT_AMOUNT": 50,
          "COLLECT_INTERVAL": 5
      }
      ```
      - `MIN_COINS_REQUIRED`: Jumlah minimal koin tersisa di pool untuk melakukan pengumpulan.
      - `MAX_COLLECT_AMOUNT`: Jumlah maksimal koin yang bisa dikumpulkan dalam sekali koleksi.
      - `COLLECT_INTERVAL`: Waktu jeda (dalam detik) sebelum melakukan pengumpulan koin berikutnya.

    - **`auth.txt`**:
      Masukkan token otentikasi yang diperlukan dari API:
      ```
      eyxxxxxxxxxxxxxxxxxxxxx
      ```

## Cara Mendapatkan Token Autentikasi (Auth Token)
1. Buka web.telegram.org dan masuk ke bot freedog
2. Buka konsol peramban (browser developer tools) dengan menekan `F12` atau `Ctrl+Shift+I`.
3. Navigasikan ke tab **Network** dan mulai melakukan aksi dalam aplikasi yang terhubung ke API.
4. Cari permintaan GameUserInfo atau yang terkait dengan **autentikasi** (biasanya disebut `Authorization` atau sejenisnya).
5. Temukan token autentikasi dalam header permintaan di bagian **Authorization**.
6. Salin token tersebut dan simpan dalam file `auth.txt` tanpa spasi tambahan atau karakter lain.

## Cara Menjalankan
1. Setelah konfigurasi selesai, jalankan program dengan perintah berikut:
    ```bash
    python3 bot.py
    ```

2. Untuk menghentikan program, tekan `CTRL + C`.

## Penjelasan Kode
- **`bot.py`**: File utama yang menjalankan logika pengumpulan koin.
- **`config.json`**: File konfigurasi yang mengatur parameter seperti jumlah minimal koin dan interval waktu.
- **`auth.txt`**: Menyimpan token otentikasi API untuk mengakses endpoint game.

## Catatan
- Gunakan program ini secara bijak agar tidak terdeteksi sebagai aktivitas yang mencurigakan.
- Pastikan token otentikasi yang digunakan valid dan memiliki akses yang diperlukan untuk API FREEDOG.

## Kontribusi
Jika kamu ingin berkontribusi atau menemukan bug, silakan buat pull request atau laporkan melalui [issues](https://github.com/Semutireng22/pridog/issues).

## Lisensi
Program ini dilisensikan di bawah [MIT License](LICENSE).
