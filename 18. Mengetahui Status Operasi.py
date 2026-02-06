import tkinter as tk
from tkinter import messagebox

def operation_status(success):
    if success:
        messagebox.showinfo("Status", "Operasi berhasil!")
    else:
        messagebox.showerror("Status", "Operasi gagal!")

window = tk.Tk()
status_button = tk.Button(window, text="Cek Status Operasi", command=lambda: operation_status(True))
status_button.pack(pady=10)
window.mainloop()
# Fungsi: Mengetahui status operasi dan memberi feedback berdasarkan hasilnya.
# Kondisi: Ketika Anda ingin memantau hasil dari suatu operasi.