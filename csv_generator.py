import pandas as pd

def generate_new_csv(df):
    file_name = "data.csv"
    data_to_csv = {
        "names": df["Funcionário"],
        "receita": df["Receita Gerada (R$)"],
        "gastos": df["Valor Gasto (R$)"],
        "categoria_gastos": df["Categoria do Gasto"]
    }

    pd.DataFrame(data_to_csv).to_csv(file_name, index = False)
    print("File successfully generated!")
    return file_name