import pandas as pd
import numpy as np
import os

def transform_data(df: pd.DataFrame, output_path: str = "data/processed/clean_data.csv") -> pd.DataFrame:
    """
    Очистка и преобразование данных + валидация.
    
    Args:
        df: исходный DataFrame
        output_path: путь для сохранения очищенных данных (CSV и Parquet)
    
    Returns:
        pd.DataFrame после очистки
    """
    original_rows = df.shape[0]

    # ----------- Редактирование имен столбцов -----------
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # ----------- Очистка текстовых столбцов -----------
    text_cols = df.select_dtypes(include='object').columns.tolist()
    for col in text_cols:
        df[col] = df[col].astype(str).str.strip().str.lower()

    fill_values = {
        "allergies": "none",
        "comorbidities": "none",
        "asthma_control_level": "unknown"
    }

    for col in text_cols:
        if col in fill_values:
            df[col] = df[col].replace({'nan': fill_values[col]}).fillna(fill_values[col])
        else:
            df[col] = df[col].replace({'nan': 'غير محدد'}).fillna('غير محدد')

    # ----------- Числовые столбцы -----------
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        df[col] = df[col].fillna(0)

    # ----------- Проверка некорректных значений -----------
    if 'age' in df.columns:
        df.loc[(df['age'] < 0) | (df['age'] > 120), 'age'] = np.nan
        df['age'] = df['age'].fillna(df['age'].median())

    if 'bmi' in df.columns:
        df.loc[(df['bmi'] < 10) | (df['bmi'] > 70), 'bmi'] = np.nan
        df['bmi'] = df['bmi'].fillna(df['bmi'].median())

    # ----------- Обработка дат -----------
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

    print(f" Данные очищены: исходно {original_rows} строк, после очистки {df.shape[0]} строк")

    # ----------- Сохранение в CSV -----------
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False, encoding="utf-8")
        print(f" Очищенные данные сохранены в CSV: {output_path}")

        # ----------- Сохранение в Parquet -----------
        parquet_path = os.path.splitext(output_path)[0] + ".parquet"
        df.to_parquet(parquet_path, index=False)
        print(f" Очищенные данные сохранены в Parquet: {parquet_path}")

    # ----------- Валидация выходных параметров -----------
    print("\n Валидация выходных параметров:")
    print(f"- Количество строк: {df.shape[0]}")
    print(f"- Количество колонок: {df.shape[1]}")
    print(f"- Названия колонок и типы:\n{df.dtypes}")
    print(f"- Первые 5 строк:\n{df.head()}")
    print(f"- Количество пропусков по колонкам:\n{df.isna().sum()}")

    return df

if __name__ == "__main__":
    df = pd.read_csv("data/raw/raw_data.csv")
    df_clean = transform_data(df)
