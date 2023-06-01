class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan.NamaJurusan)
#Pada line diatas terdapat kelas dari Mahasiswa yang memiliki atribut nama , nim dan objek jurusan Sesuai yang diminta pada soal 
#Metode __init__(self, nama, nim, jurusan) digunakan sebagai konstruktor untuk menginisialisasi objek Mahasiswa dengan atribut-atribut yang diberikan saat objek dibuat.
#Metode tampilkan_info(self) digunakan untuk mencetak informasi mahasiswa, yaitu nama, NIM, dan nama jurusan.
#Dalam metode tampilkan_info(self), atribut jurusan dari objek Mahasiswa diakses menggunakan self.jurusan.NamaJurusan.
#Ini mengasumsikan bahwa objek jurusan yang diberikan saat objek Mahasiswa dibuat adalah objek dari kelas Jurusan, yang memiliki atribut NamaJurusan.

class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        if len(self.DaftarMahasiswa) > 0:
            print("Daftar Mahasiswa di Jurusan", self.NamaJurusan)
            for mahasiswa in self.DaftarMahasiswa:
                print("- Nama:", mahasiswa.nama)
                print("  NIM:", mahasiswa.nim)
                print()
        else:
            print("Tidak ada mahasiswa terdaftar di Jurusan", self.NamaJurusan)

#Kode di atas adalah definisi dari kelas Jurusan. 
#Kelas ini memiliki atribut NamaJurusan yang menyimpan nama jurusan, dan DaftarMahasiswa yang merupakan daftar mahasiswa yang terdaftar di jurusan tersebut.
#__init__(self, nama_jurusan): Metode ini merupakan konstruktor yang akan dipanggil saat objek Jurusan dibuat. 
# Ia menginisialisasi atribut NamaJurusan dengan nilai yang diberikan dan DaftarMahasiswa dengan sebuah daftar kosong.
#tambah_mahasiswa(self, mahasiswa): Metode ini digunakan untuk menambahkan objek Mahasiswa ke dalam daftar DaftarMahasiswa jurusan ini. 
#Objek mahasiswa yang diberikan akan ditambahkan ke dalam daftar.

class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []

    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        if len(self.DaftarJurusan) > 0:
            print("Daftar Jurusan di Universitas", self.NamaUniversitas)
            for jurusan in self.DaftarJurusan:
                print("- Nama Jurusan:", jurusan.NamaJurusan)
                print()
        else:
            print("Tidak ada jurusan terdaftar di Universitas", self.NamaUniversitas)
#Kode di atas adalah definisi dari kelas Universitas.
#Kelas ini memiliki atribut NamaUniversitas yang menyimpan nama universitas, dan DaftarJurusan yang merupakan daftar jurusan yang ada di universitas tersebut.
#init__(self, nama_universitas): Metode ini merupakan konstruktor yang akan dipanggil saat objek Universitas dibuat. 
#Ia menginisialisasi atribut NamaUniversitas dengan nilai yang diberikan dan DaftarJurusan dengan sebuah daftar kosong.

# 1. Buat objek Universitas dengan nama "XYZ University"
xyz_university = Universitas("XYZ University")

# 2. Buat objek Jurusan dengan nama "Teknik Informatika" dan tambahkan objek tersebut ke dalam Universitas XYZ
teknik_informatika = Jurusan("Teknik Informatika")
xyz_university.tambah_jurusan(teknik_informatika)


while True:
    nama_mahasiswa = input("Masukkan nama mahasiswa (kosongkan untuk mengakhiri): ")
    if not nama_mahasiswa:
        break
    nim_mahasiswa = input("Masukkan NIM mahasiswa: ")
    mahasiswa = Mahasiswa(nama_mahasiswa, nim_mahasiswa, teknik_informatika)
    teknik_informatika.tambah_mahasiswa(mahasiswa)
#Pada kode diatas saya menggunakan perulangan untuk membuat muser memasukkan nama mereka sendiri kedalam input
#Kemudian itu user juga diminta untuk memasukkan NIM 
#Barulah setelah itu data tersebut ditambahkan kemudian akan dicetak setelah user mengakhiri loop dengan cara mengosongkan Input nama .

# 4. Tampilkan daftar jurusan yang ada di Universitas XYZ
xyz_university.tampilkan_daftar_jurusan()

# 5. Tampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ
teknik_informatika.tampilkan_daftar_mahasiswa()
