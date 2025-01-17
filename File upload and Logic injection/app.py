from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'
UPLOAD_FOLDER = './uploads'

# Yükleme klasörü yoksa oluştur
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

users = {"user": "password"}

jobs = [
    {"id": 1, "title": "Turkcell", "accessible": True},
    {"id": 2, "title": "Vodafone", "accessible": True},
    {"id": 3, "title": "Türksat", "accessible": True},
    {"id": 4, "title": "Havelsan", "accessible": True},
    {"id": 5, "title": "Aselsan", "accessible": True},
]

def allowed_file(file):
    """
    Güvensiz hale getirildi: Her dosya türüne izin veriliyor.
    """
    return True  # Her dosya kabul edilir!

@app.route('/', methods=['GET', 'POST'])
def login():
    """
    Kullanıcı girişi.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('profile'))
        else:
            return "Login Failed"
    return render_template('login.html')

@app.route('/profile')
def profile():
    """
    Kullanıcı profili.
    """
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('profile.html', jobs=jobs)

@app.route('/jobs/<int:job_id>')
def job_page(job_id):
    """
    İş ilanı detayları.
    """
    if 'user' not in session:
        return redirect(url_for('login'))
    job = next((job for job in jobs if job['id'] == job_id), None)
    if not job or not job['accessible']:
        return "Access Denied"
    return render_template(f"{job['title'].lower()}.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    """
    Güvensiz dosya yükleme.
    """
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file):  # Tüm dosyalar kabul edilir
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            return f"File '{file.filename}' uploaded successfully!"
        else:
            return "No file uploaded."
    return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """
    Yüklenen dosyaları görüntüle.
    """
    try:
        return send_from_directory(UPLOAD_FOLDER, filename)
    except FileNotFoundError:
        return "File not found!", 404

if __name__ == '__main__':
    app.run(debug=True)
