import os
from dotenv import load_dotenv
import gspread
import pandas as pd

load_dotenv()

gc = gspread.service_account(filename=os.getenv("FILE_NAME"))
sh = gc.open(os.getenv("PATH_NAME")).sheet1

data = sh.get_all_records()
df = pd.DataFrame(data)

df['Valor Monetário (R$)'] = pd.to_numeric(df['Valor Monetário (R$)'])
df['Data'] = pd.to_datetime(df['Data'])

media_gastos = df['Valor Monetário (R$)'].mean()
print(f"Média de gastos atual: R$ {media_gastos:.2f}")
