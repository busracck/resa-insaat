from flask import Flask, render_template,request,redirect,send_from_directory
import os

app = Flask(__name__,static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

# Formun gideceği adres (Zekioğlu'ndaki gibi)
@app.route('/mesajlari-oku', methods=['POST'])
def mesajlari_oku():
    if request.method == 'POST':
        # Formdan gelen verileri al
        isim = request.form.get('ad_soyad')
        email = request.form.get('email')
        telefon = request.form.get('telefon')
        mesaj = request.form.get('mesaj')
        
        # BURADA NORMALDE MAİL GÖNDERME KODU OLUR
        # Şimdilik sadece terminale yazdıralım ki hata vermesin
        print(f"Yeni Mesaj: {isim} - {email} - {mesaj}")
        
        # İşlem bitince teşekkür sayfasına veya anasayfaya yönlendir
        return redirect('/contact.html')

if __name__ == '__main__':
    app.run(debug=True)