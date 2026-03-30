# Task 04: Inputs, Outputs & Apply

## Objective
Master Pulumi's asynchronous resource model — `Output[T]`, `apply()`, `concat()`, and how values flow between resources.

## What to Learn
- Why outputs exist: resources aren't created until `pulumi up`, so values are promises
- `Output[T]` — wraps a future value
- `apply(lambda v: ...)` — transform an output's value
  ```python
  bucket = aws.s3.Bucket("b")
  # bucket.id is Output[str] — unknown until deployed
  url = bucket.id.apply(lambda id: f"https://{id}.s3.amazonaws.com")
  ```
- `pulumi.Output.concat()` — string interpolation with outputs
  ```python
  url = pulumi.Output.concat("https://", bucket.id, ".s3.amazonaws.com")
  ```
- `pulumi.Output.all()` — combine multiple outputs
  ```python
  pulumi.Output.all(bucket.id, role.arn).apply(lambda vals: f"{vals[0]} / {vals[1]}")
  ```
- Lifting: accessing properties on outputs directly
- Common pitfall: trying to use `.apply()` result outside Pulumi's engine

## Exercises

1. **Output simulator**: Build a simple `Output` class that wraps a value and supports `apply()` chaining and an `all()` class method. This helps internalize the pattern without needing the Pulumi SDK.

2. **Resource wiring**: Given a simulated VPC ID output and subnet CIDR, write functions that demonstrate wiring outputs between resources using your Output simulator.

3. **Output concat**: Implement a `concat` function that joins multiple Output values (and plain strings) into a single Output string.
