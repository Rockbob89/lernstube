"""Persistence & WAN Replication — MapStore, WAN sync, conflict resolution."""

import time
from typing import Any, Callable


class MapStore:
    """Simulated Hazelcast MapStore with write-through and write-behind.

    Example:
        >>> db = {}  # simulated database
        >>> store = MapStore(db, mode="write-behind", batch_size=5, coalesce=True)
        >>> store.put("key1", "value1")
        >>> store.put("key1", "value2")  # coalesces with previous
        >>> store.flush()
        >>> print(db)  # {"key1": "value2"} — only latest value written
    """

    def __init__(self, backend: dict, mode: str = "write-through",
                 batch_size: int = 10, coalesce: bool = True):
        pass

    def put(self, key: str, value: Any):
        pass

    def get(self, key: str) -> Any:
        """Load from cache, fallback to backend (MapLoader pattern)."""
        pass

    def flush(self) -> dict:
        """Flush write-behind buffer to backend.

        Returns:
            dict: {"writes": int, "coalesced": int}
        """
        pass

    def stats(self) -> dict:
        pass


class WanReplicator:
    """Simulated WAN replication between two clusters.

    Example:
        >>> cluster_a = {}
        >>> cluster_b = {}
        >>> wan = WanReplicator(cluster_a, cluster_b, mode="active-passive")
        >>> wan.put("a", "key1", "value1")  # write to cluster A
        >>> print(cluster_b["key1"])  # replicated
    """

    def __init__(self, cluster_a: dict, cluster_b: dict, mode: str = "active-passive"):
        pass

    def put(self, cluster: str, key: str, value: Any):
        """Write to a cluster. Replicate according to mode.

        Args:
            cluster: "a" or "b"
            key: cache key
            value: cache value
        """
        pass

    def get_conflicts(self) -> list[dict]:
        """Return detected conflicts (active-active mode)."""
        pass

    def resolve_conflicts(self, policy: str = "latest-update") -> dict:
        """Resolve all conflicts using given policy.

        Returns:
            dict: {"resolved": int, "policy": str, "results": list}
        """
        pass


def merge_entries(entry_a: dict, entry_b: dict, policy: str | Callable) -> dict:
    """Resolve conflict between two entries from different clusters.

    Args:
        entry_a: {"value": Any, "timestamp": float, "hits": int, "cluster": str}
        entry_b: {"value": Any, "timestamp": float, "hits": int, "cluster": str}
        policy: "latest-update", "highest-hits", or a callable(a, b) -> winner

    Returns:
        dict: the winning entry with "resolved_by" added

    Example:
        >>> a = {"value": "v1", "timestamp": 1000, "hits": 5, "cluster": "us-east"}
        >>> b = {"value": "v2", "timestamp": 1001, "hits": 3, "cluster": "eu-west"}
        >>> winner = merge_entries(a, b, "latest-update")
        >>> print(winner["value"])  # "v2"
    """
    pass


if __name__ == "__main__":
    # MapStore demo
    db = {}
    store = MapStore(db, mode="write-behind", batch_size=5, coalesce=True)
    store.put("user:1", {"name": "Alice", "v": 1})
    store.put("user:1", {"name": "Alice", "v": 2})
    store.put("user:1", {"name": "Alice", "v": 3})
    store.put("user:2", {"name": "Bob", "v": 1})
    result = store.flush()
    print(f"Flush result: {result}")
    print(f"DB state: {db}")

    # WAN replication demo
    ca, cb = {}, {}
    wan = WanReplicator(ca, cb, mode="active-active")
    wan.put("a", "key1", "from-A")
    wan.put("b", "key1", "from-B")
    print(f"Conflicts: {wan.get_conflicts()}")

    # Merge demo
    a = {"value": "old", "timestamp": 1000.0, "hits": 10, "cluster": "us"}
    b = {"value": "new", "timestamp": 1001.0, "hits": 3, "cluster": "eu"}
    print(f"Latest wins: {merge_entries(a, b, 'latest-update')}")
    print(f"Most hits wins: {merge_entries(a, b, 'highest-hits')}")
