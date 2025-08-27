# Chatbot-Application-using-Langchain

A simple chatbot application built using LangChain and Streamlit.  
It supports both:  
- Paid LLMs (OpenAI GPT-3.5 Turbo)  
- Open Source Local LLMs (Ollama with Llama 3.2)  

------------------------------------------------------------

🚀 Features
- Chat with OpenAI GPT models (requires API key).  
- Chat with Ollama local models (no API cost).  
- Simple UI with Streamlit.  
- Easy switch between OpenAI and Ollama.  

------------------------------------------------------------

🛠️ Tech Stack
- LangChain – for LLM orchestration  
- Streamlit – for chatbot UI  
- OpenAI GPT-3.5 Turbo – cloud-based LLM  
- Ollama (Llama 3.2) – local LLM  

------------------------------------------------------------

⚙️ Setup

1. Clone the Repository
   git clone https://github.com/YagamiLi45/Chatbot-Application-using-Langchain.git
   cd Chatbot-Application-using-Langchain
2. Create Virtual Environment (create_venv.txt)

3. Install Dependencies
   pip install -r requirements.txt

------------------------------------------------------------

▶️ Running with OpenAI (Paid LLM)

1. Get an OpenAI API Key → https://platform.openai.com/
   
2. Run the app:
   streamlit run app.py

Note: If you see "Error 429 (Rate Limit)", it means your API quota is exceeded.  

------------------------------------------------------------

▶️ Running with Ollama (Open Source LLM)

1. Install Ollama → https://ollama.ai/  
2. Check if Ollama is running by opening:
   http://localhost:11434/

3. Pull the model:
   ollama pull llama3.2

4. Run the app:
   streamlit run app.py

Now the chatbot will use Llama 3.2 locally 🎉  
