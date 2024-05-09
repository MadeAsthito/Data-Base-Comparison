import mysql.connector as mysql
import time

from typing import Final
from pymemcache.client import base

# CONST
DB_HOST: Final = "localhost"
DB_USER: Final = "root"
DB_PASSWORD: Final = ""
DB_NAME: Final = "db_toko"

# CONNECT DATABASE
conn = mysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

# =============
# INIT PROGRAM
# =============
 
operasi_query_insert: int = 0
operasi_query_select: int = 0
operasi_query_delete: int = 0

total_time_insert: float = 0.0
total_time_select: float = 0.0
total_time_delete: float = 0.0

# LIST DATA PELANGGAN
listNamaPelanggan = [
    "Dina Cahaya", "Linda Sari", "Rina Setiawati", "Ani Cahyani", "Joko Widodo",
    "Rudi Hartono", "Siti Nurlela", "Agus Riyadi", "Budi Santoso", "Indra Wijaya"
]
listAlamatPelanggan = [
    "Jl. Surya Kencana 4", "Jl. Gembira Jaya 25", "Jl. Bahagia Sejahtera 17",
    "Jl. Kenangan Indah 3", "Jl. Harmoni 12", "Jl. Mawar 21",
    "Jl. Damai Abadi 9", "Jl. Pahlawan Baru 5A", "Jl. Merdeka No. 10", "Jl. Bunga Cempaka 8"
]
listEmailPelanggan = [
    "dina_cahaya@gmail.com", "linda_sari@yahoo.com", "rina_setiawati@hotmail.com",
    "ani_cahyani@yahoo.com", "joko_widodo@hotmail.com", "rudi_hartono@yahoo.com",
    "siti_nurlela@outlook.com", "agus_riyadi@gmail.com", "budi_santoso@hotmail.com",
    "indra_wijaya@yahoo.com"
]

# LIST DATA BARANG
listNamaBarang = [
    "Sarden Kaleng", "Beras", "Teh Celup", "Kopi Bubuk", "Margarin",
    "Minyak Goreng", "Telur Ayam", "Sampo", "Permen", "Kecap Manis"
]
listDeskripsiBarang = [
    "Sarden kaleng praktis dan lezat", "Produk beras berkualitas tinggi", 
    "Teh celup berkualitas tinggi", "Kopi bubuk aroma khas Indonesia", 
    "Margarin untuk roti dan masakan", "Minyak goreng tanpa kolesterol", 
    "Telur ayam segar", "Sampo untuk rambut halus dan berkilau", 
    "Permen manis untuk menyegarkan", "Kecap manis dengan cita rasa autentik"
]
listHargaJualBarang = [
    11000, 29000, 12000, 18000, 15000,
    22000, 19000, 25000, 7000, 14000
]
listHargaBeliBarang = [
    8000, 25000, 10000, 15000, 12000,
    18000, 16000, 21000, 5000, 12000
]

cur = conn.cursor(dictionary=True)

# =============
# KODE PROGRAM
# =============

def test_relational():
    # DATA BARANG + PELANGGAN
    for i in range(10):
        # INSERT DATA BARANG
        nama_barang:str = listNamaBarang[i]
        stok_barang:int = 50
        deskripsi:str = listDeskripsiBarang[i]
        harga_beli = listHargaBeliBarang[i]
        harga_jual = listHargaJualBarang[i]

        start_time = time()
        cur.execute("INSERT INTO barang(nama_barang, stok_barang, deskripsi, harga_beli, harga_jual) VALUES(%s, %s, %s, %s, %s)", (nama_barang, stok_barang, deskripsi, harga_beli, harga_jual))
        end_time = time()
        
        operasi_query_insert += 1
        total_time_insert += (end_time - start_time)

        # INSERT DATA PELANGGAN
        nama_pelanggan:str = listNamaPelanggan[i]
        alamat_pelanggan:str = listAlamatPelanggan[i]
        email_pelanggan = listEmailPelanggan[i]

        start_time = time()
        cur.execute("INSERT INTO pelanggan(nama, alamat, email) VALUES(%s, %s, %s)", (nama_pelanggan, alamat_pelanggan, email_pelanggan))
        end_time = time()
        
        operasi_query_insert += 1
        total_time_insert += (end_time - start_time)

    # DATA TRANS + DETAIL TRANS


    # DATA BARANG + PELANGGAN
    for i in range(10):
        id_ref:int = i+1

        # DELETE BARANG
        start_time = time()
        cur.execute(f"DELETE FROM barang WHERE id_barang = {id_ref}")
        end_time = time()

        operasi_query_delete += 1
        total_time_delete += (end_time - start_time)

        # DELETE PELANGGAN
        start_time = time()
        cur.execute(f"DELETE FROM pelanggan WHERE id_pelanggan = {id_ref}")
        end_time = time()

        operasi_query_delete += 1
        total_time_delete += (end_time - start_time)

    # PRINT HASIL TESTING
    insert_avg_execution_time = total_time_insert / operasi_query_insert
    print(f"Average execution time for WRITE OPERATION on Relational Database : \n{insert_avg_execution_time:.6f} seconds")
    print(f"Total request for WRITE OPERATION on Relational Database : {operasi_query_insert} request")
    print()

    select_avg_execution_time = total_time_select / operasi_query_select
    print(f"Average execution time for READ OPERATION on Relational Database : \n{select_avg_execution_time:.6f} seconds")
    print(f"Total request for READ OPERATION on Relational Database : {operasi_query_select} request")
    print()

    delete_avg_execution_time = total_time_delete / operasi_query_delete
    print(f"Average execution time for DELETE OPERATION on Relational Database : \n{delete_avg_execution_time:.6f} seconds")
    print(f"Total request for DELETE OPERATION on Relational Database : {operasi_query_delete} request")
    print()
