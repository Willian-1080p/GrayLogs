# 🤖 Graylog + LLM

Este projeto estende o Graylog com integração a um LLM (Large Language Model), permitindo análise inteligente de logs, identificação automática de padrões suspeitos e apoio na investigação de incidentes de segurança.

---


Instalar o LLaMA docker 
exec -it ollama ollama run llama3

---

- 🔐 Falhas de autenticação
- ⚠️ Atividades anômalas
- 🕵️ Comportamentos suspeitos

---

## 🧠 Funcionalidades do LLM

- Interpretação de logs em linguagem natural  
- Classificação automática de eventos  
- Geração de insights de segurança  
- Apoio na investigação de incidentes  
- Contextualização de eventos (ex: possível brute force)

---

## 🏗️ Arquitetura

---

Winlogbeat → Graylog → Script Python → LLM → Resposta/Análise

---

🔄 Fluxo de funcionamento
Logs são coletados via Winlogbeat
Enviados para o Graylog
Script em Python consulta eventos relevantes
Dados são enviados para o LLM
O modelo retorna uma análise interpretada

---

⚙️ Tecnologias
Graylog
Python
API de LLM
Winlogbeat
OpenSearch

---

▶️ Funcionamento

O sistema realiza consultas baseadas em eventos críticos, como:

failed login
authentication error
suspicious activity

O LLM interpreta os dados e retorna um diagnóstico em linguagem natural.

---

📌 Exemplo de uso

🔍 Consulta
failed login

🤖 Resposta do LLM
Múltiplas tentativas de login falharam em curto período de tempo. 
Isso pode indicar um possível ataque de força bruta.

---

📊 Casos de uso
Detecção de ataques de força bruta
Análise automatizada de logs
Apoio a analistas SOC
Redução de tempo de investigação
Triagem inteligente de eventos

---

🔐 Segurança

Boas práticas aplicadas:

🔑 Não expor API Keys
📦 Uso de variáveis de ambiente (.env)
🧼 Sanitização de dados antes do envio ao LLM
🚫 Controle de acesso às APIs
📊 Limitação de requisições (rate limit)

---

🚧 Status do Projeto

⚠️ Em desenvolvimento e fase de testes

Este projeto ainda não está completo e encontra-se em evolução contínua.
Algumas funcionalidades podem estar instáveis ou em validação.

---

🚀 Melhorias futuras
🔔 Geração automática de alertas com IA
📊 Dashboard com insights do LLM
🧠 Classificação automática de incidentes (ML/AI)
🔗 Integração completa com SIEM
📈 Correlação de eventos com contexto
