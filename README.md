# WeatherSearchAI
LangChain ReAct agent using Groq's LLaMA3 to answer questions with DuckDuckGo search and real-time weather data.

---

### 📄 `README.md`

````markdown
# 🧠 ReAct Agent with Groq, Weather API & Search

This project implements a LangChain ReAct agent powered by Groq's LLaMA3 model. It combines real-time DuckDuckGo search and live weather data via the WeatherStack API. You can run it as a Python CLI or via a Streamlit web app.

---

## 🔧 Features

- 🌐 DuckDuckGo search tool for real-time information
- ☁️ WeatherStack API integration for current weather data
- 🧠 LLaMA3-70B via Groq for reasoning & response generation
- ⚡ Streamlit frontend + CLI interface
- 🔁 ReAct prompt style via LangChain Hub

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/react-agent-weather-search.git
cd react-agent-weather-search
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up `.env` file

```env
OPENAI_API_KEY=your_groq_api_key
```

> Note: You may hardcode the key directly inside the script (not recommended for production).

---

## ▶️ Run via CLI

```bash
python main.py
```

---

## 🖥️ Run via Streamlit

```bash
streamlit run streamlit_app.py
```

---

## 🧪 Tools Used

* LangChain Agents (ReAct pattern)
* Groq’s LLaMA3-70B model
* DuckDuckGo Search (via langchain\_community)
* WeatherStack API
* Streamlit
* Python 3.10+

---

## 📌 Example Query

> "Find the capital of Madhya Pradesh, then find its current weather condition."

