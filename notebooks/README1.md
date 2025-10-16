```python
import pandas as pd

# Чтение локального файла
df = pd.read_csv("processed_asthma.csv")

# Просмотр первых 5 строк
df.head()

```




<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Patient_ID</th>
      <th>Age</th>
      <th>Gender</th>
      <th>BMI</th>
      <th>Smoking_Status</th>
      <th>Family_History</th>
      <th>Allergies</th>
      <th>Air_Pollution_Level</th>
      <th>Physical_Activity_Level</th>
      <th>Occupation_Type</th>
      <th>Comorbidities</th>
      <th>Medication_Adherence</th>
      <th>Number_of_ER_Visits</th>
      <th>Peak_Expiratory_Flow</th>
      <th>FeNO_Level</th>
      <th>Has_Asthma</th>
      <th>Asthma_Control_Level</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ASTH100000</td>
      <td>52</td>
      <td>Female</td>
      <td>27.6</td>
      <td>Former</td>
      <td>1</td>
      <td>NaN</td>
      <td>Moderate</td>
      <td>Sedentary</td>
      <td>Outdoor</td>
      <td>Diabetes</td>
      <td>0.38</td>
      <td>0</td>
      <td>421.0</td>
      <td>46.0</td>
      <td>0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ASTH100001</td>
      <td>15</td>
      <td>Male</td>
      <td>24.6</td>
      <td>Former</td>
      <td>0</td>
      <td>Dust</td>
      <td>Low</td>
      <td>Moderate</td>
      <td>Indoor</td>
      <td>Both</td>
      <td>0.60</td>
      <td>2</td>
      <td>297.6</td>
      <td>22.9</td>
      <td>0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ASTH100002</td>
      <td>72</td>
      <td>Female</td>
      <td>17.6</td>
      <td>Never</td>
      <td>0</td>
      <td>NaN</td>
      <td>Moderate</td>
      <td>Moderate</td>
      <td>Indoor</td>
      <td>NaN</td>
      <td>0.38</td>
      <td>0</td>
      <td>303.3</td>
      <td>15.3</td>
      <td>0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ASTH100003</td>
      <td>61</td>
      <td>Male</td>
      <td>16.8</td>
      <td>Never</td>
      <td>0</td>
      <td>Multiple</td>
      <td>High</td>
      <td>Sedentary</td>
      <td>Outdoor</td>
      <td>Both</td>
      <td>0.60</td>
      <td>1</td>
      <td>438.0</td>
      <td>40.1</td>
      <td>1</td>
      <td>Poorly Controlled</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ASTH100004</td>
      <td>21</td>
      <td>Male</td>
      <td>30.2</td>
      <td>Never</td>
      <td>0</td>
      <td>NaN</td>
      <td>Moderate</td>
      <td>Active</td>
      <td>Indoor</td>
      <td>NaN</td>
      <td>0.82</td>
      <td>3</td>
      <td>535.0</td>
      <td>27.7</td>
      <td>0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>

## 1️⃣ Первичный просмотр данных

После загрузки датасета `processed_asthma.csv` были выведены первые 5 строк таблицы.

Данные содержат как числовые, так и категориальные признаки.  
Основные столбцы:
- **Числовые:** `Age`, `BMI`, `Family_History`, `Medication_Adherence`, `Number_of_ER_Visits`, `Peak_Expiratory_Flow`, `FeNO_Level`, `Has_Asthma`
- **Категориальные:** `Patient_ID`, `Gender`, `Smoking_Status`, `Allergies`, `Air_Pollution_Level`, `Physical_Activity_Level`, `Occupation_Type`, `Comorbidities`, `Asthma_Control_Level`

В таблице видно наличие пропусков (NaN) в некоторых столбцах, например:
- `Allergies`
- `Comorbidities`
- `Asthma_Control_Level`

Структура данных выглядит корректной и последовательной: каждая строка представляет одного пациента с набором медицинских и поведенческих характеристик.  
Следующий шаг — анализ типов данных и общей статистики.



