import pandas as pd
import chardet

def fileCharset(filename:str) -> str:
    with open(filename, 'rb') as file:
        encoding = chardet.detect(file.read(1000))
        return encoding["encoding"]

try:
    filename = '../data/csv/centros-educativos-rd-2023-2024.csv'
    encoding = fileCharset(filename)
    schools_df = pd.read_csv(filename, delimiter=';', encoding=encoding)

except FileNotFoundError as e:
    print("An error has occurred")

print(schools_df.head())
print(schools_df.info())
print(schools_df.describe())
