import os
from dotenv import load_dotenv
import gspread
import pandas as pd
from processor import load_data
from csv_generator import generate_new_csv
from llm_client import generate_analysis

load_dotenv()

df = load_data()
file_name = generate_new_csv(df)

if file_name:
    generate_analysis(file_name)
else:
    print("Empty file name")


