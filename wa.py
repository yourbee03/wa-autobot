import pywhatkit
import pandas as pd
import win32clipboard
import time

contacts_df = pd.read_excel('kontak.xlsx')

# Template pesan yang mau dikirim
message_template = """
🎉 Mulai Langkah Pertama Kamu di Pengembangan Web dengan Laravel! 🎉

Halo, {name}! 👨‍💻👩‍💻 Siapa yang siap membangun aplikasi web pertama mereka dengan Laravel? Yuk, gabung ke Workshop Laravel Fundamentals Inatechno Batch 1 (LWI-Batch1)! 💻🔥

Di workshop ini, kamu akan belajar langsung tentang dasar-dasar Laravel dan cara membuat aplikasi web dari awal. Kita akan membahas:

✨ Dasar-Dasar Pengembangan Web dengan Laravel
✨ Fitur-Fitur Inti Laravel dan Penerapannya
✨ Dari Nol hingga CRUD Lengkap dalam Beberapa Langkah

Catat tanggal pentingnya yaa! 📅 Sabtu, 16 November 2024
📍 Nutrihub Padang & Via Zoom
⏰ 09:00 WIB - selesai

🎟 Tempat Terbatas! Dapatkan pengalaman langsung, akses materi, sertifikat, dan networking dengan peserta lainnya.
🔗 Daftar sekarang: bit.ly/LWI-batch1

Jangan lewatkan kesempatan ini untuk membangun keterampilan Laravel dan memulai perjalananmu di pengembangan web! 🚀

#LaravelWorkshop #Inatechno #WebDevelopment #CodingSkills #FastLearning
"""

# lokasi gambar
image_path = r'a.jpg'

# Fungsi untuk mengirim pesan
def send_whatsapp_message(name, phone_number):
    message = message_template.format(name=name)
    
    # Kirim gambar dengan teks sebagai keterangan
    pywhatkit.sendwhats_image(f"+{phone_number}", image_path, caption=message)
    print(f"Gambar dengan pesan terkirim ke {name} di nomor {phone_number}")

# Loop melalui setiap kontak di file Excel
for index, row in contacts_df.iterrows():
    name = row.iloc[0]
    phone_number = row.iloc[1]
    
    send_whatsapp_message(name, phone_number)
    time.sleep(5)

print("Semua pesan telah terkirim!")
