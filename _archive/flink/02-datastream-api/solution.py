"""
Task 02: DataStream API
Write your PyFlink DataStream pipelines here.
Run: python solution.py
"""
from pyflink.datastream import StreamExecutionEnvironment


def basic_pipeline():
    """Exercise 1: Filter and transform sensor readings."""
    env = StreamExecutionEnvironment.get_execution_environment()
    pass


def keyby_reduce_pipeline():
    """Exercise 2: Key-by user and reduce to running sum."""
    env = StreamExecutionEnvironment.get_execution_environment()
    pass


def flatmap_pipeline():
    """Exercise 3: FlatMap sentences to filtered words."""
    env = StreamExecutionEnvironment.get_execution_environment()
    pass


if __name__ == "__main__":
    print("=== Exercise 1: Basic Pipeline ===")
    basic_pipeline()

    print("\n=== Exercise 2: KeyBy + Reduce ===")
    keyby_reduce_pipeline()

    print("\n=== Exercise 3: FlatMap ===")
    flatmap_pipeline()
