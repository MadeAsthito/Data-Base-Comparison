import global_func as gf

# MAIN
if __name__ == '__main__':

    # Input untuk measure_query_execution
    query: str = "SELECT penjualan.* FROM penjualan INNER JOIN detail_penjualan ON penjualan.id_penjualan = detail_penjualan.id_penjualan WHERE penjualan.id_penjualan = 1"
    iterations: int = 1000

    gf.get_db_size()
    print()

    gf.measure_query_execution(query, iterations)
    print()

    gf.measure_select_generated_data()
    print()

    gf.measure_insert_generated_data(iterations)