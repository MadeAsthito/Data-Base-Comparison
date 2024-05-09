# Pseudocode

## Initialization

```python
operasi_query_insert = 0
operasi_query_select = 0
operasi_query_delete = 0

total_time_insert = 0.0
total_time_select = 0.0
total_time_delete = 0.0

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
```

## Data Barang + Pelanggan

```python
for i in range(10):
    # Insert barang
    nama_barang = listBarang[i]
    stok_barang = 50
    deskripsi = listDeskripsi[i]
    harga_beli = listHargaBeli[i]
    harga_jual = listHargaJual[i]

    start_time = time()
    # Insert data barang into tb_barang
    end_time = time()

    operasi_query_insert += 1
    total_time_insert += (end_time - start_time)

    # Insert pelanggan
    nama = listName[i]
    alamat = listAlamat[i]
    email = listEmail[i]

    start_time = time()
    # Insert data pelanggan into tb_pelanggan
    end_time = time()

    operasi_query_insert += 1
    total_time_insert += (end_time - start_time)
```

## Data Trans + Detail Trans

```python
for i in range(1000):
    idTrans = i + 1
    subtotal = 0

    for j in range(5):
        id_barang = random(1, 10)
        harga_jual = listHargaJual[id_barang]
        qty = random(1, 10)
        total_harga = harga_jual * qty

        start_time = time()
        # Insert data detail transaksi into tb_trans_detail
        end_time = time()

        operasi_query_insert += 1
        total_time_insert += (end_time - start_time)

        subtotal += total_harga

    id_member = random(1, 10)
    status = listEnum[random(0, 1)]

    start_time = time()
    # Insert data transaksi into tb_trans
    end_time = time()

    operasi_query_insert += 1
    total_time_insert += (end_time - start_time)

    start_time = time()
    # Select data transaksi from tb_trans
    result_trans = select * from tb_trans WHERE id_trans = idTrans
    end_time = time()

    operasi_query_select += 1
    total_time_select += (end_time - start_time)

    start_time = time()
    # Select data pelanggan from tb_pelanggan
    result_pelanggan = select * from tb_pelanggan WHERE id_pelanggan = result_trans->id_pelanggan
    end_time = time()

    operasi_query_select += 1
    total_time_select += (end_time - start_time)

    for j in range(5):
        idDetail = (i * 5) - 5 + j

        start_time = time()
        # Select data detail transaksi from tb_trans_detail
        result_detail = select * from tb_trans_detail WHERE id_detail = idDetail
        end_time = time()

        operasi_query_select += 1
        total_time_select += (end_time - start_time)

        start_time = time()
        # Select data barang from tb_barang
        result_barang = select * from tb_barang WHERE id_barang = result_detail->id_barang
        end_time = time()

        operasi_query_select += 1
        total_time_select += (end_time - start_time)

    start_time = time()
    # Delete data detail transaksi from tb_trans_detail
    delete data from tb_trans_detail WHERE id_trans = idTrans
    end_time = time()

    operasi_query_delete += 1
    total_time_delete += (end_time - start_time)

    start_time = time()
    # Delete data transaksi from tb_trans
    delete data from tb_trans WHERE id_trans = idTrans
    end_time = time()

    operasi_query_delete += 1
    total_time_delete += (end_time - start_time)
```

## Data Barang + Pelanggan

```python
for i in range(10):
    id = i + 1

    # Delete barang
    start_time = time()
    delete data from tb_barang WHERE id_barang = id
    end_time = time()

    operasi_query_delete += 1
    total_time_delete += (end_time - start_time)

    # Delete pelanggan
    start_time = time()
    delete data from tb_pelanggan WHERE id_pelanggan = id
    end_time = time()

    operasi_query_delete += 1
    total_time_delete += (end_time - start_time)

```