```python
# Проверка структуры данных
df.info()

# Основная статистика для числовых столбцов
df.describe()

```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 10000 entries, 0 to 9999
    Data columns (total 17 columns):
     #   Column                   Non-Null Count  Dtype  
    ---  ------                   --------------  -----  
     0   Patient_ID               10000 non-null  object 
     1   Age                      10000 non-null  int64  
     2   Gender                   10000 non-null  object 
     3   BMI                      10000 non-null  float64
     4   Smoking_Status           10000 non-null  object 
     5   Family_History           10000 non-null  int64  
     6   Allergies                7064 non-null   object 
     7   Air_Pollution_Level      10000 non-null  object 
     8   Physical_Activity_Level  10000 non-null  object 
     9   Occupation_Type          10000 non-null  object 
     10  Comorbidities            5033 non-null   object 
     11  Medication_Adherence     10000 non-null  float64
     12  Number_of_ER_Visits      10000 non-null  int64  
     13  Peak_Expiratory_Flow     10000 non-null  float64
     14  FeNO_Level               10000 non-null  float64
     15  Has_Asthma               10000 non-null  int64  
     16  Asthma_Control_Level     2433 non-null   object 
    dtypes: float64(4), int64(4), object(9)
    memory usage: 1.3+ MB
    





</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>BMI</th>
      <th>Family_History</th>
      <th>Medication_Adherence</th>
      <th>Number_of_ER_Visits</th>
      <th>Peak_Expiratory_Flow</th>
      <th>FeNO_Level</th>
      <th>Has_Asthma</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>10000.000000</td>
      <td>10000.000000</td>
      <td>10000.000000</td>
      <td>10000.000000</td>
      <td>10000.000000</td>
      <td>10000.000000</td>
      <td>10000.000000</td>
      <td>10000.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>44.930700</td>
      <td>25.053320</td>
      <td>0.303400</td>
      <td>0.497998</td>
      <td>1.015900</td>
      <td>400.884090</td>
      <td>25.101420</td>
      <td>0.243300</td>
    </tr>
    <tr>
      <th>std</th>
      <td>25.653559</td>
      <td>4.874466</td>
      <td>0.459749</td>
      <td>0.224809</td>
      <td>1.020564</td>
      <td>97.531113</td>
      <td>9.840184</td>
      <td>0.429096</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>15.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>150.000000</td>
      <td>5.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>23.000000</td>
      <td>21.600000</td>
      <td>0.000000</td>
      <td>0.320000</td>
      <td>0.000000</td>
      <td>334.800000</td>
      <td>18.200000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>45.000000</td>
      <td>25.000000</td>
      <td>0.000000</td>
      <td>0.500000</td>
      <td>1.000000</td>
      <td>402.500000</td>
      <td>25.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>67.000000</td>
      <td>28.400000</td>
      <td>1.000000</td>
      <td>0.670000</td>
      <td>2.000000</td>
      <td>468.700000</td>
      <td>31.700000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>89.000000</td>
      <td>45.000000</td>
      <td>1.000000</td>
      <td>0.990000</td>
      <td>6.000000</td>
      <td>600.000000</td>
      <td>63.900000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>

## 2️⃣ Информация о данных и базовая статистика

Проведен анализ структуры данных с помощью `df.info()` и `df.describe()`.

### Основные выводы:

- Датасет содержит **10,000 строк и 17 столбцов**.
- Типы данных:
  - **int64:** `Age`, `Family_History`, `Number_of_ER_Visits`, `Has_Asthma`
  - **float64:** `BMI`, `Medication_Adherence`, `Peak_Expiratory_Flow`, `FeNO_Level`
  - **object:** `Patient_ID`, `Gender`, `Smoking_Status`, `Allergies`, `Air_Pollution_Level`, `Physical_Activity_Level`, `Occupation_Type`, `Comorbidities`, `Asthma_Control_Level`
- Некоторые столбцы содержат пропущенные значения:
  - `Allergies` — 7064 заполнено (2936 пропусков)
  - `Comorbidities` — 5033 заполнено (4967 пропусков)
  - `Asthma_Control_Level` — 2433 заполнено (7567 пропусков)

### Статистика числовых признаков:

| Признак | Среднее | Стандартное отклонение | Минимум | 25% | 50% | 75% | Максимум |
|---------|--------|----------------------|---------|-----|-----|-----|---------|
| Age | 44.93 | 25.65 | 1 | 23 | 45 | 67 | 89 |
| BMI | 25.05 | 4.87 | 15 | 21.6 | 25 | 28.4 | 45 |
| Family_History | 0.30 | 0.46 | 0 | 0 | 0 | 1 | 1 |
| Medication_Adherence | 0.50 | 0.22 | 0 | 0.32 | 0.5 | 0.67 | 0.99 |
| Number_of_ER_Visits | 1.02 | 1.02 | 0 | 0 | 1 | 2 | 6 |
| Peak_Expiratory_Flow | 400.88 | 97.53 | 150 | 334.8 | 402.5 | 468.7 | 600 |
| FeNO_Level | 25.10 | 9.84 | 5 | 18.2 | 25 | 31.7 | 63.9 |
| Has_Asthma | 0.24 | 0.43 | 0 | 0 | 0 | 0 | 1 |

