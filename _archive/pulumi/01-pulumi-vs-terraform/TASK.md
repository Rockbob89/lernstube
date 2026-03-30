# Task 01: Pulumi vs Terraform

## Objective
Understand the fundamental differences between Pulumi and Terraform, and articulate when to choose one over the other.

## What to Learn
- Pulumi's approach: real programming languages (Python, Go, TypeScript) vs HCL
  ```python
  # Pulumi — Python loop to create multiple buckets
  for i in range(3):
      s3.Bucket(f"bucket-{i}")
  # Terraform requires count or for_each in HCL — less expressive
  ```
- State management: Pulumi Service backend vs S3/GCS/Consul for Terraform
- Provider ecosystem: Pulumi wraps Terraform providers via Pulumi Bridge
- Key differences: loops, conditionals, testing, IDE support, typing
- When Terraform wins: mature ecosystem, large community, HCL simplicity for platform teams
- When Pulumi wins: complex logic, existing dev teams, testing, type safety

## Exercises

1. **Comparison matrix**: Create a markdown table comparing Pulumi and Terraform across these dimensions: language support, state management, secret handling, testing, provider ecosystem, learning curve, CI/CD integration. Write it to `comparison.md`.

2. **Decision framework**: Write a function that takes a dict of project requirements and returns a recommendation. Requirements include: `team_lang` (primary team language), `infra_complexity` (low/medium/high), `existing_iac` (none/terraform/cloudformation), `testing_priority` (low/medium/high).

3. **State backends**: Write a function that returns the available state backend options for both tools, with pros/cons for each.
