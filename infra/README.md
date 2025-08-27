# CloudFit Infrastructure Documentation

This directory contains the Terraform configuration files for provisioning the infrastructure required for the CloudFit application.

## Getting Started

To deploy the infrastructure, ensure you have Terraform installed on your machine. You can download it from [Terraform's official website](https://www.terraform.io/downloads.html).

### Prerequisites

- Terraform installed
- AWS account with appropriate permissions

### Deployment Instructions

1. **Clone the repository**:
   ```
   git clone https://github.com/yourusername/cloudfit-devops.git
   cd cloudfit-devops/infra/terraform
   ```

2. **Initialize Terraform**:
   ```
   terraform init
   ```

3. **Plan the deployment**:
   ```
   terraform plan
   ```

4. **Apply the configuration**:
   ```
   terraform apply
   ```

5. **Access the outputs**:
   After the deployment is complete, you can view the outputs (like the public IP of the EC2 instance) by running:
   ```
   terraform output
   ```

### Terraform Commands

- `terraform init`: Initializes the Terraform configuration.
- `terraform plan`: Creates an execution plan, showing what actions Terraform will take.
- `terraform apply`: Applies the changes required to reach the desired state of the configuration.
- `terraform destroy`: Destroys the infrastructure managed by Terraform.

For more detailed information on Terraform commands, refer to the [Terraform documentation](https://www.terraform.io/docs).