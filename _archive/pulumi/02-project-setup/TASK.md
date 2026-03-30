# Task 02: Project Setup

## Objective
Set up a Pulumi project from scratch, understand project structure, stacks, configuration, and secrets management.

## What to Learn
- `pulumi new` templates and project scaffolding
- `Pulumi.yaml` and `Pulumi.<stack>.yaml` structure
  ```yaml
  # Pulumi.yaml
  name: lab-infra
  runtime: python
  description: Lab infrastructure

  # Pulumi.dev.yaml — per-stack overrides
  config:
    aws:region: us-east-1
    instance_type: t3.micro
  ```
- Stack concepts: dev/staging/prod
- Config and secrets: `pulumi config set`, `pulumi config set --secret`
  ```bash
  pulumi config set aws:region us-east-1
  pulumi config set --secret db_password s3cr3t  # encrypted in state
  ```
- Passphrase vs service-managed encryption

## Exercises

1. **Project init**: Run `pulumi new python -n lab-infra -s dev` in a fresh directory. Examine the generated files and write a function that parses `Pulumi.yaml` and returns project metadata.

2. **Multi-stack config**: Write a function that generates stack config dicts for dev/staging/prod with appropriate values (instance sizes, replica counts, feature flags). This simulates what you'd put in `Pulumi.<stack>.yaml`.

3. **Secrets handling**: Write a function that categorizes config keys into "plain" vs "secret" based on naming conventions and content patterns (e.g., keys containing `password`, `token`, `key`, `secret`).
