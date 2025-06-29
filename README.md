# OCR + Ollama Demo

Proyek ini adalah aplikasi web sederhana yang menggabungkan OCR (Optical Character Recognition) dan Large Language Model (LLM) menggunakan FastAPI (Python) di backend dan Vue.js di frontend.

---

## Fitur
- Upload gambar dari frontend
- Ekstraksi teks dari gambar menggunakan OCR di backend (`main.py`)
- Hasil OCR dan respons LLM ditampilkan di frontend
- UI modern dan responsif

---

## Struktur Project
```
ocr/
  main.py            # Backend FastAPI untuk OCR & LLM
  requirements.txt   # Dependensi backend
  frontend/          # Frontend Vue.js (Vite)
    src/App.vue      # Komponen utama
    ...
rag/
  app.py             # (Opsional, untuk fitur lain)
```

---

## Cara Menjalankan Backend (FastAPI)
1. Masuk ke folder `ocr`:
   ```bash
   cd ocr
   ```
2. Aktifkan virtual environment (opsional):
   ```bash
   .\env\Scripts\activate
   ```
3. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan server FastAPI:
   ```bash
   uvicorn main:app --reload
   ```

---

## Cara Menjalankan Frontend (Vue.js)
1. Masuk ke folder frontend:
   ```bash
   cd ocr/frontend
   ```
2. Install dependensi:
   ```bash
   npm install
   ```
3. Jalankan development server:
   ```bash
   npm run dev
   ```
4. Buka browser ke alamat yang tertera (biasanya http://localhost:5173)

---

## Konfigurasi
- Pastikan backend berjalan di `http://localhost:8000`
- Endpoint upload gambar: `POST /ocr`
- Frontend akan otomatis mengirim file ke backend dan menampilkan hasilnya

---

## Lisensi
MIT