- Данные числовых столбцов показывают разумный диапазон значений без очевидных ошибок.
- Следующий шаг — анализ пропущенных значений и оценка качества данных для категориальных столбцов.



```python
# Подсчет пропущенных значений
missing = df.isnull().sum()

# Процент пропусков
missing_percent = (missing / len(df)) * 100

# Создаем таблицу с результатами
missing_df = pd.DataFrame({
    'Пропущенные значения': missing,
    'Процент %': missing_percent
})

missing_df

```





<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Пропущенные значения</th>
      <th>Процент %</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Patient_ID</th>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Age</th>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Gender</th>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>BMI</th>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Smoking_Status</th>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Family_History</th>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Allergies</th>
      <td>2936</td>
      <td>29.36</td>
    </tr>
    <tr>
      <th>Air_Pollution_Level</th>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Physical_Activity_Level</th>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Occupation_Type</th>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Comorbidities</th>
      <td>4967</td>
      <td>49.67</td>
    </tr>
    <tr>
      <th>Medication_Adherence</th>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Number_of_ER_Visits</th>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Peak_Expiratory_Flow</th>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>FeNO_Level</th>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Has_Asthma</th>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Asthma_Control_Level</th>
      <td>7567</td>
      <td>75.67</td>
    </tr>
  </tbody>
</table>
</div>


## 3️⃣ Анализ пропущенных значений

Проведен анализ пропущенных данных в датасете.

### Основные выводы:

- Столбцы без пропущенных значений:
  - `Patient_ID`, `Age`, `Gender`, `BMI`, `Smoking_Status`, `Family_History`, `Air_Pollution_Level`, `Physical_Activity_Level`, `Occupation_Type`, `Medication_Adherence`, `Number_of_ER_Visits`, `Peak_Expiratory_Flow`, `FeNO_Level`, `Has_Asthma`

- Столбцы с пропущенными значениями:
  - `Allergies` — 2,936 пропусков (29,36%)
  - `Comorbidities` — 4,967 пропусков (49,67%)
  - `Asthma_Control_Level` — 7,567 пропусков (75,67%)

### Рекомендации:

- Для дальнейшего анализа или моделирования необходимо обработать пропуски:
  - удалить строки/столбцы с большим количеством пропусков, или
  - заполнить пропущенные значения подходящими значениями (imputation).

- Большинство числовых и категориальных признаков полные и готовы к следующему этапу — анализу выбросов.


```python
# Выбираем числовые столбцы
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

# Расчет IQR для выявления выбросов
Q1 = df[numeric_cols].quantile(0.25)
Q3 = df[numeric_cols].quantile(0.75)
IQR = Q3 - Q1

# Подсчет выбросов для каждого числового столбца
outliers = ((df[numeric_cols] < (Q1 - 1.5 * IQR)) | (df[numeric_cols] > (Q3 + 1.5 * IQR))).sum()
outliers_percent = (outliers / len(df)) * 100

outliers_df = pd.DataFrame({
    'Выбросы': outliers,
    'Процент %': outliers_percent
})
outliers_df

```





<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Выбросы</th>
      <th>Процент %</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Age</th>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>BMI</th>
      <td>24</td>
      <td>0.24</td>
    </tr>
    <tr>
      <th>Family_History</th>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Medication_Adherence</th>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Number_of_ER_Visits</th>
      <td>3</td>
      <td>0.03</td>
    </tr>
    <tr>
      <th>Peak_Expiratory_Flow</th>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>FeNO_Level</th>
      <td>41</td>
      <td>0.41</td>
    </tr>
    <tr>
      <th>Has_Asthma</th>
      <td>2433</td>
      <td>24.33</td>
    </tr>
  </tbody>
</table>
</div>


## 4️⃣ Анализ выбросов (Outliers)

Проведен анализ выбросов для числовых столбцов с использованием метода межквартильного размаха (IQR).

### Основные выводы:

- Столбцы с минимальным количеством выбросов:
  - `BMI` — 24 выброса (0,24%)
  - `Number_of_ER_Visits` — 3 выброса (0,03%)
  - `FeNO_Level` — 41 выброс (0,41%)

- Столбцы без выбросов:
  - `Age`, `Family_History`, `Medication_Adherence`, `Peak_Expiratory_Flow`

