import discord
import aiohttp  
from bs4 import BeautifulSoup
import asyncio
import os
from dotenv import load_dotenv

# Load variabel dari .env
load_dotenv()

# Ambil token dengan aman
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# Cek apakah variabel sudah dimuat dengan benar
if not TOKEN or not CHANNEL_ID:
    raise ValueError("❌ TOKEN atau CHANNEL_ID tidak ditemukan di .env!")

CHANNEL_ID = int(CHANNEL_ID)  # Konversi ke integer

BASE_URL = "https://goldandglorymobile.com/ind/"
ARTICLE_BASE_URL = "https://goldandglorymobile.com"

# Aktifkan intents untuk membaca channel
intents = discord.Intents.default()

class PatchBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.latest_patch_url = None

    async def on_ready(self):
        print(f'✅ Bot {self.user} sudah online!')
        await self.check_patch_updates()

    async def get_latest_patch(self):
        """Scrape halaman utama untuk mendapatkan link patch terbaru"""
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(BASE_URL, timeout=10) as response:
                    if response.status != 200:
                        print(f"⚠️ Gagal mengambil data, status: {response.status}")
                        return None, None

                    soup = BeautifulSoup(await response.text(), "html.parser")
                    latest_article = soup.find("a", class_="text-line none")

                    if latest_article and "href" in latest_article.attrs:
                        patch_url = ARTICLE_BASE_URL + latest_article["href"]
                        patch_content = await self.get_patch_content(session, patch_url)
                        return patch_url, patch_content
            except Exception as e:
                print(f"❌ Error saat mengambil patch terbaru: {e}")
        return None, None

    async def get_patch_content(self, session, patch_url):
        """Scrape halaman detail patch untuk mendapatkan isi update dengan format rapi"""
        async with session.get(patch_url, timeout=10) as response:
            if response.status != 200:
                return "⚠️ Gagal mengambil detail patch."

            soup = BeautifulSoup(await response.text(), "html.parser")
            content_div = soup.find("div", class_="article-content")  

            if content_div:
                for br in content_div.find_all("br"):
                    br.replace_with("\n")

                content_text = "\n\n".join(p.get_text(strip=True, separator="\n") for p in content_div.find_all("p"))
                return content_text.strip()
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

bot = PatchBot()
bot.run(TOKEN)
