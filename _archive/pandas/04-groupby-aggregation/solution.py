import pandas as pd


def sales_summary(df: pd.DataFrame) -> pd.DataFrame:
    pass


def group_rank(df: pd.DataFrame, group_col: str, value_col: str) -> pd.Series:
    pass


def pivot_summary(
    df: pd.DataFrame, index: str, columns: str, values: str, aggfunc: str
) -> pd.DataFrame:
    pass


def filter_groups(df: pd.DataFrame, group_col: str, min_size: int) -> pd.DataFrame:
    pass


if __name__ == "__main__":
    print("=== sales_summary ===")
    df = pd.DataFrame({
        "region": ["East", "East", "West"],
        "product": ["A", "B", "A"],
        "revenue": [100, 200, 150],
        "quantity": [10, 20, 15],
    })
    print(sales_summary(df))

    print("\n=== group_rank ===")
    df = pd.DataFrame({"dept": ["A", "A", "B", "B"], "score": [90, 80, 70, 95]})
    print(group_rank(df, "dept", "score"))

    print("\n=== pivot_summary ===")
    df = pd.DataFrame({
        "month": ["Jan", "Jan", "Feb"],
        "product": ["A", "B", "A"],
        "sales": [10, 20, 15],
    })
    print(pivot_summary(df, "month", "product", "sales", "sum"))

    print("\n=== filter_groups ===")
    df = pd.DataFrame({"cat": ["a", "a", "b", "a", "b", "c"], "val": range(6)})
    print(filter_groups(df, "cat", 2))
