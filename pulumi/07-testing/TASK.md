# Task 07: Testing

## Objective
Write unit tests, property tests, and integration tests for Pulumi programs.

## What to Learn
- Unit tests with mocks: `pulumi.runtime.set_mocks()`
  ```python
  class MyMocks(pulumi.runtime.Mocks):
      def new_resource(self, args):
          return [args.name + "_id", args.inputs]
      def call(self, args):
          return {}
  pulumi.runtime.set_mocks(MyMocks())
  ```
- Testing resource creation, outputs, and dependencies
- Property tests: validating resource properties (e.g., no public S3 buckets)
  ```python
  @pulumi.runtime.test
  def test_no_public_bucket():
      def check(args):
          acl, = args
          assert acl != "public-read", "Bucket must not be public"
      return pulumi.Output.all(bucket.acl).apply(check)
  ```
- Integration tests: `pulumi test` and actual deployment verification
- Policy as Code with `pulumi policy`
- Test patterns: what to test vs what not to test in IaC

## Exercises

1. **Mock framework**: Build a simplified mock framework that intercepts "resource creation" calls and records what was created. Use this to verify that a function creates the expected resources with correct properties.

2. **Policy checker**: Write a policy checker that validates a list of resource definitions against rules: no public S3 buckets, all EC2 instances must have tags, RDS must have encryption enabled, EBS volumes must be encrypted.

3. **Test reporter**: Write a function that takes test results (pass/fail/skip with resource names and rule names) and produces a structured report with summary stats.
