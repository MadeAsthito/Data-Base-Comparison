import mysql.connector as mysql 
import time
import random
import json
from datetime import datetime

from typing import Final
from pymemcache.client import base

# CONST
DB_HOST: Final = "localhost"
DB_USER: Final = "root"
DB_PASSWORD: Final = ""
DB_NAME: Final = "db_toko_json"

# CONNECT DATABASE
conn = mysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

# =============
# KODE PROGRAM
# =============

def test(n:int):

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
    listEnum = ["pending", "success"]

    cur = conn.cursor(dictionary=True)

    # RESET AUTO INCREMENT
    cur.execute("ALTER TABLE pelanggan AUTO_INCREMENT = 1")
    conn.commit()
    cur.execute("ALTER TABLE barang AUTO_INCREMENT = 1")
    conn.commit()
    cur.execute("ALTER TABLE transaksi AUTO_INCREMENT = 1")
    conn.commit()
    cur.execute("ALTER TABLE detail_transaksi AUTO_INCREMENT = 1")
    conn.commit()

    # DATA BARANG + PELANGGAN
    for i in range(10):
        # INSERT DATA BARANG
        nama_barang:str = listNamaBarang[i]
        stok_barang:int = 50
        deskripsi:str = listDeskripsiBarang[i]
        harga_beli = listHargaBeliBarang[i]
        harga_jual = listHargaJualBarang[i]

        start_time = time.time()
        cur.execute("INSERT INTO barang(nama_barang, stok_barang, deskripsi, harga_beli, harga_jual) VALUES(%s, %s, %s, %s, %s)", (nama_barang, stok_barang, deskripsi, harga_beli, harga_jual))
        conn.commit()
        end_time = time.time()
        
        operasi_query_insert += 1
        total_time_insert += (end_time - start_time)

        # INSERT DATA PELANGGAN
        nama_pelanggan:str = listNamaPelanggan[i]
        alamat_pelanggan:str = listAlamatPelanggan[i]
        email_pelanggan = listEmailPelanggan[i]

        start_time = time.time()
        cur.execute("INSERT INTO pelanggan(nama, alamat, email) VALUES(%s, %s, %s)", (nama_pelanggan, alamat_pelanggan, email_pelanggan))
        conn.commit()
        end_time = time.time()
        
        operasi_query_insert += 1
        total_time_insert += (end_time - start_time)

    # DATA TRANS + DETAIL TRANS
    idBarang = 1
    idMember = 1
    for i in range(n):
        print(f"insert {i+1}")
        subtotal = 0
        idTrans = i + 1

        data_barang = []
        for j in range(5):
            # INSERT DATA DETAIL TRANSAKSI
            id_barang = idBarang
            harga_jual = listHargaJualBarang[id_barang-1]
            qty = 5
            total_harga = harga_jual * qty

            start_time = time.time()
            cur.execute("INSERT INTO detail_transaksi (id_transaksi, id_barang, jumlah, harga_per_item, total_harga) VALUES (%s, %s, %s, %s, %s)",(idTrans, id_barang, qty, harga_jual, total_harga))
            conn.commit()
            end_time = time.time()

            operasi_query_insert += 1
            total_time_insert += (end_time - start_time)

            subtotal += total_harga
            idBarang += 1

            # TODO
            start_time = time.time()
            cur.execute(f"SELECT nama_barang, stok_barang, deskripsi, harga_beli, harga_jual FROM barang WHERE id_barang = {id_barang} ")
            res_barang = cur.fetchone()
            # res_barang = select barang by id_barang
            end_time = time.time()
            total_time_select += (end_time - start_time)
            operasi_query_select += 1
            
            res_barang['jumlah'] = qty
            res_barang['harga_per_item'] = harga_jual
            res_barang['total_harga'] = total_harga
            data_barang.append(res_barang)
            # json transform(res_barang)
            # array.append(json)
        
        json_barang = json.dumps(data_barang)

        # Pengulangan ID BARANG
        if idBarang > 10:
            idBarang = 1

        id_member = idMember

        # Pengulangan ID MEMBER
        idMember += 1
        if idMember == 10:
            idMember = 1

        status = listEnum[1]

        # TODO
        data_pelanggan = []
        start_time = time.time()
        cur.execute(f"SELECT * FROM pelanggan WHERE id_pelanggan = {id_member}")
        res_pelanggan = cur.fetchone()
        # res_pelanggan = select pelanggan by id_pelanggan
        end_time = time.time()
        total_time_select += (end_time - start_time)
        operasi_query_select += 1

        res_pelanggan['created_at'] = res_pelanggan['created_at'].isoformat()
        data_pelanggan.append(res_pelanggan)
        # json transform(res_pelanggan)
        json_pelanggan = json.dumps(data_pelanggan)

        start_time = time.time()
        # Insert data transaksi into tb_trans
        cur.execute("INSERT INTO transaksi (id_pelanggan, status, subtotal, data_barang, data_pelanggan) VALUES (%s, %s, %s, %s, %s)", (id_member, status, subtotal, json_barang, json_pelanggan))
        conn.commit()
        end_time = time.time()

        operasi_query_insert += 1
        total_time_insert += (end_time - start_time)

        start_time = time.time()
        # Select data transaksi from tb_trans
        cur.execute(f"SELECT * from transaksi WHERE id_transaksi = {idTrans}")
        cur.fetchone()
        # result_trans = select * from tb_trans WHERE id_trans = idTrans
        end_time = time.time()
        # GET DATA TRANS
    
        operasi_query_select += 1
        total_time_select += (end_time - start_time)
        # id_pelanggan = data_trans['id_pelanggan']

        # start_time = time.time()
        # # Select data pelanggan from tb_pelanggan
        # cur.execute(f"SELECT * from pelanggan WHERE id_pelanggan = {id_pelanggan}")
        # # result_pelanggan = select * from tb_pelanggan WHERE id_pelanggan = result_trans->id_pelanggan
        # end_time = time.time()
        # cur.fetchone()

        # operasi_query_select += 1
        # total_time_select += (end_time - start_time)

        # for j in range(5):
        #     idDetail = ((i+1) * 5) - 5 + (j+1)

        #     start_time = time.time()
        #     # Select data detail transaksi from tb_trans_detail
        #     cur.execute(f"SELECT * FROM detail_transaksi WHERE id_detail_transaksi = {idDetail}")
        #     # result_detail = select * from tb_trans_detail WHERE id_detail = idDetail
        #     end_time = time.time()
        #     data_detail = cur.fetchone()

        #     operasi_query_select += 1
        #     total_time_select += (end_time - start_time)
            
        #     id_barang = data_detail['id_barang']

        #     start_time = time.time()
        #     # Select data barang from tb_barang
        #     cur.execute(f"SELECT * FROM barang WHERE id_barang = {id_barang}")
        #     # result_barang = select * from tb_barang WHERE id_barang = result_detail->id_barang
        #     end_time = time.time()
        #     cur.fetchone()

        #     operasi_query_select += 1
        #     total_time_select += (end_time - start_time)

        # GET DB SIZE
        cur.execute(f"SELECT table_schema AS `DATABASE`, SUM(data_length + index_length) / (1024 * 1024) AS `SIZE` FROM information_schema.tables WHERE table_schema = '{DB_NAME}' GROUP BY table_schema;")
        size_db = cur.fetchone()['SIZE']

    # DELETE DATA TRANS = DETAIL
    for i in range(n):
        print(f"delete {i+1}")
        idTrans = i + 1
        start_time = time.time()
        # Delete data detail transaksi from tb_trans_detail
        cur.execute(f"DELETE FROM detail_transaksi WHERE id_transaksi = {idTrans}")
        conn.commit()
        # delete data from tb_trans_detail WHERE id_trans = idTrans
        end_time = time.time()

        operasi_query_delete += 1
        total_time_delete += (end_time - start_time)

        start_time = time.time()
        # Delete data transaksi from tb_trans
        cur.execute(f"DELETE FROM transaksi WHERE id_transaksi = {idTrans}")
        conn.commit()
        # delete data from tb_trans WHERE id_trans = idTrans
        end_time = time.time()

        operasi_query_delete += 1
        total_time_delete += (end_time - start_time)

    # DATA BARANG + PELANGGAN
    for i in range(10):
        id_ref:int = i+1

        # DELETE BARANG
        start_time = time.time()
        cur.execute(f"DELETE FROM barang WHERE id_barang = {id_ref}")
        conn.commit()
        end_time = time.time()

        operasi_query_delete += 1
        total_time_delete += (end_time - start_time)

        # DELETE PELANGGAN
        start_time = time.time()
        cur.execute(f"DELETE FROM pelanggan WHERE id_pelanggan = {id_ref}")
        conn.commit()
        end_time = time.time()

        operasi_query_delete += 1
        total_time_delete += (end_time - start_time)

    # PRINT HASIL TESTING
    insert_avg_execution_time = total_time_insert / operasi_query_insert
    print(f"Average execution time for WRITE OPERATION on Relational JSON Database : \n{insert_avg_execution_time:.6f} seconds")
    print(f"Total request for WRITE OPERATION on Relational Database : {operasi_query_insert} request")
    print()

    select_avg_execution_time = total_time_select / operasi_query_select
    print(f"Average execution time for READ OPERATION on Relational JSON Database : \n{select_avg_execution_time:.6f} seconds")
    print(f"Total request for READ OPERATION on Relational Database : {operasi_query_select} request")
    print()

    delete_avg_execution_time = total_time_delete / operasi_query_delete
    print(f"Average execution time for DELETE OPERATION on Relational JSON Database : \n{delete_avg_execution_time:.6f} seconds")
    print(f"Total request for DELETE OPERATION on Relational Database : {operasi_query_delete} request")
    print()

    print(f"Total Size for Relational JSON Database : {size_db} mb")
    print()
