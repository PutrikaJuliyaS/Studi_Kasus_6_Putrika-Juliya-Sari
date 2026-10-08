#memilih menggunakan format penyimpan JSON atau CSV
import json
import os

NILAI_MHS= 'SK6.json'

def muat_data():
    if not os.path.exists(NILAI_MHS):
        return []
    with open(NILAI_MHS, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
                    return []

def simpan_data(data_nilai):
    with open(NILAI_MHS, 'w') as file:
        json.dump(data_nilai, file, indent=4)

#fitur untuk membaca dan menampilkan seluruh data nilai yang ada di file
def tampilkan_data(data_nilai):
    if not data_nilai:
        print("\nbelum ada data nilai")
    else:
        print("\nREKAP NILAI MAHASISWA")
        print(f"{'nama'} - {'nim'} - {'nilai'}")
        
        for mhs in data_nilai:
            print(f"{mhs['nama']} - {mhs['nim']} - {mhs['nilai']}")

#fitur untuk menambahkan rekap nilai baru.
def tambah_data(data_nilai):
    print("\nTAMBAH DATA NILAI")
    nama = input("nama mahasiswa: ")
    nim = input("nim: ")
    while True:
        try:
            nilai = float(input("nilai: "))
            break
        except ValueError:
            print("masukkan angka nilai")
    
#data nilai baru berhasil ditambahkan atau di-append ke dalam file dan tersimpan
    data_baru = {
        "nama": nama,
        "nim": nim,
        "nilai": nilai
    }
    data_nilai.append(data_baru)
    simpan_data(data_nilai)
    print("data nilai berhasil ditambhkan")

#Buat program berjalan terus menerus (menggunakan while loop)
def main():
    data_nilai = muat_data()
    
    while True:
        print("\nSISTEM REKAP NILAI")
        print("1. tampilkan data nilai")
        print("2. tambah nilai baru")
        print("3. keluar")
        pilihan = input("pilih menu (1-3): ")
        if pilihan == '1':
            tampilkan_data(data_nilai)
        elif pilihan == '2':
            tambah_data(data_nilai)
        elif pilihan == '3':
            print("anda keluar")
            break
        else:
            print("input tidak valid.")
if __name__ == "__main__":
    main()