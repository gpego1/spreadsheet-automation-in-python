# Spreadsheet Automation in Python

Este projeto é uma ferramenta de automação financeira que utiliza Python para analisar dados de orçamentos armazenados no **Google Sheets**. Ele processa transações financeiras, calcula médias, identifica gastos acima do esperado e automatiza a gestão orçamentária.

---

## 🚀 Como funciona o projeto
O script atua como um "analista de dados" pessoal:

1. **Conexão:** Utiliza a API do Google Sheets para ler seus dados financeiros em tempo real.
2. **Processamento:** Com a biblioteca `pandas`, o script converte os dados em uma tabela estruturada (*DataFrame*), tratando formatos de data e valores monetários.
3. **Análise:** Calcula a média de gastos e identifica automaticamente transações que fogem ao padrão (anomalias).
4. **Feedback:** O sistema alerta sobre desvios orçamentários, facilitando o controle financeiro.



---

## 📋 Pré-requisitos

Antes de rodar o código, certifique-se de ter:
* Python 3.x instalado.
* Uma conta no [Google Cloud Console](https://console.cloud.google.com/) para gerar suas credenciais de API.

---

## 🛠️ Passo a Passo para Configuração

### 1. Preparação da Planilha
1. Baixe o arquivo de exemplo `dados_financeiros.xlsx`.
2. Abra o seu **Google Drive**.
3. Faça o upload do arquivo `.xlsx` e abra-o com o **Google Planilhas (Google Sheets)**.
4. No canto superior direito, clique em **Compartilhar** e adicione o e-mail da sua "Conta de Serviço" (gerada no Google Cloud - encontrada no campo `client_email` do seu arquivo JSON) com permissão de **Editor**.

### 2. Configuração do Ambiente
1. Clone este repositório:
   ```bash
   git clone [https://github.com/gpego1/spreadsheet-automation-in-python.git](https://github.com/gpego1/spreadsheet-automation-in-python.git)
   cd spreadsheet-automation-in-python