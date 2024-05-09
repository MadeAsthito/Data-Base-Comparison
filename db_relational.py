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