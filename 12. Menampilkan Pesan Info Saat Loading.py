import tkinter as tk
from tkinter import messagebox
import time

def show_loading_info():
    messagebox.showinfo("Loading", "Loading data, harap tunggu...")
    time.sleep(2)  # Simulasi waktu loading
    print("Loading selesai!")

window = tk.Tk()
window.withdraw()
show_loading_info()
window.mainloop()
# Fungsi: Menampilkan pesan saat ada proses loading.
# Kondisi: Ketika Anda ingin memberi tahu pengguna bahwa proses sedang berlangsung.