import pandas as pd

# رابط الملف من Google Drive
FILE_ID = "1e_B0JuGIwMeVWKbchUdzw8xcAkh0hPbX"
file_url = f"https://drive.google.com/uc?id={FILE_ID}"

# قراءة البيانات
raw_data = pd.read_csv(file_url)

# طباعة أول 10 أسطر للتأكد
print(raw_data.head(10))
