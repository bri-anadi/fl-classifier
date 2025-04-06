# File Classifier

Utilitas Python lintas platform yang kuat untuk mengorganisir file dan folder secara otomatis berdasarkan ekstensi, nama folder, atau waktu.

## Fitur

- **Beberapa Metode Klasifikasi**:
  - **Berbasis Ekstensi**: Mengklasifikasikan file ke dalam kategori berdasarkan ekstensinya
  - **Berbasis Waktu**: Mengorganisir file berdasarkan waktu pembuatan, modifikasi, atau akses
  - **Klasifikasi Folder**: Mengkategorikan folder berdasarkan pola penamaan umum

- **Kategori File**:
  - Dokumen (PDF, DOC, TXT, dll.)
  - Gambar (JPG, PNG, GIF, dll.)
  - Audio (MP3, WAV, FLAC, dll.)
  - Video (MP4, AVI, MKV, dll.)
  - Arsip (ZIP, RAR, 7Z, dll.)
  - Kode (PY, JAVA, HTML, dll.)
  - Executable (EXE, MSI, APP, dll.)
  - Lainnya (untuk ekstensi yang tidak termasuk kategori di atas)

- **Kategori Folder**:
  - Projects: Untuk folder pengembangan dan proyek
  - Backups: Untuk konten cadangan dan arsip
  - Documents: Untuk folder dokumen dan laporan
  - Media: Untuk folder foto, video, musik
  - Downloads: Untuk folder unduhan
  - Applications: Untuk perangkat lunak dan aplikasi
  - Data: Untuk dataset dan database
  - Web: Untuk konten terkait web
  - Dated: Untuk folder dengan pola tanggal (terdeteksi otomatis)
  - Versioned: Untuk folder dengan pola versi (terdeteksi otomatis)
  - Uncategorized: Untuk folder yang tidak cocok dengan pola manapun

- **Mode Operasi**:
  - Move (default): Memindahkan file/folder ke direktori target
  - Copy: Membuat salinan alih-alih memindahkan
  - Symlink: Membuat tautan simbolis ke file/folder asli
  - Dry-run: Menampilkan apa yang akan terjadi tanpa membuat perubahan

- **Kompatibilitas Lintas Platform**:
  - Berjalan di Windows, macOS, dan Linux

## Persyaratan

- Python 3.6 atau lebih tinggi
- Tidak memerlukan pustaka tambahan (hanya menggunakan pustaka standar)

## Instalasi

Unduh skrip dan buat agar dapat dieksekusi:

```bash
chmod +x file_classifier.py
```

Atau jalankan langsung dengan Python:

```bash
python file_classifier.py [opsi]
```

## Penggunaan

### Penggunaan Dasar

```bash
python file_classifier.py DIR_SUMBER [DIR_TARGET]
```

Jika `DIR_TARGET` tidak ditentukan, file akan diorganisir di direktori baru bernama `./classified`.

### Opsi Umum

```
-l, --symlinks       Membuat symlink alih-alih memindahkan file
-c, --copy           Menyalin file alih-alih memindahkannya
-d, --dry-run        Menampilkan apa yang akan dilakukan tanpa benar-benar melakukannya
-f, --folders        Menyertakan folder dalam klasifikasi
```

### Metode Klasifikasi

```
-e, --extensions     Klasifikasi berdasarkan ekstensi file (perilaku default)
-t, --time           Organisasi berdasarkan atribut waktu
```

### Opsi Organisasi Berbasis Waktu

```
--time-attr {modified,created,accessed}
                     Atribut waktu yang digunakan (default: modified)
--time-format FORMAT
                     Format waktu untuk direktori (default: '%Y-%m' untuk tahun-bulan)
```

## Contoh

### Organisasi Berbasis Ekstensi

```bash
# Klasifikasikan semua file di folder Downloads berdasarkan ekstensi
python file_classifier.py ~/Downloads ~/Organized

# Klasifikasikan file dan folder, buat salinan alih-alih memindahkan
python file_classifier.py ~/Documents ~/Organized -f -c

# Buat symlink alih-alih memindahkan file
python file_classifier.py ~/Pictures ~/Organized -l

# Lihat pratinjau apa yang akan terjadi tanpa membuat perubahan
python file_classifier.py ~/Desktop -d
```

### Organisasi Berbasis Waktu

```bash
# Organisasikan file berdasarkan waktu modifikasi (tahun-bulan)
python file_classifier.py ~/Documents ~/TimeOrganized -t

# Organisasikan berdasarkan tanggal pembuatan dengan format tahun-bulan-hari
python file_classifier.py ~/Photos ~/Chronological -t --time-attr created --time-format "%Y-%m-%d"

# Organisasikan file dan folder berdasarkan waktu akses
python file_classifier.py ~/Downloads ~/AccessOrganized -t --time-attr accessed -f
```

## FAQ

**T: Apa yang terjadi jika file atau folder sudah ada di direktori target?**
J: Skrip akan melewatinya dan mencatat pesan peringatan.

**T: Apakah organisasi akan mempertahankan struktur direktori?**
J: Tidak, semua file diratakan ke direktori kategori yang sesuai. Untuk organisasi hierarkis, pertimbangkan untuk menggunakan organisasi berbasis waktu dengan format hierarkis seperti `%Y/%m/%d`.

**T: Bisakah saya menyesuaikan kategori file?**
J: Ya, Anda dapat mengedit kamus `FILE_CATEGORIES` dalam skrip untuk menambah atau memodifikasi kategori.

## Lisensi

Utilitas ini dirilis di bawah Lisensi MIT. Silakan gunakan, modifikasi, dan distribusikan dengan bebas.
