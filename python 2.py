import random

def buat_data_quiz_ipa_random():
    """
    Membuat dan mengembalikan list berisi 10 soal kuis IPA baru yang di-generate.
    """
    quiz_data = [
        {
            "soal": "Apa nama proses hilangnya uap air dari permukaan tumbuhan, terutama melalui stomata daun?",
            "pilihan": ["A. Kondensasi", "B. Evaporasi", "C. Transpirasi", "D. Presipitasi"],
            "jawaban_benar": "C",
            "penjelasan": "Transpirasi adalah penguapan air dari permukaan tumbuhan. Ini mirip dengan berkeringat pada manusia dan berperan dalam siklus air."
        },
        {
            "soal": "Sebuah benda memiliki massa 5 kg dan percepatan 2 m/s². Berapakah gaya (force) yang bekerja pada benda tersebut (dalam Newton)?",
            "pilihan": ["A. 2.5 N", "B. 7 N", "C. 10 N", "D. 0.4 N"],
            "jawaban_benar": "C",
            "penjelasan": "Gaya dihitung menggunakan Hukum II Newton: $F = m \times a$. Jadi, $5\ kg \times 2\ m/s^2 = 10\ N$."
        },
        {
            "soal": "Di mana letak sebagian besar sistem saraf pusat (otak dan sumsum tulang belakang) dilindungi?",
            "pilihan": ["A. Rongga Perut", "B. Kerongkongan", "C. Tulang Tengkorak dan Tulang Belakang", "D. Jaringan Otot"],
            "jawaban_benar": "C",
            "penjelasan": "Otak dilindungi oleh Tulang Tengkorak (Cranium), sementara Sumsum Tulang Belakang dilindungi oleh Tulang Belakang (Vertebrae)."
        },
        {
            "soal": "Logam apakah yang bersifat cair pada suhu kamar?",
            "pilihan": ["A. Emas", "B. Timbal", "C. Raksa (Mercury)", "D. Besi"],
            "jawaban_benar": "C",
            "penjelasan": "Raksa ($Hg$) adalah satu-satunya logam yang stabil dalam bentuk cair pada suhu ruangan standar dan sering digunakan dalam termometer lama."
        },
        {
            "soal": "Apa nama unit dasar pewarisan genetik yang terletak pada kromosom?",
            "pilihan": ["A. Mitokondria", "B. Ribosom", "C. Gen", "D. Vakuola"],
            "jawaban_benar": "C",
            "penjelasan": "Gen adalah segmen DNA yang membawa instruksi untuk membuat protein tertentu, dan bertanggung jawab atas sifat yang diwariskan."
        },
        {
            "soal": "Hewan yang memiliki suhu tubuh yang berubah-ubah sesuai dengan suhu lingkungan disebut hewan...",
            "pilihan": ["A. Endoterm", "B. Homoioterm", "C. Poikiloterm", "D. Mamalia"],
            "jawaban_benar": "C",
            "penjelasan": "Hewan **Poikiloterm** (atau berdarah dingin) seperti ikan dan reptil, memiliki suhu tubuh yang bervariasi mengikuti suhu eksternal."
        },
        {
            "soal": "Dalam rangkaian listrik seri, jika satu lampu padam, apa yang terjadi pada lampu lainnya?",
            "pilihan": ["A. Tetap menyala", "B. Menyala lebih terang", "C. Ikut padam", "D. Menyala lebih redup"],
            "jawaban_benar": "C",
            "penjelasan": "Dalam rangkaian seri, arus hanya memiliki satu jalur. Jika satu komponen rusak (padam), rangkaian terbuka, dan semua komponen lain juga mati."
        },
        {
            "soal": "Bahan bakar fosil utama yang digunakan untuk menghasilkan listrik di sebagian besar pembangkit listrik tenaga uap (PLTU) adalah?",
            "pilihan": ["A. Gas Alam", "B. Biomassa", "C. Batu Bara", "D. Uranium"],
            "jawaban_benar": "C",
            "penjelasan": "Batu bara adalah sumber energi fosil padat yang paling banyak digunakan di seluruh dunia untuk memanaskan air menjadi uap guna menggerakkan turbin pembangkit listrik."
        },
        {
            "soal": "Zat apakah yang dikeluarkan oleh ginjal setelah proses penyaringan darah?",
            "pilihan": ["A. Empedu", "B. Air liur", "C. Keringat", "D. Urine"],
            "jawaban_benar": "D",
            "penjelasan": "Ginjal menyaring limbah dari darah dan mengeluarkannya dalam bentuk **urine** melalui ureter dan disimpan di kandung kemih."
        },
        {
            "soal": "Apa nama galaksi di mana Tata Surya kita berada?",
            "pilihan": ["A. Andromeda", "B. Triangulum", "C. Bima Sakti (Milky Way)", "D. Whirlpool"],
            "jawaban_benar": "C",
            "penjelasan": "Tata Surya kita, termasuk Bumi, adalah bagian dari Galaksi Bima Sakti (Milky Way), sebuah galaksi spiral besar."
        }
    ]
    # Mengacak urutan soal
    random.shuffle(quiz_data)
    return quiz_data

