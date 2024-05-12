```
for i in range(10):
    # INSERT DATA BARANG
	SET nama_barang = listNamaBarang[i]
    SET stok_barang = 50
    SET deskripsi = listDeskripsi[i]
    SET harga_beli = listHargaBeli[i]
    SET harga_jual = listHargaJual[i]

    SET start_time = time()
    INSERT data_barang INTO tb_barang
    SET end_time = time()

    SET operasi_query_insert += 1
    SET total_time_insert += (end_time - start_time)

    # INSERT DATA PELANGGAN
    SET nama = listName[i]
    SET alamat = listAlamat[i]
    SET email = listEmail[i]

    SET start_time = time()
    INSERT data_pelanggan INTO tb_pelanggan
    SET end_time = time()

    SET operasi_query_insert += 1
    SET total_time_insert += (end_time - start_time)
```	
```	
for i in range(1000):
    SET subtotal = 0
    SET idTrans = i + 1

    for j in range(5):
        SET id_barang = idBarang
        SET harga_jual = listHargaJualBarang[id_barang-1]
        SET qty = 5
        SET total_harga = harga_jual * qty

        # INSERT DATA DETAIL TRANSAKSI
        SET start_time = time.time()
        INSERT detail_transaksi INTO tb_detail_transaksi
        SET end_time = time.time()

        SET operasi_query_insert += 1
        SET total_time_insert += (end_time - start_time)

        SET subtotal += total_harga
        SET idBarang += 1

        # Pengulangan ID BARANG
        if idBarang > 10:
            SET idBarang = 1
    
    SET id_member = idMember

    # Pengulangan ID MEMBER
    SET idMember += 1
    if idMember == 10:
        SET idMember = 1

    SET status = listEnum[1]

    # INSERT DATA TRANSAKSI
    SET start_time = time.time()
    INSERT data_transaksi INTO tb_transaksi
    SET end_time = time.time()

    SET operasi_query_insert += 1
    SET total_time_insert += (end_time - start_time)

    # SELECT DATA TRANSAKSI
    SET start_time = time.time()
    SET data_trans = SELECT data_transaksi FROM tb_transaksi WHERE id_transaksi = idTrans
    SET end_time = time.time()

    SET operasi_query_select += 1
    SET total_time_select += (end_time - start_time)
    

    # SELECT DATA PELANGGAN
    SET idPelanggan = data_trans['id_pelanggan']
    SET start_time = time.time()
    SET data_pelanggan = SELECT data_pelanggan FROM tb_pelanggan WHERE id_pelanggan = idPelanggan
    SET end_time = time.time()

    SET operasi_query_select += 1
    SET total_time_select += (end_time - start_time)

    for j in range(5):
        SET idDetail = ((i+1) * 5) - 5 + (j+1)

        # SELECT DATA DETAIL TRANSAKSI
        SET start_time = time.time()
        SET data_detail = SELECT data_detail FROM tb_detail_transaksi WHERE id_detail_transaksi = idDetail
        SET end_time = time.time()

        SET operasi_query_select += 1
        SET total_time_select += (end_time - start_time)
        
        # SELECT DATA BARANG
        SET idBarang = data_detail['id_barang']
        SET start_time = time.time()
        SET data_barang = SELECT data_barang FROM tb_barang WHERE id_barang = idBarang
        SET end_time = time.time()

        SET operasi_query_select += 1
        SET total_time_select += (end_time - start_time)

        # GET DB SIZE
        
        SET size_db = SELECT data_size_database FROM information_schema WHERE table_schema = DB_NAME
```	

```	
for i in range(1000):
    SET idTrans = i + 1

    # DELETE DATA TRANSAKSI
    SET start_time = time.time()
    DELETE data_detail_transaksi FROM tb_detail_transaksi WHERE id_transaksi = idTrans
    SET end_time = time.time()

    SET operasi_query_delete += 1
    SET total_time_delete += (end_time - start_time)

    # DELETE DATA DETAIL TRANSAKSI
    SET start_time = time.time()
    DELETE data_transaksi FROM tb_transaksi WHERE id_transaksi = idTrans
    SET end_time = time.time()

    SET operasi_query_delete += 1
    SET total_time_delete += (end_time - start_time)
```	

```	
for i in range(10):
    SET idRef = i+1

    # DELETE BARANG
    SET start_time = time.time()
    DELETE data_barang FROM tb_barang WHERE id_barang = idRef
    conn.commit()
    SET end_time = time.time()

    SET operasi_query_delete += 1
    SET total_time_delete += (end_time - start_time)

    # DELETE PELANGGAN
    SET start_time = time.time()
    DELETE data_pelanggan FROM tb_pelanggan WHERE id_pelanggan = idRef
    conn.commit()
    SET end_time = time.time()

    SET operasi_query_delete += 1
    SET total_time_delete += (end_time - start_time)
```	

```
SET insert_avg_execution_time = total_time_insert / operasi_query_insert
PRINT insert_avg_execution_time
PRINT total_time_insert
PRINT operasi_query_insert

SET select_avg_execution_time = total_time_select / operasi_query_select
PRINT select_avg_execution_time
PRINT total_time_select
PRINT operasi_query_select

SET delete_avg_execution_time = total_time_delete / operasi_query_delete
PRINT delete_avg_execution_time
PRINT total_time_delete
PRINT operasi_query_delete

PRINT size_db
```	