from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__, template_folder='File')

PRICE_KERIPIK_KACA = 3000
PRICE_BASRENG = 4000
PRICE_MAKARONI = 3500
PRICE_KERIPIK_SINGKONG = 2500


@app.route('/', methods=['GET'])
def home():
    return render_template('snackaroo_custom_slideshow_orientation.html')

@app.route('/order', methods=['GET'])
def order():
    return render_template('order_orientation.html')

@app.route('/receipt', methods=['POST'])
def receipt():
    nama = request.form.get('nama')
    email = request.form.get('email')
    telepon = request.form.get('telepon')
    produk = request.form.get('produk')
    jumlah = request.form.get('jumlah')
    alamat = request.form.get('alamat')
    pengantaran = request.form.get('pengantaran')

    try:
        jumlah_int = int(jumlah)
    except (TypeError, ValueError):
        jumlah_int = 0

    total_harga = 0
    discount = 0
    ongkir = 0
    if produk == 'keripik-kaca' and jumlah_int > 0:
        total_harga = PRICE_KERIPIK_KACA * jumlah_int
        if jumlah_int == 10:
            discount = total_harga * 0.10
        if jumlah_int < 3 and pengantaran == 'ambil':
            ongkir = 0
        elif pengantaran == 'antar':
            ongkir = 3000

    if produk == 'basreng' and jumlah_int > 0:
        total_harga = PRICE_BASRENG * jumlah_int
        if jumlah_int == 10:
            discount = total_harga * 0.10
        if jumlah_int < 3 and pengantaran == 'ambil':
            ongkir = 0
        elif pengantaran == 'antar':
            ongkir = 3000

    if produk == 'makaroni' and jumlah_int > 0:
        total_harga = PRICE_MAKARONI * jumlah_int
        if jumlah_int == 10:
            discount = total_harga * 0.10
        if jumlah_int < 3 and pengantaran == 'ambil':
            ongkir = 0
        elif pengantaran == 'antar':
            ongkir = 3000

    if produk == 'keripik-singkong' and jumlah_int > 0:
        total_harga = PRICE_KERIPIK_SINGKONG * jumlah_int
        if jumlah_int == 10:
            discount = total_harga * 0.10
        if jumlah_int < 3 and pengantaran == 'ambil':
            ongkir = 0
        elif pengantaran == 'antar':
            ongkir = 3000

    subtotal = total_harga
    total_harga_diskon = total_harga - discount + ongkir

    subtotal_formatted = f"{subtotal:,}"
    discount_formatted = f"{int(discount):,}"
    ongkir_formatted = f"{ongkir:,}"
    total_harga_diskon_formatted = f"{int(total_harga_diskon):,}"

    current_datetime = datetime.now()
    date_str = current_datetime.strftime("%d-%m-%Y")
    time_str = current_datetime.strftime("%H:%M:%S")

    kode_unik = f"Snackaroo-{nama}-{date_str}-{produk}"

    return render_template('receipt_orientation.html', nama=nama, email=email, telepon=telepon,
                           produk=produk, jumlah=jumlah_int, alamat=alamat,
                           pengantaran=pengantaran, subtotal_formatted=subtotal_formatted,
                           discount_formatted=discount_formatted, ongkir_formatted=ongkir_formatted,
                           total_harga_diskon_formatted=total_harga_diskon_formatted,
                           date_str=date_str, time_str=time_str, kode_unik=kode_unik)

if __name__ == '__main__':
    app.run(debug=True)
