"""
Task 04: State & Checkpointing
Write your stateful PyFlink pipelines here.
Run: python solution.py
"""
from pyflink.datastream import StreamExecutionEnvironment


# Exercise 1: ValueState counter - emit every 3rd event per user
# Write a KeyedProcessFunction class here


# Exercise 2: MapState deduplication
# Write a KeyedProcessFunction class here


# Exercise 3: Checkpoint configuration
def configure_checkpointing(env: StreamExecutionEnvironment):
    """Configure checkpointing: 30s interval, exactly-once, RocksDB."""
    pass


def exercise_1():
    env = StreamExecutionEnvironment.get_execution_environment()
    pass


def exercise_2():
    env = StreamExecutionEnvironment.get_execution_environment()
    pass


if __name__ == "__main__":
    print("=== Exercise 1: ValueState Counter ===")
    exercise_1()

    print("\n=== Exercise 2: MapState Deduplication ===")
    exercise_2()

    print("\n=== Exercise 3: Checkpoint Config ===")
    env = StreamExecutionEnvironment.get_execution_environment()
    configure_checkpointing(env)
    print("Checkpointing configured (inspect env settings)")
