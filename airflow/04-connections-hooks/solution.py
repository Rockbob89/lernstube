"""
Task 04: Connections & Hooks
"""
from airflow.decorators import dag, task


# Exercise 1: Write the AIRFLOW_CONN_ env var as a string
POSTGRES_CONN_ENV = ""  # Fill this in


# Exercise 2: Hook demo DAG


# Exercise 3: Test postgres connection
def test_postgres_connection(conn_id: str) -> bool:
    pass


if __name__ == "__main__":
    print(f"POSTGRES_CONN_ENV = {POSTGRES_CONN_ENV}")
    print(f"test_postgres_connection result: {test_postgres_connection('my_postgres')}")
