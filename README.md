# Auto kirim Pesan di Whatsapp

Bot Ini support untuk mengirim hingga 1000 pesan secara otomatis dengan memanfaatkan data dari file excel

## Fitur
- **Kirim ke banyak kontak**
- **Support dengan gambar**

## Requirements
- **Python** (version 2.7 or higher)

## Langkah Awal

### Step 1: Clone Repository ini
Buka terminal dan jalankan perintah :

```
git clone https://github.com/yourbee03/wa-autobot
```

### Step 2: Navigate to the Project Directory
masuk ke file bot dengan perintah:

```
cd wa-autobot
```

### Step 3: Install Dependencies
Masukkan perintah untuk menginstal dependesi yang diperlukan:

```
pip install -r requirements.txt
```

### Step 4: Isi Data Kontak
Masukkan data kontak pada file bernama kontak.xlsx
dengan ketentuan :
- **Pastikan 'Kolom 1' : berisikan Nama dan 'Kolom 2' : berisikan No telepon**
- **No telepon tidak memakai tanda '+' contoh :** 6281232345667


### Step 5: Jalankan Bot
Masukkan perintah di bawah untuk menjalankan bot :

```
python wa.py
```

## Perhatian
**Ini hanya dibuat dengan tujuan Pembelajaran**
- **Mohon Tidak di salah gunakan**

## Note
- **jika ingin memakai gambar edit pada file wa.py line 33 dan masukkan lokasi gambar anda berada**
- **jika ingin memakai file excel yang sudah ada silahkan edit pada file wa.py line 6 dan ganti kontak.xlsx dengan nama file yang sesuai** 