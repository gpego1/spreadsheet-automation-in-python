# Spreadsheet Automation in Python

This project is an advanced financial automation tool built with Python that analyzes budget and financial data stored in **Google Sheets**. The system automates everything from real-time spreadsheet reading to generating strategic reports powered by Artificial Intelligence.

---

## 🚀 How the Project Works

The script acts as a personal data analyst by following an automated workflow:

1. **Real-Time Connection**
   Uses the Google Sheets API to read financial data directly from the cloud.

2. **Data Processing**
   Uses the `pandas` library to structure, clean, and process spreadsheet data.

3. **Selective Extraction**
   Automatically generates a `data.csv` file containing only the essential information, such as employee names, income, expenses, and categories, optimizing the data sent for analysis.

4. **AI Analysis**
   The processed file is sent to an AI agent that performs a detailed analysis of income vs. expenses, identifies risks and financial issues, and suggests possible improvements based on real data.

5. **Strategic Feedback**
   The system returns a summarized and structured financial report to support decision-making.

---

## 📋 Prerequisites

Before running the project, make sure you have:

* Python 3.x installed
* A Google Cloud account to generate Google Sheets API credentials
* An OpenAI-compatible API key

---

## 🛠️ Setup Guide

### 1. Prepare the Spreadsheet

1. Download the example file `dados_financeiros.xlsx`
2. Open your **Google Drive**
3. Upload the `.xlsx` file and open it using **Google Sheets**
4. Click **Share** in the top-right corner
5. Add your Google Cloud **Service Account email** (found in the `client_email` field of your credentials JSON file) with **Editor** permissions

---

### 2. Clone the Repository

```bash
git clone https://github.com/gpego1/spreadsheet-automation-in-python.git
cd spreadsheet-automation-in-python
```

---

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

#### Activate the virtual environment

**Windows**

```bash
.\venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Configure Environment Variables

Create a `.env` file in the root directory of the project:

```env
FILE_NAME=path/to/your/credentials.json
OPENAI_API_KEY=your_api_key
BASE_URL=your_llm_base_url
MODEL=your_llm_model
```

---

## ▶️ Running the Project

Run the application with:

```bash
python main.py
```

---

## 📦 Technologies Used

* Python
* Pandas
* Google Sheets API
* OpenAI API
* dotenv

---

## 📄 Example Use Cases

* Financial spreadsheet automation
* AI-powered budget analysis
* Expense monitoring
* Automated reporting
* Business financial insights

---

Link for the SpreadSheet: https://docs.google.com/spreadsheets/d/14l7audhvE_kPdIpi2iUXNvxESGtpPyZbvNBZRGskUR4/edit?usp=sharing