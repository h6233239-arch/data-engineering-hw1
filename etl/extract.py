import pandas as pd
import os

RAW_DIR = "data/raw"

def extract_data(file_id: str = None) -> pd.DataFrame:
    """
    Загрузка данных из Google Drive по ID файла.
    Если ID не указан, программа запросит его у пользователя.

    Аргументы:
        file_id: ID файла в Google Drive (необязательно)

    Возвращает:
        pd.DataFrame после успешной загрузки
    """
    if file_id is None:
        file_id = input(" Введите Google Drive file ID: ").strip()

    file_url = f"https://drive.google.com/uc?id={file_id}"

    try:
        df = pd.read_csv(file_url)
    except Exception as e:
        raise RuntimeError(f" Ошибка при загрузке файла: {e}")

    if df.empty:
        raise ValueError(" Файл пустой!")

    os.makedirs(RAW_DIR, exist_ok=True)
    output_path = os.path.join(RAW_DIR, "raw_data.csv")
    df.to_csv(output_path, index=False)

    print(f" Данные успешно загружены и сохранены в {output_path}")
    return df

if __name__ == "__main__":
    df = extract_data()
    print(df.head())
