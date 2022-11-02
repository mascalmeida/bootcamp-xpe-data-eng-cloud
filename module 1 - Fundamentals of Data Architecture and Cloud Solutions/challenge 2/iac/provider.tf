# Define AWS as the cloud provider

provider "aws" {
  region = var.provider_region
}

# Centralized the Terraform control state file
terraform {
  backend "s3" {
    bucket = "terraform-state-md1-challenge2"
    key    = "state/terraform.tfstate"
    region = "us-east-1"
  }
}