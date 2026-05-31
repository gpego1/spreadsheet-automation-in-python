import os
from dotenv import load_dotenv
import gspread
import pandas as pd

load_dotenv()

def load_data():
    gc = gspread.service_account(filename=os.getenv("FILE_NAME"))
    sh = gc.open(os.getenv("PATH_NAME")).sheet1
    data = sh.get_all_records()
    return pd.DataFrame(data)

