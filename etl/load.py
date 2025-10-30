import os
import sqlite3
import psycopg2
import pandas as pd

def load_data(df: pd.DataFrame = None):
    """
    Загрузка очищенных данных в PostgreSQL.
    Если DataFrame не передан, читаем из Parquet-файла.
    """
    # ------------------------------
    #Чтение учётных данных
    # ------------------------------
    creds_path = 'creds.db'
    if not os.path.exists(creds_path):
        print(" Файл creds.db не найден, запрашиваем данные у пользователя...")
        host = input("Введите хост PostgreSQL: ").strip()
        port = input("Введите порт: ").strip()
        user = input("Введите пользователя: ").strip()
        password = input("Введите пароль: ").strip()
    else:
        conn = sqlite3.connect(creds_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM access;")
        rows = cursor.fetchall()
        conn.close()
        if len(rows) == 0:
            raise ValueError(" Нет данных для подключения в creds.db")
        host, port, user, password = rows[0]

    os.environ["PG_HOST"] = host
    os.environ["PG_PORT"] = str(port)
    os.environ["PG_USER"] = user
    os.environ["PG_PASSWORD"] = password

    print(" Учётные данные PostgreSQL готовы")

    # ------------------------------
    #Чтение данных
    # ------------------------------
    if df is None:
        parquet_path = "data/processed/clean_data.parquet"
        if not os.path.exists(parquet_path):
            raise FileNotFoundError(f" Файл {parquet_path} не найден!")
        df = pd.read_parquet(parquet_path)
        print(f" Данные прочитаны из Parquet: {df.shape[0]} строк")

    # ------------------------------
    #Ввод параметров пользователя
    # ------------------------------
    table_name = input("Введите имя таблицы для загрузки: ").strip()
    num_rows = input(f"Сколько строк хотите загрузить? (макс {df.shape[0]}): ").strip()

    try:
        num_rows = int(num_rows)
        if num_rows <= 0 or num_rows > df.shape[0]:
            raise ValueError
    except ValueError:
        raise ValueError(f" Некорректное число строк (1-{df.shape[0]})")

    df = df.head(num_rows)
    print(f" Будет загружено {df.shape[0]} строк")

    # ------------------------------
    #Подключение к PostgreSQL
    # ------------------------------
    conn_pg = psycopg2.connect(
        host=host,
        port=port,
        dbname="homeworks",
        user=user,
        password=password
    )
    cursor_pg = conn_pg.cursor()

    # ------------------------------
    #Проверка таблицы
    # ------------------------------
    cursor_pg.execute("""
        SELECT table_name FROM information_schema.tables
        WHERE table_schema='public' AND table_name=%s;
    """, (table_name,))
    table_exists = cursor_pg.fetchone()

    if table_exists:
        print(f"⚙️ Таблица '{table_name}' существует — очищаем старые данные...")
        cursor_pg.execute(f"TRUNCATE TABLE public.{table_name};")
    else:
        print(f" Таблица '{table_name}' не найдена — создаем новую...")
        columns = ', '.join([f"{col} TEXT" for col in df.columns])
        cursor_pg.execute(f"CREATE TABLE public.{table_name} ({columns});")

    # ------------------------------
    #Загрузка данных
    # ------------------------------
    for _, row in df.iterrows():
        placeholders = ', '.join(['%s'] * len(row))
        cursor_pg.execute(f"INSERT INTO public.{table_name} VALUES ({placeholders})", tuple(row))

    conn_pg.commit()

    cursor_pg.execute(f"SELECT COUNT(*) FROM public.{table_name};")
    print(f" Загружено {cursor_pg.fetchone()[0]} строк в '{table_name}'")

    cursor_pg.close()
    conn_pg.close()
    print(" Загрузка завершена успешно ")
