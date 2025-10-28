# Arcana-Ai_Ai-local-loader

Selamat datang di **Arcana-Ai**! Aplikasi AI Loader sederhana yang memungkinkan Anda memuat dan berinteraksi dengan model AI (GGUF) secara lokal di komputer Anda.

Aplikasi ini dibangun murni dengan Python, menggunakan `customtkinter` untuk antarmuka pengguna (GUI) yang modern dan `llama-cpp-python` untuk inferensi AI yang cepat dan efisien di CPU (atau GPU jika didukung).

---

## ✨ Fitur

* **Antarmuka Modern:** GUI yang bersih dan responsif dibangun dengan `customtkinter`.
* **Lokal & Privat:** Semua pemrosesan AI berjalan 100% di mesin Anda. Tidak ada data yang dikirim ke server eksternal.
* **Performa Tinggi:** Didukung oleh `llama-cpp-python` yang dioptimalkan untuk inferensi model LLM.
* **Mudah Digunakan:** Cukup unduh model GGUF, muat di aplikasi, dan mulai berinteraksi.

---

## 🛠️ Instalasi

Untuk menjalankan aplikasi ini, Anda memerlukan Python 3.10+ dan beberapa alat bantu build C++.

### 1. Prasyarat: C++ Build Tools (Wajib)

`llama-cpp-python` perlu mengkompilasi (build) beberapa bagian dari source code. Di Windows, ini memerlukan C++ build tools dari Visual Studio.

1.  Kunjungi halaman [Visual Studio Downloads](https://visualstudio.microsoft.com/downloads/).
2.  Unduh **Build Tools for Visual Studio**. (Anda juga bisa menggunakan installer "Visual Studio Community", tetapi Build Tools lebih ringan jika Anda tidak butuh IDE lengkap).
3.  Jalankan installer.
4.  Di tab "Workloads", centang **"Desktop development with C++"**.
    
5.  Klik "Install" dan tunggu prosesnya selesai.

### 2. Instalasi Proyek

Setelah prasyarat terpenuhi, ikuti langkah-langkah berikut:

1.  **Clone repositori ini:**
    ```bash
    git clone [https://github.com/(USERNAME)/(NAMA_REPO).git](https://github.com/(USERNAME)/(NAMA_REPO).git)
    cd (NAMA_REPO)
    ```

2.  **Buat Virtual Environment (Sangat disarankan):**
    ```bash
    python -m venv venv
    ```

3.  **Aktifkan Virtual Environment:**
    * Di Windows (CMD/PowerShell):
        ```bash
        .\venv\Scripts\activate
        ```
    * Di macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Instal semua dependensi:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Ini akan otomatis menginstal `customtkinter` dan `llama-cpp-python`. Proses instalasi `llama-cpp-python` mungkin memakan waktu beberapa menit karena perlu kompilasi).*

---

## 🚀 Penggunaan

1.  Pastikan virtual environment Anda sudah aktif (lihat langkah instalasi).
2.  Jalankan aplikasi:
    ```bash
    python main.py
    ```

3.  **Dapatkan Model:**
    Aplikasi ini dirancang untuk memuat model dalam format **GGUF**. Anda dapat mengunduh model GGUF yang kompatibel (misalnya, Llama 3, Mistral, dll.) dari [Hugging Face](https://huggingface.co/models?search=gguf).

4.  Di dalam aplikasi, gunakan tombol "Load Model" (atau yang serupa) untuk memilih file `.gguf` yang telah Anda unduh.

---

## 🤝 Kontribusi

Kontribusi sangat kami hargai! Jika Anda menemukan bug atau ingin menambahkan fitur baru, silakan ikuti langkah-langkah berikut:

1.  **Fork** repositori ini.
2.  Buat branch baru (`git checkout -b fitur/FiturKeren`).
3.  Pastikan Anda telah mengikuti **Langkah Instalasi** di atas dengan benar, terutama bagian **Prasyarat C++ Build Tools**, karena ini penting untuk pengembangan.
4.  Lakukan perubahan Anda dan buat commit (`git commit -m 'Menambahkan FiturKeren'`).
5.  Push ke branch Anda (`git push origin fitur/FiturKeren`).
6.  Buka **Pull Request**.

---

## 📜 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
