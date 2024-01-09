import pymysql

# DataBase configuration
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    charset='utf8mb4',
    database='users',
)

# All MySQL queries storage
sql_queries = {
    'create_table': '''
        CREATE TABLE users_data (
            id INT PRIMARY KEY, 
            login VARCHAR(32) NOT NULL, 
            password VARCHAR(64) NOT NULL, 
            age INT NOT NULL );
    ''',
    'delete_table': 'DROP TABLE users_data',
    'show_table_data': 'SELECT * FROM users_data;',
    'add_table_data': 'INSERT INTO users_data (id, login, password, age) VALUES (%s, %s, %s, %s);',
}

# Class for manipulating database


class DataBase:

    # Function is used for manipulating tables only
    def table_manipulation(query):
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                cursor.commit()
        finally:
            connection.close()

    # Function is used for manipulating table's data (its information)
    def table_data_manipulation(query, values):
        if query == sql_queries['show_table_data']:
            try:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    result = cursor.fetchall()
                    for element in result:
                        print(element)
            finally:
                connection.close()

        elif query == sql_queries['add_table_data']:
            try:
                with connection.cursor() as cursor:
                    cursor.execute(query, values)
                    connection.commit()
            finally:
                connection.close()


# Create table in database
DataBase.table_manipulation(sql_queries['create_table'])
# Add some information into created table
DataBase.table_data_manipulation(
    sql_queries['add_table_data'], (324, 'john', 'dlfk849', 20))
# Show the whole information involved in table
DataBase.table_data_manipulation(sql_queries['show_table_data'], None)
