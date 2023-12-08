# Sistema de Agendamento de horário para Salão de Beleza

Este é um projeto de sistema web desenvolvido em Django para gerenciar o agendamento de serviços em um salão de beleza. O sistema permite que clientes realizem agendamentos online e inclui uma integração com o WhatsApp através de chatbot para facilitar o processo.

## Configuração do Ambiente

1. **Pré-requisitos:**
   - Python 3.x
   - Django
   - Outras dependências (verifique o arquivo `requirements.txt`)

2. **Configuração do Ambiente Virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: .\venv\Scripts\activate

3. **Instalação das Dependências:**
    ````bash
   pip install -r requirements.txt
   
4. **Configuração do Banco de Dados:**
    ````bash
   python manage.py makemigrations
   python manage.py migrate
5. **Execução do Servidor de Desenvolvimento:**
    ````bash
   python manage.py runserver

### Funcionalidades Principais
- Agendamento de horários pelo cliente.
- Integração com o WhatsApp via chatbot para agendamento de horário.
- Programa de fidelidade com descontos baseados no histórico de agendamentos.