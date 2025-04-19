import psycopg2

try:
    conn = psycopg2.connect(
        dbname="lab10",
        user="postgres",
        password="Mk22335577",
        host="localhost",
        port="5432"
    )
    print("✅ Успешное подключение к базе данных!")
    conn.close()
except Exception as e:
    print("❌ Ошибка подключения:", e)
