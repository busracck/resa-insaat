from flask import Flask, request, redirect, send_from_directory

app = Flask(__name__, static_folder='.')

# Mesajları hafızada tutmak için boş bir liste (Veritabanı niyetine)
mesaj_listesi = []

# Anasayfa
@app.route('/')
def index():
    return send_from_directory('.', 'indexgercek.html')

# Diğer HTML, CSS, JS dosyalarını sunmak için
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

# Formun gönderildiği yer (Kayıt İşlemi)
@app.route('/mesajlari-oku', methods=['POST'])
def mesajlari_oku():
    if request.method == 'POST':
        # Formdan gelen verileri al
        ad = request.form.get('ad_soyad')
        email = request.form.get('email')
        telefon = request.form.get('telefon')
        mesaj = request.form.get('mesaj')
        
        # Gelen mesajı listemize ekle
        mesaj_listesi.append({
            'ad': ad,
            'email': email,
            'telefon': telefon,
            'mesaj': mesaj
        })
        
        # İşlem bitince iletişim sayfasına geri gönder
        return redirect('/contact.html')

# YENİ: Mesajları Görme Sayfası (Admin Paneli)
@app.route('/admin')
def admin_paneli():
    # Basit bir HTML tablosu hazırlayalım
    html_kodlari = """
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title>Resa İnşaat - Gelen Mesajlar</title>
        <link href="css/bootstrap.min.css" rel="stylesheet">
        <style>body{padding: 50px; background-color: #f8f9fa;}</style>
    </head>
    <body>
        <div class="container">
            <h2 class="mb-4">📥 Gelen Kutusu</h2>
            <div class="card shadow">
                <div class="card-body">
                    <table class="table table-hover table-bordered">
                        <thead class="table-dark">
                            <tr>
                                <th>Ad Soyad</th>
                                <th>Email</th>
                                <th>Telefon</th>
                                <th>Mesaj</th>
                            </tr>
                        </thead>
                        <tbody>
    """
    
    # Listemizdeki mesajları tek tek tabloya ekleyelim (En yenisi en üstte olsun diye 'reversed' yaptık)
    for m in reversed(mesaj_listesi):
        html_kodlari += f"""
            <tr>
                <td>{m['ad']}</td>
                <td>{m['email']}</td>
                <td>{m['telefon']}</td>
                <td>{m['mesaj']}</td>
            </tr>
        """
        
    # HTML'in kapanış kısımları
    html_kodlari += """
                        </tbody>
                    </table>
                    
                    <div class="mt-3">
                        <p class="text-muted small">* Not: Bu mesajlar geçicidir. Site yeniden başlatılırsa silinebilir.</p>
                        <a href="/" class="btn btn-primary">Siteye Dön</a>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html_kodlari

if __name__ == '__main__':
    app.run()