import os
import psycopg2
import pandas as pd
import numpy as np

# ==============================
# 1️⃣ Чтение и очистка данных
# ==============================
file_path = "processed_asthma.csv"  # Путь к исходному CSV

# Чтение CSV
df = pd.read_csv(file_path)
original_rows = df.shape[0]

# ----------- Приведение названий столбцов к единому формату -----------
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

# ----------- Очистка текстовых столбцов -----------
text_cols = df.select_dtypes(include='object').columns.tolist()
for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.lower()  # Убираем пробелы и переводим в нижний регистр

# ----------- Обработка пропусков для специфических колонок -----------
fill_values = {
    "allergies": "none",
    "comorbidities": "none",
    "asthma_control_level": "unknown"
}

for col in text_cols:
    if col in fill_values:
        df[col] = df[col].replace({'nan': fill_values[col]}).fillna(fill_values[col])
    else:
        df[col] = df[col].replace({'nan': 'не_указано'}).fillna('не_указано')

# ----------- Обработка числовых столбцов -----------
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    df[col] = df[col].fillna(0)

# ----------- Проверка и исправление некорректных значений -----------
if 'age' in df.columns:
    df.loc[(df['age'] < 0) | (df['age'] > 120), 'age'] = np.nan
    df['age'] = df['age'].fillna(df['age'].median())

if 'bmi' in df.columns:
    df.loc[(df['bmi'] < 10) | (df['bmi'] > 70), 'bmi'] = np.nan
    df['bmi'] = df['bmi'].fillna(df['bmi'].median())

# ----------- Обработка столбцов с датами (если есть) -----------
date_cols = []
for col in text_cols:
    try:
        df[col] = pd.to_datetime(df[col], errors='raise')
        date_cols.append(col)
    except:
        pass

for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce')
    df[col] = df[col].fillna(pd.Timestamp('2000-01-01'))

# ----------- Удаление дубликатов -----------
df = df.drop_duplicates()

# ----------- Оставляем только первые 100 строк -----------
df = df.head(100)

print(f"✅ Данные очищены: исходно {original_rows} строк, после очистки и выбора первых 100 строк {df.shape[0]} строк")

# ==============================
# 2️⃣ Подключение к PostgreSQL
# ==============================
host = os.getenv("PG_HOST")
port = os.getenv("PG_PORT")
user = os.getenv("PG_USER")
password = os.getenv("PG_PASSWORD")
dbname = "homeworks"

if not all([host, port, user, password]):
    raise ValueError("❌ Ошибка: Не заданы все переменные окружения (PG_HOST, PG_PORT, PG_USER, PG_PASSWORD)!")

# Подключение к базе
conn_pg = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
cursor_pg = conn_pg.cursor()

table_name = 'alahmad'

# ----------- Проверка существования таблицы -----------
cursor_pg.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema='public' AND table_name=%s;
""", (table_name,))
table_exists = cursor_pg.fetchone()

# ----------- Создание или очистка таблицы -----------
if table_exists:
    print(f"⚙️ Таблица '{table_name}' существует — очищаем данные...")
    cursor_pg.execute(f"TRUNCATE TABLE public.{table_name};")
else:
    print(f"🆕 Таблица '{table_name}' не найдена — создаем новую...")
    columns = ', '.join([f"{col} TEXT" for col in df.columns])
    cursor_pg.execute(f"CREATE TABLE public.{table_name} ({columns});")

# ==============================
# 3️⃣ Вставка данных в PostgreSQL
# ==============================
for _, row in df.iterrows():
    values = tuple(row)
    placeholders = ', '.join(['%s'] * len(row))
    cursor_pg.execute(f"INSERT INTO public.{table_name} VALUES ({placeholders})", values)

# Сохраняем изменения
conn_pg.commit()

# ==============================
# 4️⃣ Проверка результата
# ==============================
cursor_pg.execute(f"SELECT COUNT(*) FROM public.{table_name};")
row_count = cursor_pg.fetchone()[0]
print(f"\nКоличество строк в таблице '{table_name}': {row_count}")

df_check = pd.read_sql(f"SELECT * FROM public.{table_name} LIMIT 10;", conn_pg)
print("\nПервые 10 строк таблицы:")
print(df_check)

cursor_pg.close()
conn_pg.close()

print(f"\n🎉 Данные очищены и успешно загружены в таблицу '{table_name}' ✅")
