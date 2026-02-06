import tkinter as tk
from tkinter import messagebox

def ask_feedback():
    messagebox.showinfo("Umpan Balik", "Silakan berikan umpan balik tentang aplikasi kami.")

window = tk.Tk()
feedback_button = tk.Button(window, text="Berikan Umpan Balik", command=ask_feedback)
feedback_button.pack(pady=10)
window.mainloop()
# Fungsi: Meminta umpan balik dari pengguna setelah selesai menggunakan aplikasi.
# Kondisi: Ketika Anda ingin mengumpulkan tanggapan dari pengguna.