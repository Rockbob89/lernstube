# Task 08: Capstone — Multi-Cloud Deploy

## Objective
Deploy a small application across two clouds (or cloud + Kubernetes) using Pulumi with Python. Demonstrate everything learned: project structure, components, stack references, config, testing, and multi-provider setup.

## What to Build
A simple web application with:
- **AWS**: S3 bucket for static assets + CloudFront distribution
- **GCP (or K8s)**: Cloud Run service (or K8s Deployment) for the API backend
- **Shared**: DNS records pointing to both, config-driven per environment

## Requirements
1. Multi-stack architecture: networking, compute, app (at least 2 stacks)
2. At least one `ComponentResource`
3. Cross-stack references between stacks
4. Per-environment config (dev/prod) with secrets
5. Policy checks: no public buckets, encryption required, tags required
6. Unit tests for at least one component
7. A `README.md` explaining the architecture and how to deploy

## Deliverables
- Working Pulumi project directory with `__main__.py`, components, tests
- Architecture diagram (text-based is fine)
- Deployment instructions

## Evaluation Criteria
- Clean separation of concerns across stacks
- Proper use of ComponentResource for reusable abstractions
- Config/secrets management done correctly
- Tests actually test meaningful properties
- Code is production-quality: typed, documented, no hardcoded values
