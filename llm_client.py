from openai import OpenAI
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

base_url = os.getenv("BASE_URL")
api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("MODEL")


client = OpenAI(
    api_key= api_key,
    base_url= base_url
)

def generate_analysis(file_name):
    data = pd.read_csv(file_name)
    response = client.chat.completions.create(
        model = model, 
        messages = [
            {
                "role": "system",
                "content": """You are a data analyst who must receive data from a spreadsheet and, based on your knowledge, 
                report on the potential problems a given company may face based on employee expenses. 
                In addition, you must also suggest possible ways to generate more profit."""
            },
            {
                "role": "user",
                "content": f"""Estou a enviar-lhe um ficheiro contendo dados sobre despesas e receitas geradas por cada colaborador da minha empresa. 
                Com base exclusivamente nas informações contidas neste ficheiro, realize uma análise financeira estratégica executando as seguintes tarefas;
                  1-Diagnóstico Financeiro: Identifique padrões de gastos, colaboradores com baixa rentabilidade e potenciais riscos financeiros caso o cenário atual se mantenha.
                  2- Prevenção de Riscos: Aponte quais as despesas que são alarmantes ou desnecessárias em relação à receita gerada.
                  3- Proponha ações práticas para aumentar a margem de lucro ou otimizar a eficiência de cada colaborador.
                  4- Crie uma breve tabela comparativa de "Receita vs. Gastos" por colaborador para facilitar a minha visualização.
                  Diretrizes:
                  Seja direto e objetivo, baseando-se apenas nos dados do arquivo: {data}
                  Não utilize informações externas ou generalistas; foque estritamente na realidade dos dados apresentados.
                  Se encontrar alguma discrepância ou valor atípico (outlier) que mereça a minha atenção, destaque-o claramente.
                  Corte comentários desnecessários, foque em retornar apenas o que está sendo pedido
                     """
            }
        ]
    )

    llm_response = (response.choices[0].message.content).strip()
    print(llm_response)
    
