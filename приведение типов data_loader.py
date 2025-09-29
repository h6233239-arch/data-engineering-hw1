import pandas as pd

# Ссылка на файл из Google Drive
FILE_ID = "1e_B0JuGIwMeVWKbchUdzw8xcAkh0hPbX"
file_url = f"https://drive.google.com/uc?id={FILE_ID}"

# Чтение данных
df = pd.read_csv(file_url)

# ====== Преобразование типов данных ======
# Целые числа
df["Age"] = df["Age"].astype("int64")
df["Family_History"] = df["Family_History"].astype("int64")
df["Number_of_ER_Visits"] = df["Number_of_ER_Visits"].astype("int64")
df["Has_Asthma"] = df["Has_Asthma"].astype("int64")

# Десятичные числа (с плавающей точкой)
df["BMI"] = df["BMI"].astype("float64")
df["Medication_Adherence"] = df["Medication_Adherence"].astype("float64")
df["Peak_Expiratory_Flow"] = df["Peak_Expiratory_Flow"].astype("float64")
df["FeNO_Level"] = df["FeNO_Level"].astype("float64")

# Текстовые/категориальные данные
categorical_cols = [
    "Patient_ID", "Gender", "Smoking_Status", "Allergies",
    "Air_Pollution_Level", "Physical_Activity_Level",
    "Occupation_Type", "Comorbidities", "Asthma_Control_Level"
]
for col in categorical_cols:
    df[col] = df[col].astype("category")

# ====== Сохранение нового файла ======
output_file = "processed_asthma.csv"
df.to_csv(output_file, index=False, encoding="utf-8")

print(f"Обработанный файл сохранен: {output_file}")
print(df.dtypes)