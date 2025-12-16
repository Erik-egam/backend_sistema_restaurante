from mysql.connector import connect

class DBconfig:
    HOST='localhost'
    USER='root'
    PORT='3306'
    DATABASE='restaurante'
    PASSWORD=''
    
cnx = connect(
    host=DBconfig.HOST,
    user=DBconfig.USER,
    port=DBconfig.PORT,
    password=DBconfig.PASSWORD,
    database=DBconfig.DATABASE
)