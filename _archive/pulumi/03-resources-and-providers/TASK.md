# Task 03: Resources & Providers

## Objective
Understand how Pulumi models cloud resources, how providers work, and how resource options control behavior.

## What to Learn
- Resource classes: `pulumi_aws.s3.Bucket`, `pulumi_gcp.storage.Bucket`, etc.
  ```python
  import pulumi_aws as aws
  bucket = aws.s3.Bucket("my-bucket", acl="private")
  ```
- Custom vs managed resources
- Provider configuration: default vs explicit providers, multi-region
  ```python
  west = aws.Provider("west", region="us-west-2")
  bucket = aws.s3.Bucket("west-bucket", opts=pulumi.ResourceOptions(provider=west))
  ```
- Resource options: `depends_on`, `protect`, `ignore_changes`, `delete_before_replace`, `aliases`, `parent`
  ```python
  aws.s3.Bucket("safe-bucket", opts=pulumi.ResourceOptions(
      protect=True, depends_on=[vpc], ignore_changes=["tags"]
  ))
  ```
- Resource transformations

## Exercises

1. **Resource registry**: Write a function that models a resource registry — given a list of resource definitions (name, type, depends_on), validate that all dependency targets exist and return a dependency graph as an adjacency list.

2. **Resource options builder**: Write a builder function that takes keyword args for common resource options and returns a validated options dict. It should enforce rules like: `protect=True` requires `delete_before_replace=False`.

3. **Multi-provider config**: Write a function that generates provider configurations for deploying to multiple AWS regions. Given a list of regions, return a dict mapping region to provider config.
