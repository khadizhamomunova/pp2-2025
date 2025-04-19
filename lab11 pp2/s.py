import psycopg2 as pgsql

def paginate_query(table_name, limit, offset):
    try:
        connection = pgsql.connect(
            database="lab10",
            user='postgres',
            password='Mk22335577',
            host='localhost',
        )
        con = connection.cursor()

        query = f"SELECT * FROM {table_name} LIMIT %s OFFSET %s;"
        con.execute(query, (limit, offset))
        
        rows = con.fetchall()

        for row in rows:
            print(row)

    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            con.close()
            connection.close()

paginate_query('phone_number', limit=5, offset=0)