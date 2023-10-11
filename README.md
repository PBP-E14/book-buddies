# 📚 Book Buddies 📚

# Anggota Kelompok :family:
- Hilmy Ammar Darmawan – 2206081736 
- Irfan Kamil - 2206083400 
- Kilau Nisrina Akhyaari – 2206082051 
- Rizki Ariffudin – 2206082612 
- Rizky Prawira Negoro - 2206030956 

# Cerita aplikasi serta manfaatnya :newspaper:
Kami akan membuat aplikasi book club bernama Book Buddies. Pada aplikasi kami akan ada katalog buku, dimana user bisa melihat-lihat buku yang tersedia. Akan ada detail buku seperti judul, penulis, tahun terbit, dan penerbit. Lalu, apabila user ingin menandakan buku untuk dibaca di kemudian hari, user bisa menandakannya dan bisa cek buku apa saja yang sudah ditandai untuk dibaca di halaman wishlist.  

User yang ingin memberikan ulasan untuk suatu buku bisa melakukannya dalam fitur review yang kami buat. User lain bisa melihat review yang sudah di post oleh user lain. Karena aplikasi kami adalah book club, kami akan membuat forum diskusi agar para user bisa mendiskusikan topik-topik terkait buku yang sedang dibaca, buku yang sedang populer, dan lainnya.  

Aplikasi kami juga ada user profile page yang menampilkan data user seperti nama, tanggal lahir, nomor telepon, email, domisili, dan bio. Akan ada history buku-buku yang sudah dibaca oleh user. 

"Book Buddies" menawarkan platform yang komprehensif bagi para pecinta buku untuk menjelajahi, berbagi, dan mendiskusikan bacaan mereka dengan komunitas yang bersemangat. Dengan berbagai fitur yang mendukung, aplikasi ini dapat meningkatkan minat baca user dan memperkaya pengalaman literasi mereka. Melalui diskusi dan interaksi di forum, user dapat membangun network dengan pembaca lain yang memiliki minat dan selera yang serupa.

## Daftar dan Deskripsi Modul dalam Aplikasi :calling:

### 💬 Forum Diskusi 
Cara kerja forum diskusi pada aplikasi kami sebenarnya mirip dengan forum diskusi di kebanyakan aplikasi. Setiap pengguna dapat mengirimkan pesan dan terdapat beberapa pilihan diskusi yang dapat dipilih pengguna. Pilihan diskusi dapat ditambahkan oleh semua user. Tampilan pada fitur ini adalah massage-massage box yang berisi pesan-pesan para pengguna.

### :books: Katalog buku
Berisi kumpulan buku dan detail dari buku tersebut. Kumpulan buku dapat ditambah, kurang, dan edit dengan admin.

### 🧾 Review
User dapat memberikan ulasan terhadap suatu buku yang telah dibacanya. Selain itu, User juga dapat membaca ulasan-ulasan yang telah diberikan oleh user lain.

### 🔖 Wishlist 
Dapat diakses ketika terdapat logged in user. Wishlist akan menampilkan tabel yang berisi judul buku, penulis, tahun terbit, penerbit, dan tautan (shortlink) ke fitur perpustakaan.

### :man_office_worker: User profile page
Menampilkan data user seperti nama, gender, nomor telepon, email, alamat, tanggal lahir, dan bio. User bisa mengubah data pada halaman ini. User juga bisa melihat buku-buku yang sudah pernah ia baca pada bagian history.

# :briefcase: Daftar model
### User: 
nama, gender, nomor telepon, email, alamat, tanggal lahir, buku yang pernah dibaca, password
### Message: 
Tipe diskusi, Tanggal Upload, Jumlah Balasan
### Review: 
User yang sedang log in, judul buku, isi review
### Wishlist: 
Judul buku, penulis, penerbit, tahun terbit, tautan (shortlink), dan user yang sedang log in
### Buku: 
Judul buku, penulis, penerbit, tahun terbit, cover

# :green_book: Sumber dataset katalog buku
https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset 

# :customs: Role user
## Pengunjung: 
Dapat mengakses aplikasi dengan login maupun tidak login. Jika pengunjung login, maka Ia dapat mengakses semua fitur yang tersedia pada aplikasi. Akan tetapi, jika pengunjung tidak login, pengunjung memiliki akses yang terbatas pada fitur, yaitu hanya dapat mengakses halaman katalog buku dan forum (hanya bisa melihat, tidak bisa menambahkan post ke forum).
## Admin: 
Hanya bisa mengubah katalog buku (create, edit, dan delete).
