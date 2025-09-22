import pandas as pd

FILE_ID = "1e_B0JuGIwMeVWKbchUdzw8xcAkh0hPbX"  # ID файла на Google Drive
file_url = f"https://drive.google.com/uc?id={FILE_ID}"

raw_data = pd.read_csv(file_url)     # читаем файл

raw_data.head(10) 