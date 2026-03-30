"""Jet (Stream Processing) — pipelines, windowing, event-time processing."""

from typing import Any, Callable
from collections import defaultdict


class JetPipeline:
    """Simulated Hazelcast Jet pipeline with fluent API.

    Example:
        >>> events = [
        ...     {"user": "alice", "action": "click", "value": 1},
        ...     {"user": "bob", "action": "view", "value": 2},
        ...     {"user": "alice", "action": "click", "value": 3},
        ... ]
        >>> result = (JetPipeline()
        ...     .read_from(events)
        ...     .filter(lambda e: e["action"] == "click")
        ...     .map(lambda e: {"user": e["user"], "value": e["value"]})
        ...     .group_by(lambda e: e["user"])
        ...     .aggregate(lambda group: sum(e["value"] for e in group))
        ...     .write_to("stdout")
        ...     .execute())
        >>> print(result)  # {"alice": 4}
    """

    def __init__(self):
        pass

    def read_from(self, source) -> "JetPipeline":
        pass

    def map(self, func: Callable) -> "JetPipeline":
        pass

    def filter(self, func: Callable) -> "JetPipeline":
        pass

    def flat_map(self, func: Callable) -> "JetPipeline":
        pass

    def group_by(self, key_fn: Callable) -> "JetPipeline":
        pass

    def aggregate(self, agg_fn: Callable) -> "JetPipeline":
        pass

    def write_to(self, sink: str) -> "JetPipeline":
        pass

    def execute(self) -> Any:
        pass


def tumbling_window(events: list[dict], window_size_ms: int,
                    timestamp_field: str = "timestamp",
                    agg_fn: Callable = None) -> list[dict]:
    """Group timestamped events into fixed-size non-overlapping windows.

    Args:
        events: list of dicts with a timestamp field
        window_size_ms: window size in milliseconds
        timestamp_field: name of timestamp field
        agg_fn: aggregation function applied per window, receives list of events

    Returns:
        list of dicts: [{"window_start": int, "window_end": int, "result": Any}]

    Example:
        >>> events = [
        ...     {"timestamp": 1000, "value": 1},
        ...     {"timestamp": 1500, "value": 2},
        ...     {"timestamp": 2500, "value": 3},
        ...     {"timestamp": 3500, "value": 4},
        ... ]
        >>> windows = tumbling_window(events, 2000, agg_fn=lambda evts: sum(e["value"] for e in evts))
        >>> print(windows)
        # [{"window_start": 0, "window_end": 2000, "result": 3}, ...]
    """
    pass


def sliding_window(events: list[dict], window_size_ms: int, slide_ms: int,
                   timestamp_field: str = "timestamp",
                   agg_fn: Callable = None) -> list[dict]:
    """Group events into overlapping windows.

    Args:
        events: list of dicts with a timestamp field
        window_size_ms: window size in milliseconds
        slide_ms: slide interval in milliseconds
        timestamp_field: name of timestamp field
        agg_fn: aggregation function

    Returns:
        list of window results

    Example:
        >>> windows = sliding_window(events, window_size_ms=3000, slide_ms=1000, ...)
    """
    pass


class EventTimeProcessor:
    """Process events in event-time order with watermark support.

    Example:
        >>> processor = EventTimeProcessor(max_lateness_ms=1000)
        >>> processor.process({"timestamp": 1000, "value": "a"})
        >>> processor.process({"timestamp": 3000, "value": "b"})
        >>> processor.advance_watermark(2500)
        >>> processor.process({"timestamp": 1200, "value": "late"})  # late event
        >>> print(processor.late_events)
        [{"timestamp": 1200, "value": "late"}]
    """

    def __init__(self, max_lateness_ms: int = 0):
        pass

    def process(self, event: dict) -> str:
        """Process event. Returns 'accepted' or 'late'.

        Args:
            event: dict with 'timestamp' key
        """
        pass

    def advance_watermark(self, timestamp: int):
        pass

    @property
    def late_events(self) -> list[dict]:
        pass

    def stats(self) -> dict:
        """Return processing stats: total, accepted, late, watermark."""
        pass


if __name__ == "__main__":
    # Pipeline demo
    events = [
        {"user": "alice", "action": "click", "value": 1},
        {"user": "bob", "action": "view", "value": 2},
        {"user": "alice", "action": "click", "value": 3},
        {"user": "bob", "action": "click", "value": 5},
    ]
    result = (JetPipeline()
        .read_from(events)
        .filter(lambda e: e["action"] == "click")
        .map(lambda e: {"user": e["user"], "value": e["value"]})
        .group_by(lambda e: e["user"])
        .aggregate(lambda group: sum(e["value"] for e in group))
        .execute())
    print("Pipeline result:", result)

    # Windowing demo
    ts_events = [{"timestamp": i * 500, "value": i} for i in range(10)]
    windows = tumbling_window(ts_events, 2000, agg_fn=lambda evts: sum(e["value"] for e in evts))
    print("Tumbling windows:", windows)

    # Event-time demo
    proc = EventTimeProcessor(max_lateness_ms=1000)
    for e in [{"timestamp": 1000, "v": 1}, {"timestamp": 3000, "v": 2}]:
        proc.process(e)
    proc.advance_watermark(2500)
    proc.process({"timestamp": 1200, "v": "late"})
    print("Late events:", proc.late_events)
    print("Stats:", proc.stats())
