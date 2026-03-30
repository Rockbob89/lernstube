"""Pulumi vs Terraform — comparison exercises."""


def recommend_tool(requirements: dict) -> str:
    """Return 'pulumi' or 'terraform' with reasoning based on project requirements.

    Args:
        requirements: dict with keys:
            - team_lang: str (e.g. 'python', 'go', 'typescript', 'none')
            - infra_complexity: str ('low', 'medium', 'high')
            - existing_iac: str ('none', 'terraform', 'cloudformation')
            - testing_priority: str ('low', 'medium', 'high')

    Returns:
        str: recommendation with reasoning

    Example:
        >>> recommend_tool({
        ...     "team_lang": "python",
        ...     "infra_complexity": "high",
        ...     "existing_iac": "none",
        ...     "testing_priority": "high"
        ... })
    """
    pass


def state_backends() -> dict:
    """Return state backend options for both Pulumi and Terraform.

    Returns:
        dict: {
            "pulumi": [{"name": str, "pros": list, "cons": list}, ...],
            "terraform": [{"name": str, "pros": list, "cons": list}, ...]
        }

    Example:
        >>> backends = state_backends()
        >>> for b in backends["pulumi"]:
        ...     print(f"{b['name']}: {b['pros']}")
    """
    pass


if __name__ == "__main__":
    reqs = {
        "team_lang": "python",
        "infra_complexity": "high",
        "existing_iac": "terraform",
        "testing_priority": "high",
    }
    print("Recommendation:", recommend_tool(reqs))
    print()
    print("State backends:", state_backends())
