# ARCANA AI By AL Musawiru

## Tentang ARCANA AI :
ARCANA AI adalah sebuah aplikasi ai lokal yang dibuat menggunakan python. Aplikasi ini menggunakan model "Phi-3-mini-4k-instruct-q4.gguf" yang dikembangkan oleh Microsoft. Model ini dipilih karena memiliki kemampuan yang sangat pas untuk kebutuhan proyek ini. Berikut kemampuannya : 

### 🔍 Kemampuan Utama
- Pemrosesan bahasa alami (Natural Language Processing / NLP)
- Pemahaman konteks percakapan
- Pembuatan teks otomatis dan ringkasan
- Dukungan prompt dalam Bahasa Indonesia dan Inggris

Aplikasi ini juga dirancang agar dapat berjalan di komputer lokal tanpa koneksi internet.

## Rancangan : 
Aplikasi ini dibuat menggunakan runtime dan bahasa pemrograman python + lib customthinter oleh Tom Schimansky untuk user interface-nya. Aplikasi ini menggunakan llama-cpp-python dikembangkan oleh Andrei Shlyakhov untuk memuat model lokal. Di aplikasi ini juga menggunakan lib psutil oleh Giampaolo Rodola untuk mengambil informasi dan mengontrol proses serta penggunaan sumber daya sistem seperti CPU, RAM, disk, dan jaringan.

## Cara Mengemas Dan Menjalankan
- Install python 3.12
- Download dan ekstrak file ARCANA-AI.zip lalu masuk ke dalam folder tersebut.
- Buka terminal dan masuk ke direktori projek.
- Jalankan perintah "env\scripts\activate" jika pakai cmd untuk menjalankan virtual environment.
- Untuk menjalankan aplikasi jalankan perintah "python main.py" di terminal.
- Jika ingin mengemas jalankan perintah "pyinstaller main.py --name ArcanaAI --onedir --noconfirm --noconsole --add-data "assets;assets" --add-data "model;model" --collect-all llama_cpp --collect-all customtkinter --icon assets/logo.ico" di terminal.

## Informasi penting
Karena ai dimuat di komputer lokal. Jadi perlu spek pc yang mempuni untuk menjalankan. PC yang digunakan dalam pengembangan sebagai berikut :
- OS : Windows 11 Home
- CPU : Intel Core i5 Gen 12
- RAM : 16 Gb
- Menggunakan VGA On Board

Spek PC yang dapat digunakan :
- OS : Windows 10/11
- CPU : intel core i3 gen 6 +
- RAM : 8 GB +

## Kontributor
- Al Musawiru — Developer utama proyek

## Lisensi
Proyek ini dilisensikan di bawah MIT License. Bebas digunakan, dimodifikasi, dan dikembangkan kembali dengan tetap mencantumkan atribusi.

## Terima kasih atas perhatiannya
Terima kasih telah menggunakan ARCANA AI. Semoga aplikasi ini bermanfaat untuk pengembangan teknologi AI lokal di Indonesia.