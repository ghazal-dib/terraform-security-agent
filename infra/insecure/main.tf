terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "eu-central-1"
}

# Misconfigured on purpose: public ACL, no encryption, no versioning, no logging
resource "aws_s3_bucket" "data" {
  bucket = "insecure-demo-data-bucket-12345"
}

resource "aws_s3_bucket_acl" "data" {
  bucket = aws_s3_bucket.data.id
  acl    = "public-read"
}

# Misconfigured on purpose: SSH and all ports open to the whole internet
resource "aws_security_group" "web" {
  name        = "insecure-web-sg"
  description = "Open to the world"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Misconfigured on purpose: wildcard IAM permissions
resource "aws_iam_policy" "admin_all" {
  name = "insecure-admin-all"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "*"
      Resource = "*"
    }]
  })
}