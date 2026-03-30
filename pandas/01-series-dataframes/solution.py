import pandas as pd


def create_employee_df(
    names: list[str], salaries: list[int], departments: list[str]
) -> pd.DataFrame:
    pass


def df_summary(df: pd.DataFrame) -> dict:
    pass


def reindex_by_column(df: pd.DataFrame, col: str) -> pd.DataFrame:
    pass


def safe_add_column(df: pd.DataFrame, col_name: str, values: list) -> pd.DataFrame:
    pass


if __name__ == "__main__":
    print("=== create_employee_df ===")
    print(create_employee_df(["Alice", "Bob"], [90000, 85000], ["Eng", "Sales"]))

    print("\n=== df_summary ===")
    print(df_summary(pd.DataFrame({"a": [1, 2], "b": ["x", "y"]})))

    print("\n=== reindex_by_column ===")
    df = pd.DataFrame({"id": [10, 20], "val": [1, 2]})
    print(reindex_by_column(df, "id"))

    print("\n=== safe_add_column ===")
    df = pd.DataFrame({"a": [1, 2]})
    print(safe_add_column(df, "b", [3, 4]))
