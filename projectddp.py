import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style

class HalamanUtama:
    def __init__(self, master):
        self.master = master
        self.master.title("Halaman Utama")

        self.style = Style()
        self.create_widgets()

    def create_widgets(self):
        self.style.configure('.', font=('Helvetica', 12))
        tk.Label(self.master, text="Welcome To Nurul Fikri Grade Academic Aplication", font=('Helvetica', 18, 'bold')).pack(pady=20)

class PenghitungIPKApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Penghitung IPK")

        self.matakuliah_var = tk.StringVar()
        self.kehadiran_var = tk.DoubleVar()
        self.uts_var = tk.DoubleVar()
        self.uas_var = tk.DoubleVar()
        self.harian_var = tk.DoubleVar()

        # Bobot matakuliah (sesuaikan dengan kebijakan akademik)
        self.bobot_matakuliah = {
            "Pempgraman Web 1": {"kehadiran": 0.2, "uts": 0.3, "uas": 0.4, "harian": 0.1},
            "Dasar Dasar Pemograman": {"kehadiran": 0.1, "uts": 0.4, "uas": 0.3, "harian": 0.2},
            "Sistem Operasi": {"kehadiran": 0.3, "uts": 0.2, "uas": 0.2, "harian": 0.3},
            "Dasar Dasar Pemograman": {"kehadiran": 0.2, "uts": 0.3, "uas": 0.3, "harian": 0.2},
            "Matematika Komputer": {"kehadiran": 0.1, "uts": 0.3, "uas": 0.4, "harian": 0.2},
            "Bahasa Indonesia": {"kehadiran": 0.2, "uts": 0.3, "uas": 0.4, "harian": 0.1},
            "Pembentukan Karakter": {"kehadiran": 0.2, "uts": 0.3, "uas": 0.3, "harian": 0.2},
            "Pendidikan Agama Islam": {"kehadiran": 0.1, "uts": 0.4, "uas": 0.4, "harian": 0.1},
        }

        # Inisialisasi tema dari ttkbootstrap
        self.style = Style(theme='superhero') 
        self.create_widgets()

    def create_widgets(self):
        self.style.configure('.', font=('Helvetica', 12))  # Konfigurasi font default

        # Label dan Combobox untuk Matakuliah
        tk.Label(self.master, text="Pilih Matakuliah:").pack()
        matakuliah_options = list(self.bobot_matakuliah.keys())
        matakuliah_combobox = ttk.Combobox(self.master, textvariable=self.matakuliah_var, values=matakuliah_options)
        matakuliah_combobox.pack()

        # Label dan Entry untuk Kehadiran
        tk.Label(self.master, text="Kehadiran:").pack()
        tk.Entry(self.master, textvariable=self.kehadiran_var).pack()

        # Label dan Entry untuk UTS
        tk.Label(self.master, text="Nilai UTS:").pack()
        tk.Entry(self.master, textvariable=self.uts_var).pack()

        # Label dan Entry untuk UAS
        tk.Label(self.master, text="Nilai UAS:").pack()
        tk.Entry(self.master, textvariable=self.uas_var).pack()

        # Label dan Entry untuk Nilai Harian
        tk.Label(self.master, text="Nilai Harian:").pack()
        tk.Entry(self.master, textvariable=self.harian_var).pack()

        # Tombol Hitung IPK
        tk.Button(self.master, text="Hitung IPK", command=self.hitung_ipk).pack(pady=10)

    def hitung_ipk(self):
        try:
            # Lakukan perhitungan IPK sesuai bobot komponen matakuliah yang dipilih
            matakuliah = self.matakuliah_var.get()
            kehadiran = self.kehadiran_var.get()
            uts = self.uts_var.get()
            uas = self.uas_var.get()
            harian = self.harian_var.get()

            # Ambil bobot matakuliah yang dipilih
            bobot_matakuliah = self.bobot_matakuliah.get(matakuliah, {})

            # Pastikan matakuliah yang dipilih memiliki bobot
            if not bobot_matakuliah:
                messagebox.showerror("Error", "Matakuliah tidak valid.")
                return

            # Hitung IPK dalam skala 4.0
            skala_100_to_4 = 4.0 / 100.0
            ipk = (kehadiran * bobot_matakuliah["kehadiran"] +
                   uts * bobot_matakuliah["uts"] +
                   uas * bobot_matakuliah["uas"] +
                   harian * bobot_matakuliah["harian"]) * skala_100_to_4

            # Pastikan IPK tidak melebihi 4.0
            ipk = min(ipk, 4.0)

            if ipk < 2.0:
                deskripsi = "IPK Anda buruk."
            elif ipk < 3.5:
                deskripsi = "IPK Anda baik."
            elif ipk < 4.0:
                deskripsi = "IPK Anda sangat baik."
            else:
                deskripsi = "Selamat, Anda mendapat predikat cum laude!"


            # Tampilkan hasil
            messagebox.showinfo("Hasil IPK", f"IPK Anda ({matakuliah}): {ipk:.2f}\n{deskripsi}")

        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HalamanUtama(root)
    app = PenghitungIPKApp(root)
    root.mainloop()

    