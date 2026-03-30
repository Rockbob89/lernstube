"""Testing — unit tests, policy checks, and test infrastructure."""


class MockResourceMonitor:
    """Simplified mock for intercepting resource creation.

    Example:
        >>> monitor = MockResourceMonitor()
        >>> monitor.create_resource("aws:s3:Bucket", "my-bucket", {"acl": "private"})
        >>> monitor.create_resource("aws:ec2:Instance", "web-1", {"instance_type": "t3.micro"})
        >>> assert len(monitor.resources) == 2
        >>> assert monitor.get_resources_by_type("aws:s3:Bucket") == [{"name": "my-bucket", "props": {"acl": "private"}}]
    """

    def __init__(self):
        pass

    def create_resource(self, resource_type: str, name: str, props: dict):
        pass

    def get_resources_by_type(self, resource_type: str) -> list[dict]:
        pass

    def assert_resource_exists(self, resource_type: str, name: str) -> bool:
        pass

    def assert_property(self, resource_type: str, name: str, prop: str, expected) -> bool:
        pass


def check_policies(resources: list[dict], rules: list[dict]) -> list[dict]:
    """Check resources against policy rules.

    Args:
        resources: list of dicts with keys: name, type, properties
        rules: list of dicts with keys: name, resource_type, check (callable)

    Returns:
        list of violations: [{"resource": str, "rule": str, "message": str}]

    Example:
        >>> resources = [
        ...     {"name": "bad-bucket", "type": "aws:s3:Bucket", "properties": {"acl": "public-read"}},
        ...     {"name": "good-bucket", "type": "aws:s3:Bucket", "properties": {"acl": "private"}},
        ... ]
        >>> rules = [
        ...     {"name": "no-public-buckets", "resource_type": "aws:s3:Bucket",
        ...      "check": lambda p: p.get("acl") != "public-read", "message": "S3 bucket must not be public"}
        ... ]
        >>> violations = check_policies(resources, rules)
        >>> assert len(violations) == 1
        >>> assert violations[0]["resource"] == "bad-bucket"
    """
    pass


def generate_test_report(results: list[dict]) -> dict:
    """Generate a structured test report.

    Args:
        results: list of dicts with keys: resource, rule, status ("pass"/"fail"/"skip"), message

    Returns:
        dict: {
            "total": int,
            "passed": int,
            "failed": int,
            "skipped": int,
            "failures": [{"resource": str, "rule": str, "message": str}],
            "pass_rate": float
        }

    Example:
        >>> report = generate_test_report([
        ...     {"resource": "bucket-1", "rule": "no-public", "status": "pass", "message": ""},
        ...     {"resource": "bucket-2", "rule": "no-public", "status": "fail", "message": "public ACL"},
        ... ])
        >>> assert report["pass_rate"] == 0.5
    """
    pass


if __name__ == "__main__":
    # Mock demo
    monitor = MockResourceMonitor()
    monitor.create_resource("aws:s3:Bucket", "data-bucket", {"acl": "private", "versioning": True})
    monitor.create_resource("aws:ec2:Instance", "web-1", {"instance_type": "t3.micro", "tags": {"env": "prod"}})
    print("Resources:", monitor.resources)

    # Policy check demo
    resources = [
        {"name": "bad-bucket", "type": "aws:s3:Bucket", "properties": {"acl": "public-read"}},
        {"name": "untagged-ec2", "type": "aws:ec2:Instance", "properties": {"instance_type": "t3.micro"}},
    ]
    rules = [
        {"name": "no-public-buckets", "resource_type": "aws:s3:Bucket",
         "check": lambda p: p.get("acl") != "public-read", "message": "Bucket must not be public"},
        {"name": "require-tags", "resource_type": "aws:ec2:Instance",
         "check": lambda p: bool(p.get("tags")), "message": "EC2 must have tags"},
    ]
    violations = check_policies(resources, rules)
    print("Violations:", violations)

    # Report demo
    report = generate_test_report([
        {"resource": "bucket-1", "rule": "no-public", "status": "pass", "message": ""},
        {"resource": "bucket-2", "rule": "no-public", "status": "fail", "message": "public ACL"},
        {"resource": "ec2-1", "rule": "require-tags", "status": "skip", "message": "n/a"},
    ])
    print("Report:", report)
