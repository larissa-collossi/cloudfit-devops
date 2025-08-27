# CloudFit Infrastructure Terraform Setup

This directory contains the Terraform configuration files for provisioning the infrastructure required for the CloudFit application.

## Prerequisites

- Ensure you have [Terraform](https://www.terraform.io/downloads.html) installed on your machine.
- Configure your AWS credentials to allow Terraform to provision resources.

## Directory Structure

- `main.tf`: Contains the main Terraform configuration for provisioning resources.
- `variables.tf`: Defines the variables used in the Terraform configuration.
- `outputs.tf`: Specifies the outputs of the Terraform configuration.

## Deployment Instructions

1. Navigate to the `terraform` directory:
   ```
   cd infra/terraform
   ```

2. Initialize Terraform:
   ```
   terraform init
   ```

3. Review the execution plan:
   ```
   terraform plan
   ```

4. Apply the configuration to provision the infrastructure:
   ```
   terraform apply
   ```

5. To destroy the infrastructure when no longer needed:
   ```
   terraform destroy
   ```

## Outputs

After a successful deployment, you will receive outputs such as the public IP of the EC2 instance, which can be used to access the CloudFit application.