# 🌐 Henri Tri Herdiansyah — Portfolio Website

Website portfolio personal yang dibangun dengan HTML, CSS, dan JavaScript murni tanpa framework apapun.

🔗 **Live:** [henrith.github.io/portfolio](https://henrith.github.io/portofolio-website) *(update link setelah deploy)*

---

## ✨ Fitur

- 🎨 Dark theme dengan aksen mint yang elegan
- 📱 Fully responsive — mobile, tablet, desktop
- ⚡ Animasi smooth (fade-in on scroll, hover effects)
- 📊 Skill chart interaktif menggunakan Chart.js (Radar & Bar chart)
- 🔢 Single file — tidak ada dependency build tool
- 🧭 Sticky navbar dengan efek blur saat scroll

---

## 📁 Struktur File

```
portfolio/
├── portfolio-henri.html         # Halaman utama portfolio (HTML + CSS + JS)
├── admin.html                   # Panel admin lokal untuk mengelola projects.json
├── admin.css                    # Gaya tampilan panel admin
├── projects.json                # Database data proyek dalam format JSON
├── cv.html                      # Source CV interaktif (optimasi cetak A4)
├── generate_cv.py               # Skrip otomatisasi kompilasi HTML ke PDF
├── CV-Henri-Tri-Herdiansyah.pdf # Hasil ekspor PDF CV ter-update
├── henri.jpeg                   # Foto profil tentang saya
├── henri-hero.jpeg              # Foto banner hero
└── README.md                    # Dokumentasi repositori
```

---

## 🛠️ Teknologi

| Teknologi | Kegunaan |
|-----------|----------|
| HTML5 | Struktur halaman |
| CSS3 | Styling, animasi, layout (Grid & Flexbox) |
| JavaScript (Vanilla) | Interaktivitas, scroll observer |
| Chart.js 4.4.0 | Visualisasi skill (via CDN) |
| Google Fonts | Tipografi (Inter + Space Grotesk) |

---

## 🚀 Cara Menjalankan

Tidak perlu install apapun. Cukup:

1. Clone repo ini
```bash
git clone https://github.com/Henrith14/portofolio-website.git
```

2. Buka file `portfolio-henri.html` langsung di browser

Atau buka lewat Live Server di VS Code untuk pengalaman development yang lebih baik.

---

## 📂 Sections

| Section | Isi |
|---------|-----|
| Hero | Nama, tagline, CTA button |
| Tentang | Foto, bio, detail personal |
| Pengalaman | Timeline kerja & organisasi |
| Skills | Tech stack + chart visualisasi |
| Proyek | Card proyek dengan deskripsi & link |
| Kontak | Email & Instagram |

---

## 📄 Pembaruan & Kompilasi CV

CV Anda dikelola secara lokal menggunakan HTML (`cv.html`) agar mudah di-styling dan ramah sistem ATS. Untuk memperbarui dan mencetak PDF CV secara otomatis:

1. Buka dan edit file [cv.html](file:///c:/Users/henri/.vscode/web%20porto%20henri/cv.html).
2. Jalankan perintah kompilasi berikut di terminal Anda:
   ```bash
   python generate_cv.py
   ```
3. File `CV-Henri-Tri-Herdiansyah.pdf` akan ter-update secara otomatis menggunakan kompilasi headless Microsoft Edge.

---

## 📸 Preview

> Screenshot bisa ditambahkan di sini setelah deploy

---

## 👤 Author

**Henri Tri Herdiansyah**  
Mahasiswa Informatika — UPN Veteran Jawa Timur  
📧 henrith02@gmail.com  
📸 [@henrith_](https://instagram.com/henrith_)  
💻 [GitHub](https://github.com/Henrith14)
