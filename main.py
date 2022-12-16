import pymysql
from config import host, user, password, db_name

# подключаемся к базе
try:
    connection = pymysql.connect(
        host=host,
        port=3306,   # default
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Successful connection")
    print("#" * 20)

    try:
        with connection.cursor() as cursor:  # контекстный менеджер with
            create_table_query = "CREATE TABLE 'users'(id int AUTO_INCREMENT," \
                                 " name varchar(48)," \
                                 " password varchar(48)," \
                                 " email varchar(48), PRIMARY KEY (id));"  # прямой запрос
            cursor.execute(create_table_query)
            print("Table created successfully")

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)
