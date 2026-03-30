"""
Task 05: Table API & SQL
Write your PyFlink Table/SQL pipelines here.
Run: python solution.py
"""
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment


def sql_aggregation():
    """Exercise 1: SQL aggregation - total price per category."""
    env = StreamExecutionEnvironment.get_execution_environment()
    t_env = StreamTableEnvironment.create(env)
    pass


def windowed_sql():
    """Exercise 2: Windowed SQL with TUMBLE TVF."""
    env = StreamExecutionEnvironment.get_execution_environment()
    t_env = StreamTableEnvironment.create(env)
    pass


def stream_table_conversion():
    """Exercise 3: DataStream -> Table -> SQL -> DataStream."""
    env = StreamExecutionEnvironment.get_execution_environment()
    t_env = StreamTableEnvironment.create(env)
    pass


if __name__ == "__main__":
    print("=== Exercise 1: SQL Aggregation ===")
    sql_aggregation()

    print("\n=== Exercise 2: Windowed SQL ===")
    windowed_sql()

    print("\n=== Exercise 3: Stream-Table Conversion ===")
    stream_table_conversion()
