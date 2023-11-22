terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.26.0"
    }
  }
}

provider "aws" {
  # Configuration options
  profile = "poc" ## change the profile value accordingly
  region = "us-east-1"
}