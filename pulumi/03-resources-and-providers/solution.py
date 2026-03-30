"""Resources & Providers — modeling cloud resources and provider config."""


def build_dependency_graph(resources: list[dict]) -> dict:
    """Build a dependency graph from resource definitions.

    Args:
        resources: list of dicts with keys:
            - name: str
            - type: str (e.g. "aws:s3:Bucket")
            - depends_on: list[str] (resource names)

    Returns:
        dict: adjacency list {resource_name: [dependent_names]}

    Example:
        >>> graph = build_dependency_graph([
        ...     {"name": "vpc", "type": "aws:ec2:Vpc", "depends_on": []},
        ...     {"name": "subnet", "type": "aws:ec2:Subnet", "depends_on": ["vpc"]},
        ...     {"name": "instance", "type": "aws:ec2:Instance", "depends_on": ["subnet"]},
        ... ])
        >>> assert graph["vpc"] == ["subnet"]
    """
    pass


def build_resource_options(**kwargs) -> dict:
    """Build and validate Pulumi resource options.

    Supported kwargs: protect, delete_before_replace, ignore_changes,
                      depends_on, parent, aliases, retain_on_delete

    Raises:
        ValueError: if protect=True and delete_before_replace=True

    Example:
        >>> opts = build_resource_options(protect=True, ignore_changes=["tags"])
        >>> assert opts["protect"] is True
        >>> assert opts["delete_before_replace"] is False
    """
    pass


def multi_region_providers(regions: list[str], base_config: dict) -> dict:
    """Generate provider configs for multiple AWS regions.

    Args:
        regions: list of AWS region strings
        base_config: shared config (profile, etc.)

    Returns:
        dict: {region: {provider_config}}

    Example:
        >>> providers = multi_region_providers(
        ...     ["us-east-1", "eu-west-1"],
        ...     {"profile": "prod"}
        ... )
        >>> assert providers["us-east-1"]["region"] == "us-east-1"
    """
    pass


if __name__ == "__main__":
    resources = [
        {"name": "vpc", "type": "aws:ec2:Vpc", "depends_on": []},
        {"name": "subnet", "type": "aws:ec2:Subnet", "depends_on": ["vpc"]},
        {"name": "sg", "type": "aws:ec2:SecurityGroup", "depends_on": ["vpc"]},
        {"name": "instance", "type": "aws:ec2:Instance", "depends_on": ["subnet", "sg"]},
    ]
    print("Dependency graph:", build_dependency_graph(resources))
    print()
    print("Resource options:", build_resource_options(protect=True, ignore_changes=["tags"]))
    print()
    print("Providers:", multi_region_providers(["us-east-1", "eu-west-1"], {"profile": "prod"}))
