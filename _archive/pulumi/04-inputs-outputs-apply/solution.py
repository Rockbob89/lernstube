"""Inputs, Outputs & Apply — simulating Pulumi's async model."""

from typing import Any, Callable, TypeVar

T = TypeVar("T")


class Output:
    """Simplified Pulumi Output simulator.

    Example:
        >>> out = Output("vpc-123")
        >>> result = out.apply(lambda v: f"subnet-of-{v}")
        >>> print(result.value)
        subnet-of-vpc-123
    """

    def __init__(self, value: Any):
        pass

    def apply(self, func: Callable) -> "Output":
        """Transform the wrapped value.

        Example:
            >>> Output(5).apply(lambda x: x * 2).value
            10
        """
        pass

    @classmethod
    def all(cls, *outputs: "Output") -> "Output":
        """Combine multiple Outputs into one Output containing a tuple.

        Example:
            >>> combined = Output.all(Output("a"), Output("b"))
            >>> print(combined.value)
            ('a', 'b')
        """
        pass

    def __repr__(self):
        pass


def concat(*parts) -> Output:
    """Concatenate Output values and plain strings into a single Output.

    Args:
        *parts: mix of Output instances and plain strings

    Returns:
        Output wrapping the concatenated string

    Example:
        >>> result = concat("https://", Output("my-bucket"), ".s3.amazonaws.com")
        >>> print(result.value)
        https://my-bucket.s3.amazonaws.com
    """
    pass


def wire_resources():
    """Demonstrate wiring outputs between simulated resources.

    Create:
    - A VPC with an id output
    - A subnet that uses the VPC id
    - A connection string that combines multiple outputs

    Returns:
        dict with keys: vpc_id, subnet_id, connection_string (all Output instances)

    Example:
        >>> resources = wire_resources()
        >>> print(resources["connection_string"].value)
    """
    pass


if __name__ == "__main__":
    out = Output("vpc-abc123")
    print("Apply:", out.apply(lambda v: v.upper()))
    print("All:", Output.all(Output("a"), Output("b"), Output("c")))
    print("Concat:", concat("arn:aws:s3:::", Output("my-bucket"), "/*"))
    print()
    resources = wire_resources()
    for k, v in resources.items():
        print(f"  {k}: {v}")
