# Documentação da Infraestrutura CloudFit

Este diretório contém os arquivos de configuração do Terraform para provisionar a infraestrutura necessária para a aplicação CloudFit.

## Primeiros Passos

Para implantar a infraestrutura, certifique-se de que o Terraform está instalado em sua máquina. Você pode baixá-lo no [site oficial do Terraform](https://www.terraform.io/downloads.html).

### Pré-requisitos

- Terraform instalado
- Conta AWS com permissões apropriadas

### Instruções de Implantação

1. **Clone o repositório**:
   ```
   git clone https://github.com/cloudfit-devops/cloudfit-devops.git
   cd cloudfit-devops/infra/terraform
   ```

2. **Inicialize o Terraform**:
   ```
   terraform init
   ```

3. **Planeje a implantação**:
   ```
   terraform plan
   ```

4. **Aplique a configuração**:
   ```
   terraform apply
   ```

5. **Acesse os outputs**:
   Após a conclusão da implantação, você pode visualizar as saídas (como o IP público da instância EC2) executando:
   ```
   terraform output
   ```

### Comandos Terraform

- `terraform init`: Inicializa a configuração do Terraform.
- `terraform plan`: Cria um plano de execução, mostrando quais ações o Terraform realizará.
- `terraform apply`: Aplica as alterações necessárias para atingir o estado desejado da configuração.
- `terraform destroy`: Destroi a infraestrutura gerenciada pelo Terraform.

Para mais informações detalhadas sobre os comandos do Terraform, consulte a [documentação do Terraform](https://www.terraform.io/docs).