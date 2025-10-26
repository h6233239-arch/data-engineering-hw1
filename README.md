# Asthma Risk & Severity Dataset

   ### [About Dataset](https://drive.google.com/file/d/1e_B0JuGIwMeVWKbchUdzw8xcAkh0hPbX/view?usp=drive_link)
   This synthetic dataset simulates health records of individuals with varying levels of asthma severity. It is designed to support predictive modeling, classification, and exploratory analysis in the healthcare domain.

The dataset contains patient-level data such as demographics, lifestyle factors, environmental exposures, and medical indicators that are known to influence asthma risk and severity.

Use cases include:

- [Asthma severity prediction]
- [Health risk scoring]
- [Impact analysis of factors like pollution, BMI, or smoking]
- [Educational machine learning tasks]


Since the data is fully synthetic, it is safe for public use and contains no personal or sensitive information.
## скрипт выгрузки файла из Google Drive 

     import pandas as pd

     FILE_ID = "1e_B0JuGIwMeVWKbchUdzw8xcAkh0hPbX"  # ID файла на Google Drive
     file_url = f"https://drive.google.com/uc?id={FILE_ID}"

      raw_data = pd.read_csv(file_url)     # читаем файл

      raw_data.head(10) 
     print(raw_data.head(10))
     
![скриншот1](скриншот1.jpg)
![скриншот2](скриншот2.jpg)
## скрипт приведения типов

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


     
## Зависимости 
    pandas
    matplotlib
    jupyterlab
    gdown
    wget
    ipykernel


## [EDA](https://nbviewer.org/github/h6233239-arch/data-engineering-hw1/blob/main/notebooks/EAD.ipynb)

