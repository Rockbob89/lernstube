"""What Hazelcast Is — comparison and use case exercises."""


def compare_technologies(tech_a: str, tech_b: str) -> dict:
    """Compare two caching/IMDG technologies across key dimensions.

    Args:
        tech_a: one of 'hazelcast', 'redis', 'memcached', 'ignite'
        tech_b: one of 'hazelcast', 'redis', 'memcached', 'ignite'

    Returns:
        dict: {
            "dimensions": {
                "data_model": {"tech_a": str, "tech_b": str},
                "clustering": {...},
                "compute": {...},
                "persistence": {...},
                "language_support": {...},
                "licensing": {...}
            },
            "summary": str
        }

    Example:
        >>> result = compare_technologies("hazelcast", "redis")
        >>> print(result["dimensions"]["compute"])
    """
    pass


def match_use_case(requirements: dict) -> dict:
    """Recommend a technology based on requirements.

    Args:
        requirements: dict with keys:
            - need_compute: bool
            - embedded_mode: bool
            - data_size_gb: int
            - language: str (e.g. 'java', 'python', 'go')
            - latency_requirement_ms: int

    Returns:
        dict: {"recommendation": str, "reasoning": list[str], "alternatives": list[str]}

    Example:
        >>> result = match_use_case({
        ...     "need_compute": True,
        ...     "embedded_mode": True,
        ...     "data_size_gb": 50,
        ...     "language": "java",
        ...     "latency_requirement_ms": 1
        ... })
        >>> print(result["recommendation"])  # "hazelcast"
    """
    pass


def describe_architecture(mode: str) -> dict:
    """Describe Hazelcast architecture for a given deployment mode.

    Args:
        mode: one of 'embedded', 'client-server', 'cloud'

    Returns:
        dict: {
            "components": list[str],
            "communication": str,
            "pros": list[str],
            "cons": list[str],
            "best_for": str
        }

    Example:
        >>> arch = describe_architecture("embedded")
        >>> print(arch["pros"])
    """
    pass


if __name__ == "__main__":
    print("=== Hazelcast vs Redis ===")
    print(compare_technologies("hazelcast", "redis"))
    print()
    print("=== Use Case Match ===")
    print(match_use_case({
        "need_compute": True,
        "embedded_mode": False,
        "data_size_gb": 100,
        "language": "python",
        "latency_requirement_ms": 5,
    }))
    print()
    print("=== Client-Server Architecture ===")
    print(describe_architecture("client-server"))