- Столбец с значительным количеством выбросов:
  - `Has_Asthma` — 2,433 выброса (24,33%)

### Рекомендации:

- Большинство числовых признаков чистые и готовы к дальнейшему анализу.
- Столбец `Has_Asthma` требует дополнительной проверки и, при необходимости, обработки выбросов перед построением моделей или детальным анализом.


```python
# Создаем сводную таблицу с пропусками и выбросами
metrics_df = pd.DataFrame({
    'Пропущенные значения %': (df.isnull().sum() / len(df)) * 100,
    'Выбросы %': ((df[numeric_cols] < (Q1 - 1.5*IQR)) | (df[numeric_cols] > (Q3 + 1.5*IQR))).sum() / len(df) * 100
})

# Для категориальных столбцов добавляем только пропуски
for col in df.select_dtypes(include=['object']).columns:
    if col not in metrics_df.index:
        metrics_df.loc[col] = [df[col].isnull().sum() / len(df) * 100, 0]

metrics_df = metrics_df.sort_index()
metrics_df


```





<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Пропущенные значения %</th>
      <th>Выбросы %</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Age</th>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Air_Pollution_Level</th>
      <td>0.00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Allergies</th>
      <td>29.36</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Asthma_Control_Level</th>
      <td>75.67</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>BMI</th>
      <td>0.00</td>
      <td>0.24</td>
    </tr>
    <tr>
      <th>Comorbidities</th>
      <td>49.67</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Family_History</th>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>FeNO_Level</th>
      <td>0.00</td>
      <td>0.41</td>
    </tr>
    <tr>
      <th>Gender</th>
      <td>0.00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Has_Asthma</th>
      <td>0.00</td>
      <td>24.33</td>
    </tr>
    <tr>
      <th>Medication_Adherence</th>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Number_of_ER_Visits</th>
      <td>0.00</td>
      <td>0.03</td>
    </tr>
    <tr>
      <th>Occupation_Type</th>
      <td>0.00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Patient_ID</th>
      <td>0.00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Peak_Expiratory_Flow</th>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Physical_Activity_Level</th>
      <td>0.00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Smoking_Status</th>
      <td>0.00</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>


## 4️⃣ Анализ выбросов (Outliers)

Проведен анализ выбросов для числовых столбцов с использованием метода межквартильного размаха (IQR).

### Основные выводы:

- Столбцы с минимальным количеством выбросов:
  - `BMI` — 24 выброса (0,24%)
  - `Number_of_ER_Visits` — 3 выброса (0,03%)
  - `FeNO_Level` — 41 выброс (0,41%)

- Столбцы без выбросов:
  - `Age`, `Family_History`, `Medication_Adherence`, `Peak_Expiratory_Flow`

- Столбец с значительным количеством выбросов:
  - `Has_Asthma` — 2,433 выброса (24,33%)

### Рекомендации:

- Большинство числовых признаков чистые и готовы к дальнейшему анализу.
- Столбец `Has_Asthma` требует дополнительной проверки и, при необходимости, обработки выбросов перед построением моделей или детальным анализом.


## 5️⃣ Итоговое заключение и сводная таблица метрик

Проведен сводный анализ качества данных, объединяющий информацию о пропущенных значениях и выбросах.

### Основные выводы:

- Столбцы без пропусков и без выбросов:
  - `Age`, `Family_History`, `Medication_Adherence`, `Number_of_ER_Visits`, `Peak_Expiratory_Flow`

- Столбцы с пропущенными значениями (значительная часть данных):
  - `Allergies` — 29,36%
  - `Comorbidities` — 49,67%
  - `Asthma_Control_Level` — 75,67%
  - Остальные категориальные признаки (`Gender`, `Patient_ID`, `Occupation_Type`, `Physical_Activity_Level`, `Smoking_Status`, `Air_Pollution_Level`) не имеют числовых выбросов, но содержат пропуски, если смотреть по фактическим данным.

- Столбцы с выбросами:
  - `BMI` — 0,24%
  - `Number_of_ER_Visits` — 0,03%
  - `FeNO_Level` — 0,41%
  - `Has_Asthma` — 24,33%

### Рекомендации:

- Для дальнейшего анализа или построения моделей необходимо обработать пропуски в `Allergies`, `Comorbidities` и `Asthma_Control_Level`.
- Столбец `Has_Asthma` требует проверки выбросов.
- Остальные столбцы готовы к использованию и дальнейшему анализу.
- Датасет в целом структурирован корректно и позволяет проводить дальнейший статистический и корреляционный анализ.

