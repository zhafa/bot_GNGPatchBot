import discord
import aiohttp  
from bs4 import BeautifulSoup
import asyncio
import os
from dotenv import load_dotenv

# Load variabel dari .env
load_dotenv()

# Ambil token & channel ID dengan aman
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# Validasi variabel
if not TOKEN or not CHANNEL_ID:
    raise ValueError("❌ TOKEN atau CHANNEL_ID tidak ditemukan di .env!")

CHANNEL_ID = int(CHANNEL_ID)  # Konversi ke integer

BASE_URL = "https://goldandglorymobile.com/ind/"
ARTICLE_BASE_URL = "https://goldandglorymobile.com"

# Intents agar bisa membaca pesan
intents = discord.Intents.default()
intents.message_content = True  # Tambahkan jika bot perlu membaca pesan

class PatchBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.latest_patch_url = None
        self.session = None  # Inisialisasi tanpa membuat session langsung

    async def on_ready(self):
        try:
            print(f'✅ Bot {self.user} sudah online!')
            if self.session is None:
                self.session = aiohttp.ClientSession()  # Buat session saat event loop sudah berjalan
            await self.check_patch_updates()
        except Exception as e:
            print(f"❌ Error di on_ready: {e}")

    async def on_message(self, message):
        """Mendeteksi jika pengguna mengetik !ping"""
        if message.author == self.user:  # Hindari bot merespon pesan sendiri
            return

        if message.content == "!ping":
            await message.channel.send("Pong! 🏓")

    async def get_latest_patch(self):
        """Scrape halaman utama untuk mendapatkan link patch terbaru"""
        try:
            async with self.session.get(BASE_URL, timeout=10) as response:
                if response.status != 200:
                    print(f"⚠️ Gagal mengambil data, status: {response.status}")
                    return None, None

                soup = BeautifulSoup(await response.text(), "html.parser")
                latest_article = soup.find("a", class_="text-line none")

                if latest_article and "href" in latest_article.attrs:
                    patch_url = ARTICLE_BASE_URL + latest_article["href"]
                    patch_content = await self.get_patch_content(patch_url)
                    return patch_url, patch_content
        except Exception as e:
            print(f"❌ Error saat mengambil patch terbaru: {e}")
        return None, None

    async def get_patch_content(self, patch_url):
        """Scrape halaman detail patch untuk mendapatkan isi update dengan format rapi"""
        try:
            async with self.session.get(patch_url, timeout=10) as response:
                if response.status != 200:
                    return "⚠️ Gagal mengambil detail patch."

                soup = BeautifulSoup(await response.text(), "html.parser")
                content_div = soup.find("div", class_="article-content")  

                if content_div:
                    for br in content_div.find_all("br"):
                        br.replace_with("\n")

                    content_text = "\n\n".join(p.get_text(strip=True, separator="\n") for p in content_div.find_all("p"))
                    return content_text.strip()
        except Exception as e:
            print(f"❌ Error saat mengambil detail patch: {e}")
        return "Tidak ada detail patch yang ditemukan."

    async def check_patch_updates(self):
        """Loop untuk cek update patch terbaru setiap 1 jam"""
        await self.wait_until_ready()
        channel = self.get_channel(CHANNEL_ID)

        if not channel:
            print(f"❌ Channel dengan ID {CHANNEL_ID} tidak ditemukan.")
            return

        while not self.is_closed():
            latest_patch_url, latest_patch_content = await self.get_latest_patch()

            # Pastikan tidak posting ulang patch yang sama
            if latest_patch_url and latest_patch_url != self.latest_patch_url:
                self.latest_patch_url = latest_patch_url
                full_message = f"🔥 **Patch Baru!** 🔥\n{latest_patch_content}\n\nCek di {latest_patch_url}"

                messages = self.split_message(full_message)
                for msg in messages:
                    await channel.send(msg)

            await asyncio.sleep(3600)  # Cek setiap 1 jam

    def split_message(self, message, limit=2000):
        """Membagi pesan menjadi beberapa bagian jika melebihi batas karakter Discord"""
        messages = []
        while len(message) > limit:
            split_index = message.rfind("\n", 0, limit)
            if split_index == -1:
                split_index = limit

            messages.append(message[:split_index])
            message = message[split_index:].strip()

        messages.append(message)
        return messages

    async def close(self):
        """Tutup session saat bot dimatikan"""
        if self.session:
            await self.session.close()
        await super().close()

bot = PatchBot()

try:
    bot.run(TOKEN)
except Exception as e:
    print(f"❌ Error saat menjalankan bot: {e}")
