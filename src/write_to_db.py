import os
import psycopg2
import pandas as pd

# 1️⃣ Чтение учетных данных из переменных среды
host = os.getenv("PG_HOST")
port = os.getenv("PG_PORT")
user = os.getenv("PG_USER")
password = os.getenv("PG_PASSWORD")
dbname = "homeworks"  # Имя базы данных PostgreSQL

# Проверяем, что все переменные заданы
if not all([host, port, user, password]):
    raise ValueError("❌ Ошибка: Не заданы все переменные среды (PG_HOST, PG_PORT, PG_USER, PG_PASSWORD)!")

# 2️⃣ Подключение к PostgreSQL
conn_pg = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
cursor_pg = conn_pg.cursor()

# 3️⃣ Имя таблицы
table_name = 'alahmad'

# 4️⃣ Проверяем, существует ли таблица в схеме public
cursor_pg.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema='public' AND table_name=%s;
""", (table_name,))
table_exists = cursor_pg.fetchone()

# 5️⃣ Чтение данных из CSV
df = pd.read_csv('processed_asthma.csv').head(100)  # Берем первые 100 строк

if table_exists:
    # Таблица существует → очищаем все старые данные
    print(f"Таблица '{table_name}' существует, очищаем данные...")
    cursor_pg.execute(f"TRUNCATE TABLE public.{table_name};")
else:
    # Таблицы нет → создаем новую
    print(f"Таблица '{table_name}' не найдена, создаем новую...")
    # Формируем список колонок как TEXT
    columns = ', '.join([f"{col} TEXT" for col in df.columns])
    cursor_pg.execute(f"CREATE TABLE public.{table_name} ({columns});")

# 6️⃣ Вставляем новые данные
for _, row in df.iterrows():
    values = tuple(row)
    placeholders = ', '.join(['%s'] * len(row))
    cursor_pg.execute(f"INSERT INTO public.{table_name} VALUES ({placeholders})", values)

# 7️⃣ Сохраняем изменения
conn_pg.commit()

# 8️⃣ ✅ Проверка после вставки
# Количество строк в таблице
cursor_pg.execute(f"SELECT COUNT(*) FROM public.{table_name};")
row_count = cursor_pg.fetchone()[0]
print(f"\nКоличество строк в таблице '{table_name}': {row_count}")

# Просмотр первых 5 строк таблицы
df_check = pd.read_sql(f"SELECT * FROM public.{table_name} LIMIT 5;", conn_pg)
print("\nПервые 5 строк таблицы:")
print(df_check)

# 9️⃣ Закрываем соединение
cursor_pg.close()
conn_pg.close()

print(f"\nДанные успешно добавлены и проверены в таблице '{table_name}' ✅")
