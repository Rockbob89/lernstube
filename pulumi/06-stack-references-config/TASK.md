# Task 06: Stack References & Config

## Objective
Design multi-stack architectures with cross-stack references and per-stack configuration management.

## What to Learn
- `StackReference` — reading outputs from another stack
  ```python
  net = pulumi.StackReference("org/networking/dev")
  vpc_id = net.get_output("vpc_id")  # Output[str] from another stack
  ```
- Multi-stack patterns: networking/compute/app separation
- `pulumi.Config` — typed config access
  ```python
  cfg = pulumi.Config()
  region = cfg.require("region")         # str, raises if missing
  count = cfg.get_int("replica_count", 2) # int with default
  token = cfg.require_secret("api_token") # Output[str], decrypted at runtime
  ```
- Config namespacing: `pulumi config set aws:region us-east-1`
- Environment-specific overrides
- When to split stacks vs keep monolithic

## Exercises

1. **Stack reference simulator**: Build a `StackReference` class that can "export" outputs from one stack and "import" them in another. Simulate two stacks: a networking stack that exports VPC/subnet IDs, and a compute stack that consumes them.

2. **Config manager**: Write a `ConfigManager` class that loads config from a dict (simulating `Pulumi.<stack>.yaml`), supports namespaced keys (`aws:region`), typed access (get_int, get_bool, get_secret), and defaults.

3. **Stack splitting advisor**: Write a function that takes a list of resource definitions with their change frequency and blast radius, and recommends how to split them across stacks.
