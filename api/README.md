# Documentação da API CloudFit

## Visão Geral
CloudFit é um aplicativo de monitoramento de atividades físicas em tempo real que fornece uma API REST para rastreamento de atividades. Esta API é construída com Flask e serve como backend para a plataforma CloudFit.

## Instruções de Configuração

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação
1. Clone o repositório:
   ```
   git clone https://github.com/larissa-collossi/cloudfit-devops.git
   cd cloudfit-devops/api
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências necessárias:
   ```
   pip install -r requirements.txt
   ```

## Executando a Aplicação
Para executar a aplicação Flask, utilize o seguinte comando:
```
python src/app.py
```
A aplicação será iniciada em `http://localhost:5000`.

## Endpoints da API

### GET /status
- **Descrição**: Retorna o status da API.
- **Resposta**:
  ```json
  {
    "status": "ok"
  }
  ```
## Testes
Os testes ainda estão em desenvolvimento. Em breve, instruções detalhadas serão disponibilizadas nesta seção.

## Contribuindo
Contribuições são bem-vindas! Envie um pull request ou abra uma issue para melhorias ou correções de bugs.

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.