"""
Task 2: Architecture — Solutions
"""


def query_flow() -> list[dict[str, str]]:
    """
    Exercise 1: Return an ordered list of steps describing how a query
    flows through Druid. Each step is a dict with 'node' and 'action' keys.

    Example:
        [
            {"node": "Client", "action": "sends query to ..."},
            {"node": "???", "action": "..."},
            ...
        ]
    """
    return []


def node_failure_analysis() -> dict[str, dict[str, str]]:
    """
    Exercise 2: For each node type, describe impact of a single instance failure.
    Return a dict mapping node type to:
        {
            "impact": "what breaks",
            "data_loss": "yes/no and why",
            "self_healing": "yes/no and how"
        }
    """
    node_types = [
        "Historical",
        "Broker",
        "Coordinator",
        "Overlord",
        "MiddleManager",
    ]
    return {node: {"impact": "", "data_loss": "", "self_healing": ""} for node in node_types}


def capacity_estimate() -> dict:
    """
    Exercise 3: Given:
        - 3 Historicals, each 64GB RAM, 1TB SSD
        - Average segment size: 500MB
        - Compression ratio: 10:1 (segment-to-raw)

    Calculate:
        - total_ssd_capacity_tb: total SSD across cluster
        - max_segments: how many segments fit on disk
        - raw_data_per_segment_gb: raw data represented by one segment
        - total_raw_data_tb: total raw data the cluster can serve
        - estimated_events: rough event count (assume ~200 bytes/event avg)

    Return a dict with these keys and your computed values.
    """
    return {
        "total_ssd_capacity_tb": 0,
        "max_segments": 0,
        "raw_data_per_segment_gb": 0,
        "total_raw_data_tb": 0,
        "estimated_events": 0,
    }


if __name__ == "__main__":
    print("=== Exercise 1: Query Flow ===")
    for step in query_flow():
        print(f"  {step['node']}: {step['action']}")

    print("\n=== Exercise 2: Node Failure Analysis ===")
    for node, analysis in node_failure_analysis().items():
        print(f"  {node}:")
        for k, v in analysis.items():
            print(f"    {k}: {v}")

    print("\n=== Exercise 3: Capacity Estimate ===")
    for k, v in capacity_estimate().items():
        print(f"  {k}: {v}")
