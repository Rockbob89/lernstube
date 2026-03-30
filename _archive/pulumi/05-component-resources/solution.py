"""Component Resources — reusable infrastructure abstractions."""


class ComponentResource:
    """Simulated Pulumi ComponentResource base class.

    Example:
        >>> class MyBucket(ComponentResource):
        ...     def __init__(self, name):
        ...         super().__init__("custom:MyBucket", name)
        ...         self.register_outputs({"bucket_name": name})
    """

    def __init__(self, type_name: str, name: str, parent=None):
        pass

    def register_outputs(self, outputs: dict):
        pass

    @property
    def urn(self) -> str:
        pass

    def add_child(self, child: "ComponentResource"):
        pass


class VpcComponent(ComponentResource):
    """Simulated VPC component encapsulating VPC, subnets, NAT gateway.

    Example:
        >>> vpc = VpcComponent("main-vpc", cidr="10.0.0.0/16", az_count=2)
        >>> print(vpc.outputs["vpc_id"])
        >>> print(vpc.outputs["public_subnet_ids"])
    """

    def __init__(self, name: str, cidr: str, az_count: int = 2):
        pass


class EksComponent(ComponentResource):
    """Simulated EKS cluster component.

    Example:
        >>> eks = EksComponent("main-cluster", vpc_id="vpc-123",
        ...                     subnet_ids=["subnet-1", "subnet-2"])
        >>> print(eks.outputs["cluster_endpoint"])
    """

    def __init__(self, name: str, vpc_id: str, subnet_ids: list[str]):
        pass


class AppStack(ComponentResource):
    """Composed component combining VPC + EKS.

    Example:
        >>> app = AppStack("my-app", cidr="10.0.0.0/16")
        >>> print(app.outputs["cluster_endpoint"])
        >>> print(app.outputs["vpc_id"])
    """

    def __init__(self, name: str, cidr: str):
        pass


if __name__ == "__main__":
    vpc = VpcComponent("prod-vpc", cidr="10.0.0.0/16", az_count=3)
    print("VPC URN:", vpc.urn)
    print("VPC outputs:", vpc.outputs)
    print()
    app = AppStack("prod-app", cidr="10.0.0.0/16")
    print("AppStack URN:", app.urn)
    print("AppStack outputs:", app.outputs)
