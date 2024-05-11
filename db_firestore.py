import time
import firebase_admin
import json
from firebase_admin import credentials, firestore
from typing import Final

cred = credentials.Certificate("./key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

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

    size_db:float = 0

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

    # INIT COLLECTION
    doc_transaksi = db.collection("transaksi")
    doc_pelanggan = db.collection("pelanggan")
    doc_barang = db.collection("barang")

    # RESET AUTO INCREMENT + DELETE ALL DATA ON DATABASE

    # DATA BARANG + PELANGGAN
    print("INSERTING DATA BARANG + PELANGGAN")
    for i in range(10):
        # INSERT DATA BARANG
        nama_barang:str = listNamaBarang[i]
        stok_barang:int = 50
        deskripsi:str = listDeskripsiBarang[i]
        harga_beli = listHargaBeliBarang[i]
        harga_jual = listHargaJualBarang[i]

        start_time = time.time()
        doc_barang.add({
            "nama_barang" : nama_barang,
            "stok_barang" : stok_barang,
            "deskripsi" : deskripsi,
            "harga_beli" : harga_beli,
            "harga_jual" : harga_jual
        })
        end_time = time.time()
        
        operasi_query_insert += 1
        total_time_insert += (end_time - start_time)

        # INSERT DATA PELANGGAN
        nama_pelanggan:str = listNamaPelanggan[i]
        alamat_pelanggan:str = listAlamatPelanggan[i]
        email_pelanggan = listEmailPelanggan[i]

        start_time = time.time()
        doc_pelanggan.add({
            "nama" : nama_pelanggan,
            "alamat" : alamat_pelanggan,
            "email" : email_pelanggan
        })
        end_time = time.time()
        
        operasi_query_insert += 1
        total_time_insert += (end_time - start_time)

    # DATA TRANS + DETAIL TRANS
    idBarang = 1
    idMember = 1
    print("INSERTING DATA TRANSAKSI")
    for i in range(n):
        subtotal = 0
        idTrans = i + 1

        data_barang = []
        for j in range(5):
            id_barang = idBarang
            nama_barang = listNamaBarang[id_barang-1]
            harga_jual = listHargaJualBarang[id_barang-1]
            qty = 5
            total_harga = harga_jual * qty

            # APPEND DATA BARANG
            data_barang.append({
                "nama_barang" : nama_barang,
                "harga_jual" : harga_jual,
                "qty" : qty,
                "total_harga" : total_harga
            })

            subtotal += total_harga
            idBarang += 1

            # Pengulangan ID BARANG
            if idBarang > 10:
                idBarang = 1
        
        id_member = idMember

        # Pengulangan ID MEMBER
        idMember += 1
        if idMember == 10:
            idMember = 1

        status = listEnum[1]

        # INSERT DATA TRANSAKSI
        start_time = time.time()
        doc_transaksi.add({
            "data_pelanggan": {
                "nama" : listNamaPelanggan[id_member-1],
                "alamat" : listAlamatPelanggan[id_member-1],
                "email" : listEmailPelanggan[id_member-1]
            },
            "data_barang" : data_barang,
            "total_harga" : subtotal,
            "status" : status
        })
        end_time = time.time()

        operasi_query_insert += 1
        total_time_insert += (end_time - start_time)
    
    
    print("PROSES SELECT + DELETE")
    start_time = time.time()
    doc_data_transaksi = doc_transaksi.stream()
    end_time = time.time()
    total_time_select += (end_time - start_time)

    data_transaksi = {}
    for doc in doc_data_transaksi:
        # SELECT DATA TRANSAKSI
        data_transaksi[doc.id] = doc.to_dict() 
    
        operasi_query_select += 1

        # CHECK COLLECTION SIZE
        json_strings = json.dumps(doc.to_dict())
        size_bytes = len(json_strings.encode('utf-8'))
        size_db += size_bytes
           
        # DELETE DATA TRANSAKSI
        start_time = time.time()
        doc_transaksi.document(doc.id).delete()
        end_time = time.time()

        operasi_query_delete += 1
        total_time_delete += (end_time - start_time)

    # GET DB SIZE
    doc_data_barang = doc_barang.stream()
    for doc in doc_data_barang:
        # CHECK COLLECTION SIZE
        json_strings = json.dumps(doc.to_dict())
        size_bytes = len(json_strings.encode('utf-8'))
        size_db += size_bytes
           
        # DELETE DATA BARANG
        start_time = time.time()
        doc_barang.document(doc.id).delete()
        end_time = time.time()

        operasi_query_delete += 1
        total_time_delete += (end_time - start_time)

    doc_data_pelanggan = doc_pelanggan.stream()
    for doc in doc_data_pelanggan:
        # CHECK COLLECTION SIZE
        json_strings = json.dumps(doc.to_dict())
        size_bytes = len(json_strings.encode('utf-8'))
        size_db += size_bytes
           
        # DELETE DATA PELANGGAN
        start_time = time.time()
        doc_pelanggan.document(doc.id).delete()
        end_time = time.time()

        operasi_query_delete += 1
        total_time_delete += (end_time - start_time)

    # PRINT HASIL TESTING
    print()
    print("RESULT TESTING : FIRESTORE ")
    insert_avg_execution_time = total_time_insert / operasi_query_insert
    print(f"WRITE OPERATION average time : {insert_avg_execution_time:.6f} seconds")
    print(f"WRITE OPERATION total time : {total_time_insert:.6f} seconds")
    print(f"WRITE OPERATION total request : {operasi_query_insert} request")
    print()

    select_avg_execution_time = total_time_select / operasi_query_select
    print(f"READ OPERATION average time : {select_avg_execution_time:.6f} seconds")
    print(f"READ OPERATION total time : {total_time_select:.6f} seconds")
    print(f"READ OPERATION total request : {operasi_query_select} request")
    print()

    delete_avg_execution_time = total_time_delete / operasi_query_delete
    print(f"DELETE OPERATION average time : {delete_avg_execution_time:.6f} seconds")
    print(f"DELETE OPERATION total time : {total_time_delete:.6f} seconds")
    print(f"DELETE OPERATION total request : {operasi_query_delete} request")
    print()

    # CALCULATE MB
    size_db = size_db / (1024 * 1024) 
    print(f"Total Size for Relational + Caching Database : {size_db} mb")
    print()
