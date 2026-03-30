"""Project Setup — Pulumi project structure and config exercises."""

import yaml


def parse_pulumi_yaml(file_path: str) -> dict:
    """Parse a Pulumi.yaml file and return project metadata.

    Args:
        file_path: path to Pulumi.yaml

    Returns:
        dict with keys: name, runtime, description

    Example:
        >>> meta = parse_pulumi_yaml("Pulumi.yaml")
        >>> print(meta["name"], meta["runtime"])
    """
    pass


def generate_stack_configs() -> dict:
    """Generate config dicts for dev, staging, and prod stacks.

    Returns:
        dict: {
            "dev": {"instance_type": ..., "replicas": ..., "debug": ..., ...},
            "staging": {...},
            "prod": {...}
        }

    Example:
        >>> configs = generate_stack_configs()
        >>> assert configs["prod"]["replicas"] > configs["dev"]["replicas"]
    """
    pass


def classify_config_keys(config: dict) -> dict:
    """Classify config keys as 'plain' or 'secret'.

    Args:
        config: flat dict of config key-value pairs

    Returns:
        dict: {"plain": {k: v, ...}, "secret": {k: v, ...}}

    Example:
        >>> result = classify_config_keys({
        ...     "region": "us-east-1",
        ...     "db_password": "hunter2",
        ...     "app_name": "myapp",
        ...     "api_token": "abc123"
        ... })
        >>> assert "db_password" in result["secret"]
        >>> assert "region" in result["plain"]
    """
    pass


if __name__ == "__main__":
    print("Stack configs:", generate_stack_configs())
    print()
    print("Classified:", classify_config_keys({
        "region": "us-east-1",
        "db_password": "hunter2",
        "app_name": "myapp",
        "api_token": "abc123",
        "replicas": "3",
        "tls_key": "-----BEGIN...",
    }))
