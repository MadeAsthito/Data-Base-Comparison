import db_relational
import db_json
import db_caching

# MAIN
if __name__ == '__main__':
    # DATABASE RELATIONAL
    n_transaksi = 1000

    print(f"RELATIONAL : {n_transaksi} transaksi")
    db_relational.test(n_transaksi)

    print(f"JSON : {n_transaksi} transaksi")
    db_json.test(n_transaksi)

    # db_caching.test(n_transaksi)