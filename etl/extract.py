import pandas as pd
import os

RAW_DIR = "data/raw"

def extract_data(file_id: str = None) -> pd.DataFrame:
    """
    Загрузка данных из Google Drive по ID файла.
    Если ID не передан, запрашиваем у пользователя.

    Args:
        file_id: ID файла на Google Drive (опционально)

    Returns:
        pd.DataFrame после загрузки
    """
    if file_id is None:
        file_id = input("🟢 أدخل Google Drive file ID: ").strip()

    file_url = f"https://drive.google.com/uc?id={file_id}"

    try:
        df = pd.read_csv(file_url)
    except Exception as e:
        raise RuntimeError(f"❌ Ошибка при загрузке файла: {e}")

    if df.empty:
        raise ValueError("❌ Файл пустой!")

    os.makedirs(RAW_DIR, exist_ok=True)
    output_path = os.path.join(RAW_DIR, "raw_data.csv")
    df.to_csv(output_path, index=False)

    print(f"✅ Данные загружены и сохранены в {output_path}")
    return df

if __name__ == "__main__":
    df = extract_data()
    print(df.head())
