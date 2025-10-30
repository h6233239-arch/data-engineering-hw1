import sys
from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    # Проверяем наличие аргумента
    if len(sys.argv) < 2:
        print("❌ Ошибка: необходимо передать хотя бы 1 аргумент (Google Drive file ID).")
        print("Пример: python etl/main.py 1e_B0JuGIwMeVWKbchUdzw8xcAkh0hPbX")
        sys.exit(1)

    # Получаем file_id из аргумента командной строки
    file_id = sys.argv[1].strip()
    print(f"🟢 Получен file_id: {file_id}")

    # 1️⃣ Extract
    df_raw = extract_data(file_id)

    # 2️⃣ Transform
    df_clean = transform_data(df_raw)

    # 3️⃣ Load
    load_data(df_clean)

    print("🎯 Процесс ETL успешно завершён!")

if __name__ == "__main__":
    main()
