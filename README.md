# GNG PatchBot

## 📌 Deskripsi
GNG PatchBot adalah bot Discord yang secara otomatis memantau dan menginformasikan pembaruan patch terbaru dari situs *Gold and Glory Mobile*. Bot ini menggunakan web scraping untuk mendapatkan informasi terbaru dan mengirimkannya ke server Discord secara otomatis.

## 🚀 Fitur Utama
- 🔎 **Scraping Otomatis**: Mengambil informasi patch terbaru dari situs *Gold and Glory Mobile*.
- 📢 **Notifikasi di Discord**: Mengirim pembaruan terbaru langsung ke channel yang ditentukan.
- ⏳ **Cek Otomatis**: Mengecek pembaruan setiap 1 jam sekali.
- 📄 **Format Pesan Rapi**: Menggunakan pemformatan agar informasi lebih mudah dibaca.

## 🛠️ Teknologi yang Digunakan
- **Python 3**
- **discord.py** (untuk komunikasi dengan Discord)
- **BeautifulSoup** (untuk web scraping)
- **Requests** (untuk mengambil data dari situs web)
- **dotenv** (untuk mengelola kredensial dengan aman)

## ⚙️ Instalasi dan Konfigurasi

### 1️⃣ Clone Repositori
```bash
git clone https://github.com/username/GNG-PatchBot.git
cd GNG-PatchBot
```

### 2️⃣ Buat Virtual Environment *(Opsional, tapi disarankan)*
```bash
python -m venv venv
source venv/bin/activate  # Untuk Linux/Mac
venv\Scripts\activate  # Untuk Windows
```

### 3️⃣ Instal Dependensi
```bash
pip install -r requirements.txt
```

### 4️⃣ Buat File `.env` untuk Menyimpan Kredensial
Buat file `.env` di root project dan isi dengan:
```ini
DISCORD_TOKEN=your_discord_bot_token
CHANNEL_ID=your_channel_id
```
> ⚠️ **Jangan membagikan file `.env` ini ke publik!** Pastikan file `.gitignore` sudah mengabaikan `.env` agar tidak diunggah ke GitHub.

### 5️⃣ Jalankan Bot
```bash
python bot.py
```

## 📝 Struktur Folder
```
GNG-PatchBot/
├── bot.py           # File utama bot
├── .env             # Token Discord dan konfigurasi channel (tidak diupload ke GitHub)
├── .gitignore       # File dan folder yang diabaikan Git
├── README.md        # Dokumentasi proyek
```

## 📌 Contoh Output di Discord
```
📢 **Patch Terbaru: Update v1.2.3**
🛠️ **Perbaikan Bug:**
- Memperbaiki crash saat login.
- Mengoptimalkan performa pada perangkat lama.

🔗 **Detail lengkap:** [Gold and Glory Mobile Patch Notes](https://example.com/patch-notes)
```

## 🤝 Kontribusi
1. **Fork repositori ini.**
2. **Buat branch baru:**
   ```bash
   git checkout -b fitur-baru
   ```
3. **Commit perubahan:**
   ```bash
   git commit -m "Menambahkan fitur baru"
   ```
4. **Push ke branch:**
   ```bash
   git push origin fitur-baru
   ```
5. **Buat Pull Request!**

## 📧 Kontak
Jika ada pertanyaan atau saran, silakan hubungi saya melalui:
- 💬 **Discord**: `lospecados#0034`
- 📩 **Email**: zhafaanbiya311@gmail.com

Selamat menggunakan **GNG PatchBot**! 🎉

