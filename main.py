from src import db_relational
from src import db_json
from src import db_caching
from src import db_json_caching
from src import db_firestore

# MAIN
if __name__ == '__main__':
    # DATABASE RELATIONAL
    n_transaksi = 1000

    print(f"RELATIONAL : {n_transaksi} transaksi")
    db_relational.test(n_transaksi)

    print(f"JSON : {n_transaksi} transaksi")
    db_json.test(n_transaksi)

    print(f"Caching : {n_transaksi} transaksi")
    db_caching.test(n_transaksi)

    print(f"JSON + Caching : {n_transaksi} transaksi")
    db_json_caching.test(n_transaksi)

    # print(f"FIRESTORE : {n_transaksi} transaksi")
    # db_firestore.test(n_transaksi)