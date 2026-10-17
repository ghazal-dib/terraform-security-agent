# Terraform Security Review Agent

An AI agent that reviews Terraform code for AWS security misconfigurations before deployment.

It runs Checkov and Trivy, merges and deduplicates their findings, judges real-world severity, explains each issue in plain language, maps it to CIS AWS Foundations Benchmark and Saudi NCA controls, and proposes corrected code.

## Status
In progress.

## Structure
- `infra/secure/` - securely configured test infrastructure
- `infra/insecure/` - deliberately misconfigured test infrastructure
- `agent/` - the review agent
- `mappings/` - compliance control data
- `reports/` - generated reports
