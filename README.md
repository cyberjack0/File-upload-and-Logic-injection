# File-upload-and-Logic-injection
# Flask File Upload Vulnerability Project / Flask Dosya Yükleme Zafiyeti Projesi

This project demonstrates both **vulnerable** and **secure** file upload systems using Flask. It is intended for educational and testing purposes.

Bu proje, Flask tabanlı bir dosya yükleme sisteminin hem **zararlı** hem de **güvenli** varyasyonlarını simüle etmek amacıyla geliştirilmiştir. Eğitim ve test amaçlıdır.

---

## 🚩 Purpose / Amaç
This project includes two scenarios:  
Bu proje iki senaryo içerir:

1. **Vulnerable Scenario**: A structure where all file types are uploaded and processed without control.  
   **Zafiyetli Senaryo**: Tüm dosya türlerinin yüklendiği ve kontrolsüz olarak işlendiği bir yapı.
2. **Secure Scenario**: A structure where only specific file types are accepted, with MIME type and extension checks.  
   **Güvenli Senaryo**: Yalnızca belirli dosya türlerinin kabul edildiği, MIME türü ve uzantı kontrollerinin yapıldığı bir yapı.

---

## ⚠️ Vulnerable Structure / Zafiyetli Yapı
**Vulnerable Scenario**:  
**Zafiyetli Senaryo**:

- The system accepts any file type without checking the file's type or content.  
  Sistem, dosyanın türüne veya içeriğine bakmaksızın tüm dosya türlerini kabul eder.
- No MIME type validation is performed.  
  MIME türü kontrolü yapılmaz.
- Attackers can upload malicious files (e.g., `.exe`, `.php`) to potentially compromise the system.  
  Saldırganlar, zararlı dosyalar (ör. `.exe`, `.php`) yükleyerek sistemi tehlikeye atabilir.

### Example Scenario / Örnek Senaryo
1. **File Type Vulnerability / Dosya Türü Zafiyeti**:
   - Upload `.exe` or `.php` files.  
     `.exe` veya `.php` dosyasını yükleyin.
   - When executed in an exploitable environment, malicious commands can be executed.  
     Çalıştırılabilir bir ortamda açıldığında zararlı komutlar yürütülebilir.

2. **Bypassing via Burp Suite / Burp Suite ile Manipülasyon**:
   - Modify the filename or MIME type during upload to bypass restrictions.  
     Yükleme sırasında dosya adını veya MIME türünü değiştirerek kısıtlamaları aşın.

---

## ✅ Secure Structure / Güvenli Yapı
**Secure Scenario**:  
**Güvenli Senaryo**:

- Uploaded files are checked for both MIME type and extension.  
  Yüklenen dosyalar MIME türü ve uzantısı açısından kontrol edilir.
- Only safe file types like `.txt`, `.pdf`, and `.docx` are allowed.  
  Yalnızca `.txt`, `.pdf`, ve `.docx` gibi güvenli dosya türlerine izin verilir.
- Malicious files are rejected.  
  Zararlı dosyalar reddedilir.

---

## 📂 File Structure / Dosya Yapısı
```plaintext
/
├── app.py           # Flask application / Flask uygulaması
├── uploads/         # Folder where uploaded files are stored / Yüklenen dosyaların depolandığı klasör
├── templates/       # HTML templates / HTML şablon dosyaları
├── static/          # Static files (CSS, JavaScript) / Statik dosyalar (CSS, JavaScript)
└── README.md        # Project description / Proje açıklaması

🛠️ How to Run? / Nasıl Çalıştırılır?
Install the required libraries:
Gerekli kütüphaneleri yükleyin:
bash
pip install flask python-magic

Start the Flask application:
Flask uygulamasını başlatın:
bash
python app.py

Open the following URL in your browser:
Tarayıcınızda şu adresi açın:
http://127.0.0.1:5000/
