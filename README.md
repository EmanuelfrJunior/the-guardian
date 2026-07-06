📡 Network Guardian

Sistema de monitoramento de rede desenvolvido em Python para coleta de métricas de conectividade, latência e disponibilidade de hosts.

🚀 Visão geral

O Network Guardian é um agente de monitoramento que roda continuamente em um servidor Linux e realiza testes de rede como:

Ping em múltiplos hosts
Medição de latência (ms)
Detecção de hosts online/offline
Execução contínua em loop (agente)
Estrutura preparada para integração com Grafana e bancos de dados de séries temporais
🧠 Objetivo do projeto

Este projeto foi criado com foco em aprendizado prático de:

Monitoramento de redes
Automação em Python
Estruturação de agentes de coleta
Boas práticas de arquitetura de software
Preparação para observabilidade (Grafana / InfluxDB)


🏗️ Arquitetura atual
network-guardian/
│
├── app/
│   ├── collectors/
│   │   └── ping.py          # Coleta de latência via ping
│   │
│   ├── scheduler/
│   │   └── scheduler.py     # Loop principal do agente
│   │
│   └── __init__.py
│
├── main.py                  # Entry point do agente
├── requirements.txt        # Dependências Python
├── .env                    # Variáveis de ambiente (não versionado)
├── .gitignore              # Arquivos ignorados pelo Git
└── README.md


⚙️ Funcionalidades implementadas

✅ Coleta de Ping
Testa conectividade com hosts
Retorna latência em milissegundos
Detecta status online/offline

✅ Estrutura de Agente
Loop contínuo (while True)
Execução automática a cada intervalo definido
Processamento de múltiplos hosts

✅ Organização modular
Separação por responsabilidades:
collectors
scheduler
main entrypoint

📦 Exemplo de saída
🚀 Network Guardian iniciado...

🟢 1.1.1.1 - 18.2 ms
🟢 8.8.8.8 - 19.1 ms
🟢 google.com - 21.0 ms
----------------------------------------
🟢 1.1.1.1 - 17.9 ms
🔴 192.168.0.1 - offline
🧰 Tecnologias utilizadas

Python 3.12
ping3
psutil (futuro uso)
python-dotenv
Git / GitHub
Linux (Ubuntu em Proxmox)
🧠 Conceitos aplicados
Estrutura de agentes (daemons simples)
Monitoramento de rede via ICMP
Programação modular em Python
Execução contínua (scheduler loop)
Boas práticas com .gitignore e .env
🚧 Próximos passos

O projeto está em evolução contínua. Próximas etapas:

 Persistência de dados (SQLite / InfluxDB)
 Exportação de métricas para Grafana
 Dashboard de monitoramento em tempo real
 Detecção de anomalias de rede
 Logs estruturados
 Execução como serviço (systemd)
 Integração com alertas (Telegram / Discord)
