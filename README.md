PSEUDO CODE : 
'''
operasi_query_insert = 0
operasi_query_select = 0
operasi_query_delete = 0

total_time_insert = 0.0
total_time_select = 0.0
total_time_delete = 0.0


for i in range(10):
	// insert barang 
	nama_barang = listBarang[i]
	stok_barang = 50
	deskripsi = listDeskripsi[i]
	harga_beli = listHargaBeli[i]
	harga_jual = listHargaJual[i]
	
	start_time = time()
	insert data 
	end_time = time()
	
	operasi_query_insert += 1
	total_time_insert += (end_time - start_time)
	
	// insert pelanggan
	nama = listName[i]
	alamat = listAlamat[i]
	email = listEmail[i]
	
	start_time = time()
	insert data 
	end_time = time()
	
	operasi_query_insert += 1
	total_time_insert += (end_time - start_time)

// TRANS
for i in range(1000)
	// insert data  detail
	subtotal = 0
	idTrans = i+1
	for j in range(5):
		id_trans = idTrans
		id_barang = random(1,10)
		harga_jual = listHargaJual[id_barang]
		qty = random(1,10)
		total_harga = harga_jual * qty
		
		start_time = time()
		insert data 
		end_time = time()
	
		operasi_query_insert += 1
		total_time_insert += (end_time - start_time)
		
		subtotal += total_harga
	
	// insert data trans
	id_member = random(1,10)
	status = listEnum[random(0,1)]
	subtotal = subtotal
		
	start_time = time()
	insert data 
	end_time = time()
	
	operasi_query_insert += 1
	total_time_insert += (end_time - start_time)
	
	// read data trans 
	
		
	start_time = time()
	result_trans = select * from tb_trans WHERE id_trans = idTrans
	end_time = time()
	
	operasi_query_select += 1
	total_time_select += (end_time - start_time)
			
	start_time = time()
	result_pelanggan = select * from tb_pelanggan WHERE id_pelanggan = result_trans->id_pelanggan 
	end_time = time()
	
	operasi_query_select += 1
	total_time_select += (end_time - start_time)
	
	for j in range(5):
		// trans 1 = detail 1,2,3,4,5
		// trans 2 = detail 6,7,8,9,10
		// trans 3 = detail 11,12,13,14,15
		
		// i = 1 ; j = 1 id_detail = 1
		// i = 2 ; j = 1 id_detail = 6
		// i = 3 ; j = 3 id_detail = 13
		
		
		// read data detail
		idDetail = (i*5) - 5 + j
		
		start_time = time()
		result_detail = select * from tb_trans WHERE id_detail = idDetail
		end_time = time()
	
		operasi_query_select += 1
		total_time_select += (end_time - start_time)
		
		start_time = time()
		result_barang = select * from tb_barang WHERE id_barang = result_detail->id_barang 
		end_time = time()
	
		operasi_query_select += 1
		total_time_select += (end_time - start_time)
		
		

	// delete data detail
		
	start_time = time()
	delete data detail WHERE id_trans = idTrans
	end_time = time()
	
	operasi_query_delete += 1
	total_time_delete += (end_time - start_time)	
	
	// delete data trans
	
	start_time = time()
	delete data trans WHERE id_trans = idTrans
	end_time = time()
	
	operasi_query_delete += 1
	total_time_delete += (end_time - start_time)
	
for i in range(10):
	id = i+1
	
	// delete barang
	start_time = time()
	delete data barang WHERE id_barang = id
	end_time = time()
	
	operasi_query_delete += 1
	total_time_delete += (end_time - start_time)
	
	// delete pelanggan
	start_time = time()
	delete data pelanggan WHERE id_pelanggan = id
	end_time = time()
	
	operasi_query_delete += 1
	total_time_delete += (end_time - start_time)
'''