# --- Fungsi Inti Kuis (Sama seperti sebelumnya, memastikan sistem poin berfungsi) ---

def jalankan_quiz_ipa(quiz_data):
    """
    Menampilkan soal, mengecek jawaban, dan menghitung skor.
    """
    skor = 0
    total_soal = len(quiz_data)
    poin_per_soal = 10
    
    print("="*60)
    print("      🧪 KUIS ILMU PENGETAHUAN ALAM (Soal Baru) 🔬")
    print(f"         Total Soal: {total_soal} | Poin Maksimum: {total_soal * poin_per_soal}")
    print("="*60)
    print("Instruksi: Jawab dengan mengetik A, B, C, atau D.")
    print("-" * 60)
    
    for i, soal in enumerate(quiz_data):
        print(f"\nSOAL #{i+1}: {soal['soal']}")
        
        for pilihan in soal["pilihan"]:
            print(f"   {pilihan}")

        jawaban_user = input("Jawaban Anda (A/B/C/D): ").upper()
        
        while jawaban_user not in ['A', 'B', 'C', 'D']:
            print("❌ Input tidak valid. Mohon masukkan A, B, C, atau D.")
            jawaban_user = input("Jawaban Anda (A/B/C/D): ").upper()
            
        if jawaban_user == soal["jawaban_benar"]:
            skor += poin_per_soal
            print(f"✔️ BENAR! Anda mendapatkan +{poin_per_soal} poin.")
            print(f"   💡 Penjelasan: {soal['penjelasan']}")
        else:
            print(f"❌ SALAH. Jawaban yang benar adalah {soal['jawaban_benar']}.")
            print(f"   💡 Penjelasan: {soal['penjelasan']}")
        
        print("-" * 60)

    tampilkan_hasil_akhir(skor, total_soal, poin_per_soal)


def tampilkan_hasil_akhir(skor, total_soal, poin_per_soal):
    """
    Menghitung dan menampilkan skor akhir serta evaluasi.
    """
    skor_maksimum = total_soal * poin_per_soal
    persentase = (skor / skor_maksimum) * 100

    print("\n" + "#"*60)
    print("                 HASIL AKHIR KUIS IPA")
    print("#"*60)
    print(f"Total Soal Dijawab  : {total_soal}")
    print(f"Total Poin Anda     : {skor} dari {skor_maksimum}")
    print(f"Persentase Skor     : {persentase:.2f}%")
    
    if persentase >= 80:
        evaluasi = "Luar biasa! Penguasaan IPA Anda sangat baik. ⭐"
    elif persentase >= 50:
        evaluasi = "Cukup baik. Tingkatkan lagi pemahaman Anda! 👍"
    else:
        evaluasi = "Perlu belajar lebih keras di bidang IPA. Semangat! 💪"
        
    print(f"Evaluasi            : {evaluasi}")
    print("#"*60)

# --- Jalankan Program ---
data_kuis = buat_data_quiz_ipa_random()
jalankan_quiz_ipa(data_kuis)