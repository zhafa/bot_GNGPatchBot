"# Discord_GNG-PatchBot" 
GNG PatchBot
📌 Deskripsi
GNG PatchBot adalah bot Discord yang secara otomatis memantau dan menginformasikan pembaruan patch terbaru dari situs Gold and Glory Mobile. Bot ini menggunakan web scraping untuk mendapatkan informasi terbaru dan mengirimkannya ke server Discord secara otomatis.

🚀 Fitur Utama
🔎 Scraping Otomatis: Mengambil informasi patch terbaru dari situs Gold and Glory Mobile.
📢 Notifikasi di Discord: Mengirim pembaruan terbaru langsung ke channel yang ditentukan.
⏳ Cek Otomatis: Mengecek pembaruan setiap 1 jam sekali.
📄 Format Pesan Rapi: Menggunakan pemformatan agar informasi lebih mudah dibaca.
🛠️ Teknologi yang Digunakan
Python 3
discord.py (untuk komunikasi dengan Discord)
BeautifulSoup (untuk web scraping)
Requests (untuk mengambil data dari situs web)
dotenv (untuk mengelola kredensial dengan aman)
⚙️ Instalasi dan Konfigurasi
1️⃣ Clone Repository
git clone https://github.com/username/GNG-PatchBot.git
cd GNG-PatchBot
2️⃣ Buat Virtual Environment (Opsional, tapi disarankan)
python -m venv venv
source venv/bin/activate  # Untuk Linux/Mac
venv\Scripts\activate  # Untuk Windows
3️⃣ Instal Dependensi
pip install -r requirements.txt
4️⃣ Buat File .env untuk Menyimpan Kredensial
Buat file .env di root project dan isi dengan:

DISCORD_TOKEN=your_discord_bot_token
CHANNEL_ID=your_channel_id
Pastikan untuk mengganti your_discord_bot_token dan your_channel_id dengan token bot dan ID channel yang sesuai.

5️⃣ Jalankan Bot
python bot.py
📝 Struktur Folder
GNG-PatchBot/
├── bot.py           # File utama bot
├── .env             # Token Discord dan konfigurasi channel (tidak diupload ke GitHub)
├── .gitignore       # File dan folder yang diabaikan Git
├── README.md        # Dokumentasi proyek
🤝 Kontribusi
Fork repository ini.
Buat branch baru: git checkout -b fitur-baru
Commit perubahan: git commit -m 'Menambahkan fitur baru'
Push ke branch: git push origin fitur-baru
Buat Pull Request!
📜 Lisensi
Proyek ini menggunakan lisensi MIT. Silakan lihat file LICENSE untuk detail lebih lanjut.

📧 Kontak
Jika ada pertanyaan atau saran, silakan hubungi saya melalui:

💬 Discord: lospecados#0034
📩 Email: zhafaanbiya311@gnail,com
Selamat menggunakan GNG PatchBot! 🎉