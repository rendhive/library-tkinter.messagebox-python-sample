import tkinter as tk
from tkinter import messagebox

def show_temp_message():
    messagebox.showinfo("Pesan Sementara", "Ini pesan sementara.")
    window.after(2000, window.quit)  # Menutup jendela setelah 2 detik

window = tk.Tk()
window.withdraw()  # Menyembunyikan jendela utama
show_temp_message()
window.mainloop()
# Fungsi: Menampilkan pesan yang otomatis menutup setelah waktu tertentu.
# Kondisi: Ketika Anda ingin menyampaikan informasi secepat tanpa perlu interaksi.