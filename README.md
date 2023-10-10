# :airplane: Pacil Airport :airplane:

# Anggota Kelompok :family:
- Hilmy Ammar Darmawan – 2206081736 
- Irfan Kamil - 2206083400 
- Kilau Nisrina Akhyaari – 2206082051 
- Rizki Ariffudin – 2206082612 
- Rizky Prawira Negoro - 2206030956 

# Cerita aplikasi serta manfaatnya :newspaper:
Kami akan membuat aplikasi seperti “bandara”.  Akan ada loket tiket check-in, perpustakaan/reading area, café, daftar penerbangan, dan toko oleh-oleh. Aplikasi ini ditujukan agar penumpang tidak bosan saat menunggu boarding pesawat mereka. Setelah pengunjung check-in, ia bisa menunggu di café dan memesan makanan atau minuman. Pengunjung juga bisa menunggu di perpustakaan untuk membaca buku. Untuk memudahkan pengunjung men-track kapan pesawatnya akan berangkat, kami akan membuat fitur daftar penerbangan yang menampilkan data jam penerbangan, maskapai, tujuan, dan detail lainnya. Apabila pengunjung ingin check detail dan melakukan modifikasi pada profilenya, ia bisa melakukan hal tersebut di user profile page. 

Apabila user tidak login, ia hanya bisa mengakses perpustakaan, café, dan daftar penerbangan. Apabila user yang tidak login ingin membeli sesuatu di café, akan muncul pop-up yang menunjukkan bahwa ia tidak bisa membeli makanan atau minuman tersebut dan diarahkan untuk login.

User yang sudah login bisa mengakses semua fitur. Untuk membeli makanan atau minuman di café, ia bisa menggunakan saldo yang ia punya. Apabila tidak cukup, user bisa melakukan top-up saldo pada halaman user profile page. Pengunjung yang ingin melakukan check-in bisa ke loket check-in untuk melihat daftar penerbangan dan memilih penerbangan mana yang ia akan check-in. 

## Deskripsi Fitur-Fitur dalam Aplikasi :calling:

### :ticket: Loket Check-In 
Fitur ini hanya dapat diakses apabila pengguna sudah login ke aplikasi. Pada halaman check-in ini dimanfaatkan form yang meminta pengguna untuk mengisi data yang dibutuhkan dalam melakukan check in, yaitu penerbangan yang sudah dipesan, data diri seperti nama lengkap, tempat dan tanggal lahir, dan berat bagasi. Data-data tersebut akan disimpan pada model penumpang sehingga penumpang yang sudah check in tidak dapat melakukan check in lagi. Setelah berhasil check in, halaman akan berpindah ke halaman sukses check in yang akan menampilkan QR untuk verifikasi check in ke petugas di bandara. 

### :books: Perpustakaan
Terdapat kumpulan buku-buku yang dapat dipinjam oleh pengunjung. Pengunjung hanya bisa meminjam buku apabila sudah login, jika belum maka pengunjung hanya dapat melihat-lihat saja. Admin dapat menambahkan dan menghapus buku. 

### :coffee: Café
Terdapat katalog yang menampilkan menu-menu yang dijual beserta harganya. Pengunjung dapat memasukkan menu ke dalam keranjang dan hanya bisa check-out/membeli menu tersebut apabila saldo mencukupi.  

### :flight_departure: Daftar Penerbangan 
Menampilkan list dalam bentuk tabel untuk jadwal penerbangan pesawat. Pada list ini akan menampilkan data-data seperti jam berangkat, status penerbangan (boarding, take-off, dll), tujuan penerbangan, kode penerbangan, dan terminal/pintu keberangkatan. 

### :man_office_worker: User profile page
Menampilkan data pengunjung, tiket yang sudah di check-in, saldo, dan bisa melakukan top-up saldo. User bisa memodifikasi profilenya pada bagian ini. 

# :briefcase: Daftar modul
### User: 
Nama, gender, nomor telepon, email, alamat, tanggal lahir, saldo, tiket yang di check-in, password 
### Penumpang: 
Penerbangan yang dinaiki, nama lengkap, tempat dan tanggal lahir, berat bagasi penumpang, QR check-in penumpang. 
### Menu: 
Tipe (Makanan, minuman, snack), Harga 
### Penerbangan: 
Jam berangkat, status penerbangan (boarding, take-off, dll), tujuan penerbangan, kode penerbangan, dan terminal/pintu keberangkatan. 
### Perpustakaan: 
Judul buku, penulis, penerbit, tahun terbit 

# :green_book: Sumber dataset katalog buku
https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset 

# :customs: Role user
Pada aplikasi ini, kami hanya membuat dua role untuk pengguna, yaitu
## Pengunjung: 
Dapat mengakses aplikasi dengan login maupun tidak login. Jika pengunjung login, maka Ia dapat mengakses semua fitur yang tersedia pada aplikasi. Akan tetapi, jika pengunjung tidak login, pengunjung memiliki akses yang terbatas pada fitur, yaitu hanya dapat mengakses halaman cafe tanpa dapat membeli, mengakses halaman perpustakaan, dan halaman daftar penerbangan. 
## Admin: 
Untuk admin, tidak dapat mengakses halaman check in, akan tetapi dapat mengatur data penumpang yang sudah check-in, lalu data-data lainnya pada model dapat dimodifikasi oleh admin dengan mengakses setiap halaman yang menampilkan model tersebut dan mengklik tombol edit. 
