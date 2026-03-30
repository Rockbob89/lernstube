"""
Task 06: Connectors
Write your connector DDL and pipeline code here.
Run: python solution.py (validates DDL syntax with Flink, but needs infra for actual execution)
"""
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment


# Exercise 1: Kafka source DDL
KAFKA_SOURCE_DDL = """
"""


# Exercise 2: Kafka sink DDL
KAFKA_SINK_DDL = """
"""


# Exercise 3: End-to-end SQL pipeline
INSERT_SQL = """
"""


# Exercise 4: FileSystem source DDL
FILESYSTEM_SOURCE_DDL = """
"""


def register_and_run():
    """Register tables and execute the pipeline."""
    env = StreamExecutionEnvironment.get_execution_environment()
    t_env = StreamTableEnvironment.create(env)
    pass


if __name__ == "__main__":
    print("=== Kafka Source DDL ===")
    print(KAFKA_SOURCE_DDL)

    print("\n=== Kafka Sink DDL ===")
    print(KAFKA_SINK_DDL)

    print("\n=== Insert SQL ===")
    print(INSERT_SQL)

    print("\n=== FileSystem Source DDL ===")
    print(FILESYSTEM_SOURCE_DDL)
