import MySQLdb as mydb
import datetime

class gagian:

    def __init__(self):
        self.cek = False

    def getcek(self):
        return self.cek

    def setcek(self):
        self.cek = True

    def letcek(self):
        self.cek = False

def isiData(nim, nama, alamat):
    print("'%s','%s','%s " % (nim, nama, alamat))
    conn = mydb.connect('127.0.0.1', 'root', '', 'kampus')
    curs = conn.cursor()
    curs.execute("INSERT INTO `mahasiswa`(`nim`, `nama`, `alamat`) VALUES "
                 "('%s','%s','%s')" % (nim, nama, alamat))
    conn.commit()
    curs.close()
    conn.close()


def cekData(id):
    conn = mydb.connect('127.0.0.1', 'root', '', 'kampus')
    curs = conn.cursor()
    curs.execute("SELECT * FROM `mahasiswa` WHERE id = %s" % (id))
    rows = curs.fetchall()
    if len(rows) is not 0:
        print("%s; %s; %s; %s" % (rows[0][0],rows[0][1],rows[0][2],rows[0][3].strftime('%d %B %Y')))
    for row in rows:
        if str(row[0]) == id:
            ceks.setcek()
            print("Data ditemukan")
        else:
            print("Data tidak ditemukan")
    curs.close()
    conn.close()

def ubahData(id, nim, nama, alamat):
    conn = mydb.connect('127.0.0.1', 'root', '', 'kampus')
    curs = conn.cursor()
    try:
        curs.execute("UPDATE `mahasiswa` SET `nim`='%s',`nama`='%s',`alamat`='%s '"
                     " WHERE `id`='%s';" % (nim, nama, alamat, id))
        conn.commit()
    except:
        print(SystemError)
    curs.close()
    conn.close()

def hapusData(id):
    conn = mydb.connect('127.0.0.1', 'root', '', 'kampus')
    curs = conn.cursor()
    try:
        curs.execute("DELETE FROM `mahasiswa` WHERE `id` = '%s'" % (id))
        conn.commit()
    except:
        print(SystemError)
    curs.close()
    conn.close()

def tampilData():
    conn = mydb.connect('127.0.0.1', 'root', '', 'kampus')
    curs = conn.cursor()
    try:
        curs.execute("SELECT * FROM `mahasiswa`")
        rows = curs.fetchall()
        for row in rows:
            print("%s; %s; %s; %s" % (row[0],row[1],row[2],row[3].strftime('%d %B %Y')))
    except:
        print(SystemError)
    curs.close()
    conn.close()

def menu():
    print("Pilih Menu\n\n"
          "1.\tMengisi Data Mahasiswa\n"
          "2.\tMengubah Data Mahasiswa\n"
          "3.\tMenghapus Data Mahasiswa\n"
          "4.\tMenampilkan Data Mahasiswa\n"
          "5.\tKeluar Aplikasi\n")
    pilihan = input("Pilihan Anda : ")
    if pilihan is "1":
        print("\n\n===========Input Data============\n\n")
        nim = input("NIM\t: ")
        nama = input("Nama\t: ")
        alamat = input("Alamat\t: ")
        isiData(nim, nama, alamat )
        print("\n\n\n")
        menu()
    elif pilihan is "2":
        print("\n\n===========Ubah Data============\n\n")
        id = input("Masukkan ID data yang akan diubah : ")
        cekData(id)
        if ceks.getcek():
            nim = input("NIM\t: ")
            nama = input("Nama\t: ")
            alamat = input("Alamat\t: ")
            ubahData(id, nim, nama, alamat)
            ceks.letcek()
        else:
            print("Data tidak ditemukan")
        print("\n\n\n")
        menu()
    elif pilihan is "3":
        print("\n\n===========Hapus Data============\n\n")
        id = input("Masukkan ID data yang akan dihapus : ")
        cekData(id)
        if ceks.getcek():
            yakin = input("Yakin ingin menghapus data ini? (y/n)")
            if yakin is "y" or yakin is "Y":
                hapusData(id)
            else:
                print(" Jadikah anda hapus data ini ? ")
            ceks.letcek()
        else:
            print("Data tidak ditemukan. Kembali ke Menu")
        print("\n\n\n")
        menu()
    elif pilihan is "4":
        tampilData()
        print("\n\n\n")
        menu()
    elif pilihan is "5":
        print("Terima Kasih telah menggunakan program ini")
    else:
        print("Opsi tidak tersedia")

ceks = gagian()
menu()
