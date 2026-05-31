# Spreadsheet Automation in Python

Este projeto é uma ferramenta avançada de automação financeira que utiliza Python para analisar dados de orçamentos armazenados no **Google Sheets**. O sistema automatiza desde a leitura em tempo real até à geração de relatórios estratégicos com auxílio de Inteligência Artificial.

---

## 🚀 Como funciona o projeto
O script atua como um "analista de dados" pessoal, seguindo um fluxo automatizado:

1. **Conexão em Tempo Real:** Utiliza a API do Google Sheets para ler os seus dados financeiros diretamente da nuvem.
2. **Processamento de Dados:** Utiliza a biblioteca `pandas` para estruturar os dados, tratar formatos e realizar limpezas necessárias.
3. **Extração Seletiva:** O script gera automaticamente um ficheiro `data.csv` contendo apenas as informações essenciais (nome do funcionário, receitas, gastos e categorias), otimizando o envio para processamento.
4. **Análise por IA:** O ficheiro processado é enviado para um agente de IA, que realiza uma análise crítica de receita vs. gastos, identifica problemas, riscos e sugere melhorias baseadas nos números reais.
5. **Feedback Estratégico:** O sistema retorna um relatório sumarizado e estruturado para apoiar a sua tomada de decisão financeira.



---

## 📋 Pré-requisitos

Antes de executar o código, certifique-se de ter:
* Python 3.x instalado.
* Uma conta no [Google Cloud Console](https://console.cloud.google.com/) para gerar as suas credenciais de API.

---

## 🛠️ Passo a Passo para Configuração

### 1. Preparação da Planilha
1. Transfira o ficheiro de exemplo `dados_financeiros.xlsx`.
2. Abra o seu **Google Drive**.
3. Faça o upload do ficheiro `.xlsx` e abra-o com o **Google Planilhas (Google Sheets)**.
4. No canto superior direito, clique em **Partilhar** e adicione o e-mail da sua "Conta de Serviço" (gerada no Google Cloud - encontrada no campo `client_email` do seu ficheiro JSON) com permissão de **Editor**.

### 2. Configuração do Ambiente
1. Clone este repositório:
   ```bash
   git clone [https://github.com/gpego1/spreadsheet-automation-in-python.git](https://github.com/gpego1/spreadsheet-automation-in-python.git)
   cd spreadsheet-automation-in-python

2. Crie Ambiente Virtual
    ```bash
    python -m venv venv
    .\venv\Scripts\activate

3. Instale dependências
   ```bash
   pip install -r requirements.txt

### 3. Variáveis de Ambiente
   1. Configurar arquivo .env
   ```bash
      FILE_NAME=caminho/para/o/seu/credentials.json
      OPENAI_API_KEY=sua_api_key
      BASE_URL=sua base_url
      MODEL=seu modelo de llm

### 4. Executar projeto
```bash 
   python main.py

