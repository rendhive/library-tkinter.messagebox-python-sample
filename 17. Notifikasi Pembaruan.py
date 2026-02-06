import tkinter as tk
from tkinter import messagebox

def notify_update():
    messagebox.showinfo("Pembaruan", "Aplikasi telah diperbarui ke versi terbaru.")

window = tk.Tk()
update_button = tk.Button(window, text="Cek Pembaruan", command=notify_update)
update_button.pack(pady=10)
window.mainloop()
# Fungsi: Memberikan notifikasi ketika ada pembaruan pada aplikasi.
# Kondisi: Ketika Anda ingin memberi tahu pengguna tentang pembaruan yang penting