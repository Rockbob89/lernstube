"""
Task 06: Testing & Debugging
Write your DAG tests here. Run with: pytest solution.py -v
"""
import pytest


# Exercise 1: DAG validation test
def test_dag_import_no_errors():
    """Import all DAGs and assert no import errors."""
    pass


def test_dag_no_cycles():
    """Assert no DAG has cycles."""
    pass


# Exercise 2: Structure test for etl_basic
def test_etl_basic_task_count():
    """etl_basic should have exactly 3 tasks."""
    pass


def test_etl_basic_task_ids():
    """etl_basic should have extract, transform, load tasks."""
    pass


def test_etl_basic_dependencies():
    """extract >> transform >> load dependency chain."""
    pass


# Exercise 3: List the 4 bugs in the buggy DAG
BUGS = [
    # "Bug 1: ...",
    # "Bug 2: ...",
    # "Bug 3: ...",
    # "Bug 4: ...",
]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
