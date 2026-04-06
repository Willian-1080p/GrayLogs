# 🖥️ Winlogbeat + Graylog

Este projeto configura o **Winlogbeat** para coletar logs do Windows e enviá-los para o **Graylog**, permitindo centralização, análise e monitoramento de eventos.

---

## 🎯 Objetivo

Centralizar logs de máquinas Windows para:

- 🔍 Monitoramento de segurança
- 🚨 Detecção de incidentes
- 📊 Análise de eventos
- 🛡️ Auditoria de atividades

---

## ⚙️ Tecnologias

- Winlogbeat
- Graylog
- OpenSearch

---

## 📦 Logs coletados

Os seguintes logs do Windows são coletados:

- **Security** → Logins, falhas, autenticação
- **System** → Eventos do sistema operacional
- **Application** → Eventos de aplicações

---

## 🔧 Configuração

Arquivo: `winlogbeat.yml`

### Exemplo de configuração:


winlogbeat.event_logs:
  - name: Security

output.logstash:
  hosts: ["IP_DO_GRAYLOG:5044"]

---

  ▶️ Execução

Execute os comandos abaixo no PowerShell como administrador:

Test-NetConnection 192.168.15.234 -Port 5044

se TcpTestSucceeded : True

cd C:\Winlogbeat\winlogbeat-7.17.15-windows-x86_64 powershell.exe -ExecutionPolicy Bypass -File .\install-service-winlogbeat.ps1 Start-Service winlogbeat Get-Service winlogbeat

---

🔍 Verificação

No Graylog:

Criar um Input Beats na porta 5044
Verificar se os logs estão sendo recebidos
Buscar por eventos como:
failed login
error
security

---

📊 Casos de uso
Monitorar tentativas de login falhas
Detectar atividades suspeitas
Auditoria de eventos do sistema
Apoio em análise forense

---

🚨 Exemplos de eventos
Failed login
Alteração de usuário
Execução de processos
Tentativas de acesso não autorizado
🔐 Segurança

---

Boas práticas recomendadas:

🔒 Utilizar comunicação segura (TLS)
🚫 Restringir acesso ao servidor Graylog
📁 Monitorar integridade dos logs
🔑 Evitar exposição de dados sensíveis
