# Projeto CloudFit DevOps

## Visão Geral
CloudFit é uma startup focada em monitoramento de atividades físicas em tempo real. Este projeto envolve o desenvolvimento de uma API REST que permite aos usuários acompanhar suas atividades físicas e monitorar seu progresso. O projeto está estruturado em dois principais componentes: a API e o provisionamento de infraestrutura.

## Objetivos
- Desenvolver uma API REST usando Flask para monitoramento de atividades físicas.
- Provisionar infraestrutura utilizando Terraform para hospedar a API.
- Configurar um pipeline de CI/CD usando GitHub Actions para testes automatizados e deploy.

## Estrutura do Projeto
```
cloudfit-devops
├── api                  # Contém o código da API
│   ├── src             # Código-fonte da API
│   ├── requirements.txt # Dependências Python
│   └── README.md       # Documentação da API
├── infra                # Infraestrutura como código
│   ├── terraform        # Configurações do Terraform
│   └── README.md       # Documentação da infraestrutura
├── .github              # Workflows do GitHub
│   └── workflows
│       └── ci-cd.yml   # Configuração do pipeline CI/CD
├── .gitignore           # Arquivos ignorados pelo Git
└── README.md            # Visão geral e documentação do projeto
```

## Instruções para Configuração Local
1. **Clone o repositório:**
  ```
  git clone https://github.com/larissa-collossi/cloudfit-devops.git
  cd cloudfit-devops
  ```

2. **Configure a API:**
  - Navegue até o diretório `api`.
  - Instale as dependências necessárias:
    ```
    pip install -r requirements.txt
    ```
  - Execute a aplicação:
    ```
    python src/app.py
    ```

3. **Provisione a Infraestrutura:**
  - Navegue até o diretório `infra/terraform`.
  - Inicialize o Terraform:
    ```
    terraform init
    ```
  - Aplique a configuração do Terraform:
    ```
    terraform apply
    ```

4. **Configuração do CI/CD:**
  - O pipeline de CI/CD está configurado no arquivo `.github/workflows/ci-cd.yml`. Ele executa automaticamente os testes e faz o deploy da aplicação ao realizar push na branch principal.

## Configuração de Variáveis Sensíveis

Para provisionar a infraestrutura AWS e realizar o deploy via CI/CD, é necessário configurar as seguintes variáveis de ambiente no repositório (em **Settings > Secrets and variables > Actions**):

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_SESSION_TOKEN`
- `EC2_SSH_KEY`

Essas variáveis devem ser adicionadas como **secrets** para garantir a segurança das credenciais e do acesso SSH à instância EC2.

## Detalhes da Infraestrutura
A infraestrutura é provisionada usando Terraform, incluindo uma instância EC2 e um grupo de segurança permitindo tráfego HTTP na porta 80.

## Explicação do Workflow de CI/CD
O pipeline de CI/CD automatiza o processo de teste e deploy da aplicação. Inclui etapas para instalar dependências, executar testes e fazer o deploy para a infraestrutura provisionada.

## Contribuindo
Contribuições são bem-vindas! Por favor, envie um pull request ou abra uma issue para sugestões ou melhorias.
