📊 Graylog Stack com Docker

Este projeto implementa uma plataforma completa de centralização de logs utilizando o Graylog, com suporte a ingestão via Syslog, GELF e Beats, permitindo monitoramento, análise e correlação de eventos em um ambiente centralizado.

---

- Graylog 5.2
- MongoDB 5.0
- OpenSearch 2.11
- Docker & Docker Compose

---

## 🏗️ Arquitetura

- **MongoDB** → Armazena configurações e metadados  
- **OpenSearch** → Responsável pela indexação e busca  
- **Graylog** → Interface web, processamento e análise de logs  

---

## 📦 Estrutura do Projeto

---

├── docker-compose.yml
└── README.md

---

⚙️ Configuração

Antes de subir o ambiente, configure as variáveis de segurança:

🔐 Gerar senha secreta
pwgen -N 1 -s 96
🔑 Gerar hash da senha do admin
echo -n "SuaSenha" | sha256sum

---

📝 Configurar no docker-compose.yml
GRAYLOG_PASSWORD_SECRET=Sua_senha_aqui
GRAYLOG_ROOT_PASSWORD_SHA2=Sua_Hash_senha_aqui

---

▶️ Como executar
docker-compose up -d

---

🌐 Acesso
Interface Web: http://localhost:9000
Usuário: admin
Senha: definida no hash configurado

---

📡 Portas expostas
Porta	Função
9000	Interface Web
1514/udp	Syslog
12201/udp	GELF
5044	Beats

---

📊 Funcionalidades
Centralização de logs
Criação de dashboards
Filtros e buscas avançadas
Criação de alertas (triggers)
Monitoramento em tempo real
