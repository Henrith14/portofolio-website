import subprocess
import os

def generate_pdf():
    # Mengambil direktori saat ini
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_html = os.path.join(current_dir, "cv.html")
    output_pdf = os.path.join(current_dir, "CV-Henri-Tri-Herdiansyah.pdf")
    
    # Path standar Microsoft Edge di Windows
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    
    # Validasi keberadaan file Edge & HTML input
    if not os.path.exists(edge_path):
        print(f"Error: Microsoft Edge tidak ditemukan di '{edge_path}'.")
        return
    if not os.path.exists(input_html):
        print(f"Error: Input file '{input_html}' tidak ditemukan.")
        return
        
    print(f"Membuka '{input_html}'...")
    print(f"Menjalankan kompilasi headless Microsoft Edge untuk membuat PDF...")
    
    # Perintah CLI Edge untuk mencetak HTML ke PDF
    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--print-to-pdf-no-header",  # Meniadakan header (tanggal/judul) dan footer (url/halaman) default browser
        f"--print-to-pdf={output_pdf}",
        input_html
    ]
    
    try:
        # Menjalankan proses kompilasi
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        if os.path.exists(output_pdf):
            size_kb = os.path.getsize(output_pdf) / 1024
            print(f"\n[SUKSES] PDF berhasil dibuat!")
            print(f"Path: {output_pdf}")
            print(f"Ukuran File: {size_kb:.2f} KB")
        else:
            print("\n[EROR] Proses selesai tetapi file PDF tidak ditemukan.")
    except subprocess.CalledProcessError as e:
        print("\n[EROR] Gagal menjalankan Microsoft Edge untuk kompilasi PDF:")
        print(e.stderr)

if __name__ == "__main__":
    generate_pdf()
