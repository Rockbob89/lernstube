"""
Task 03: Windowing
Write your windowed PyFlink pipelines here.
Run: python solution.py
"""
from pyflink.datastream import StreamExecutionEnvironment


def tumbling_window_pipeline():
    """Exercise 1: Tumbling window - avg temp per sensor per 10s window."""
    env = StreamExecutionEnvironment.get_execution_environment()
    pass


def sliding_window_pipeline():
    """Exercise 2: Sliding window - 30s window, 10s slide."""
    env = StreamExecutionEnvironment.get_execution_environment()
    pass


def session_window_pipeline():
    """Exercise 3: Session window - clicks per user with 5s gap."""
    env = StreamExecutionEnvironment.get_execution_environment()
    pass


if __name__ == "__main__":
    print("=== Exercise 1: Tumbling Window ===")
    tumbling_window_pipeline()

    print("\n=== Exercise 2: Sliding Window ===")
    sliding_window_pipeline()

    print("\n=== Exercise 3: Session Window ===")
    session_window_pipeline()
