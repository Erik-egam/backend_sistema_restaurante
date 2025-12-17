from mysql.connector import pooling

class DBconfig:
    POOL_NAME='my_pool_name'
    POOL_SIZE=10
    HOST='localhost'
    USER='root'
    PORT='3306'
    DATABASE='restaurante'
    PASSWORD=''
    

pool = pooling.MySQLConnectionPool(
    pool_name=DBconfig.POOL_NAME,
    pool_size=DBconfig.POOL_SIZE,
    host=DBconfig.HOST,
    user=DBconfig.USER,
    port=DBconfig.PORT,
    password=DBconfig.PASSWORD,
    database=DBconfig.DATABASE
)

def get_conexion():
    return pool.get_connection()