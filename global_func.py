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

client = base.Client(('localhost', 11211))

# Perhitungan waktu untuk query yang diinput beserta jumlah total iterasinya
def measure_query_execution(query:str, iterations:int, cache=False):
    conn.commit()
    cache_result = None
    
    total_execution_time: float = 0.0

    cur = conn.cursor(dictionary=True)

    for i in range(iterations):
        if cache:
            start_time = time.time()
            
            cache_result = client.get(f"measure_query_{i}")
            
            if cache_result is None:
                result = cur.execute(query)
                client.set(f"measure_query_{i}", result)
        else: 
            start_time = time.time()
            
            result = cur.execute(query)

        end_time = time.time()

        execution_time = end_time - start_time
        total_execution_time += execution_time
    
    avg_execution_time: float = total_execution_time / iterations
    print(f"Average execution time for the query \n'{query}': \n{avg_execution_time:.6f} seconds")

    cur.close()
    return avg_execution_time

# Perhitungan waktu untuk proses pengambilan seluruh data transaksi beserta detailnya
def measure_select_generated_data(table:str ='penjualan'):
    conn.commit()

    total_execution_time: float = 0.0

    cur = conn.cursor(dictionary=True)

    cur.execute(f"SELECT COUNT(*) as TOTAL FROM {table}")
    results = cur.fetchone()
    iterations: int = results['TOTAL'] if results else 0
    
    for i in range(iterations):
        start_time = time.time()

        qur_select: str = f"SELECT * FROM {table} INNER JOIN detail_{table} ON {table}.id_{table} = detail_{table}.id_{table} WHERE {table}.id_{table} = {i+1}"
        cur.execute(qur_select)

        end_time = time.time()

        execution_time = end_time - start_time
        total_execution_time += execution_time
        
        cur.fetchall() 

    avg_execution_time: float = total_execution_time / iterations
    print(f"Average execution time for querying all of the data on {table} + detail {table}: \n{avg_execution_time:.6f} seconds")

    cur.close()
    return avg_execution_time

# Perhitungan waktu untuk proses inserting data karyawan sesuai dengan iterasi
def measure_insert_generated_data(iterations: int):
    total_execution_time: float = 0.0

    cur = conn.cursor(dictionary=True)
    
    for i in range(iterations):
        start_time = time.time()

        cur.execute(f"INSERT INTO karyawan(nama, alamat, tgl_masuk, created_at, updated_at) VALUES ('testing{i+1}', 'jl testing, no {i+1})', '2023-12-30', '2024-05-01 00:00:00', '2024-05-01 00:00:00')")
        conn.commit()

        end_time = time.time()

        execution_time = end_time - start_time
        total_execution_time += execution_time
    
    avg_execution_time: float = total_execution_time / iterations
    print(f"Average execution time for INSERT {iterations} data on karyawan table : \n{avg_execution_time:.6f} seconds")

    cur.close()
    return avg_execution_time

def get_db_size():
    cur = conn.cursor(dictionary=True)

    query: str = """
        SELECT table_schema AS `DATABASE`, SUM(data_length + index_length) / (1024 * 1024) AS `SIZE`
        FROM information_schema.tables 
        WHERE table_schema = 'db_toko'
        GROUP BY table_schema;
    """

    cur.execute(query)
    result = cur.fetchone()['SIZE']

    print(f"Database Size = {result:.5f} Mb")

    cur.close()
    return result

conn.close()