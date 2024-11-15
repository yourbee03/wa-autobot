import pywhatkit
import pandas as pd
import win32clipboard
import time

contacts_df = pd.read_excel('kontak.xlsx')

# Template pesan yang mau dikirim
message_template = """
🎉 Contoh Template 🎉

Halo, {name}! 
Ini contoh Template yang ada, silahkan sesuaikan dengan kebutuhan anda 😁

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
