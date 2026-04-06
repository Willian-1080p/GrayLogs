import requests
from requests.auth import HTTPBasicAuth

GRAYLOG_URL = "http://localhost:9000/api/search/universal/relative"
GRAYLOG_USER = "admin"
GRAYLOG_PASSWORD = "SUA_SENHA"

OLLAMA_URL = "http://localhost:11434/api/generate"

params = {
    "query": "failed login",
    "range": 300
}

response = requests.get(
    GRAYLOG_URL,
    params=params,
    auth=HTTPBasicAuth(GRAYLOG_USER, GRAYLOG_PASSWORD)
)

logs = response.json()

log_messages = ""
for msg in logs.get("messages", []):
    log_messages += str(msg["message"]) + "\n"

prompt = f"""
Você é um analista SOC.

Analise os logs abaixo e responda:
- Isso é suspeito?
- Tipo de ataque
- Recomendações

Logs:
{log_messages}
"""

llm_response = requests.post(OLLAMA_URL, json={
    "model": "llama3",
    "prompt": prompt,
    "stream": False
})

print("\n===== ANÁLISE =====\n")
print(llm_response.json()["response"])