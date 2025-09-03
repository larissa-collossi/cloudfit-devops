# Configuração de Infraestrutura CloudFit com Terraform

Este diretório contém os arquivos de configuração do Terraform para provisionar a infraestrutura necessária para a aplicação CloudFit.

## Pré-requisitos

- Certifique-se de ter o [Terraform](https://www.terraform.io/downloads.html) instalado em sua máquina.
- Configure suas credenciais AWS para permitir que o Terraform provisione recursos.

## Estrutura de Diretórios

- `main.tf`: Contém a configuração principal do Terraform para provisionamento dos recursos.
- `variables.tf`: Define as variáveis utilizadas na configuração do Terraform.
- `outputs.tf`: Especifica as saídas da configuração do Terraform.

## Instruções de Deploy

1. Navegue até o diretório `terraform`:
   ```
   cd infra/terraform
   ```

2. Inicialize o Terraform:
   ```
   terraform init
   ```

3. Revise o plano de execução:
   ```
   terraform plan
   ```

4. Aplique a configuração para provisionar a infraestrutura:
   ```
   terraform apply
   ```

5. Para destruir a infraestrutura quando não for mais necessária:
   ```
   terraform destroy
   ```

## Saídas

Após um deploy bem-sucedido, você receberá saídas como o IP público da instância EC2, que pode ser usado para acessar a aplicação CloudFit.