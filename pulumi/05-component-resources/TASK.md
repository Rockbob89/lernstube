# Task 05: Component Resources

## Objective
Build reusable infrastructure abstractions using Pulumi's `ComponentResource` pattern.

## What to Learn
- `ComponentResource` vs plain resources
- Parent-child resource relationships
- Encapsulating related resources into a single logical unit
  ```python
  class VpcComponent(pulumi.ComponentResource):
      def __init__(self, name, opts=None):
          super().__init__("custom:network:Vpc", name, {}, opts)
          self.vpc = aws.ec2.Vpc("vpc", cidr_block="10.0.0.0/16",
                                  opts=pulumi.ResourceOptions(parent=self))
          self.register_outputs({"vpc_id": self.vpc.id})
  ```
- Exposing outputs from components
- `register_outputs()` — why and when to use it
- Composing components

## Exercises

1. **Component skeleton**: Build a simulated `ComponentResource` base class that tracks child resources, supports `register_outputs()`, and provides a `urn` property. No Pulumi SDK needed — just model the pattern.

2. **VPC component**: Using your base class, create a `VpcComponent` that encapsulates a VPC, public/private subnets, and a NAT gateway as child resources. Expose the VPC ID and subnet IDs as outputs.

3. **Component composition**: Create an `AppStack` component that composes your `VpcComponent` with an EKS-like cluster component. Demonstrate how outputs flow between composed components.
