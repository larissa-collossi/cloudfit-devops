# CloudFit DevOps Project

## Overview
CloudFit is a startup focused on real-time fitness activity monitoring. This project involves developing a REST API that allows users to track their fitness activities and monitor their progress. The project is structured into two main components: the API and the infrastructure provisioning.

## Objectives
- Develop a REST API using Flask for fitness activity monitoring.
- Provision infrastructure using Terraform to host the API.
- Set up a CI/CD pipeline using GitHub Actions for automated testing and deployment.

## Project Structure
```
cloudfit-devops
├── api                  # Contains the API code
│   ├── src             # Source code for the API
│   ├── requirements.txt # Python dependencies
│   └── README.md       # API documentation
├── infra                # Infrastructure as code
│   ├── terraform        # Terraform configurations
│   └── README.md       # Infrastructure documentation
├── .github              # GitHub workflows
│   └── workflows
│       └── ci-cd.yml   # CI/CD pipeline configuration
├── .gitignore           # Files to ignore in Git
└── README.md            # Project overview and documentation
```

## Local Setup Instructions
1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd cloudfit-devops
   ```

2. **Set up the API:**
   - Navigate to the `api` directory.
   - Install the required dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Run the application:
     ```
     python src/app.py
     ```

3. **Provision Infrastructure:**
   - Navigate to the `infra/terraform` directory.
   - Initialize Terraform:
     ```
     terraform init
     ```
   - Apply the Terraform configuration:
     ```
     terraform apply
     ```

4. **CI/CD Setup:**
   - The CI/CD pipeline is configured in the `.github/workflows/ci-cd.yml` file. It will automatically run tests and deploy the application on push to the main branch.

## Infrastructure Details
The infrastructure is provisioned using Terraform, which includes an EC2 instance and a security group allowing HTTP traffic on port 80.

## CI/CD Workflow Explanation
The CI/CD pipeline automates the process of testing and deploying the application. It includes steps for installing dependencies, running tests, and deploying the application to the provisioned infrastructure.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.