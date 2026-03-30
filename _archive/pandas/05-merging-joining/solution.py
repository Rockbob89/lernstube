import pandas as pd


def safe_merge(
    left: pd.DataFrame, right: pd.DataFrame, on: str, how: str
) -> pd.DataFrame:
    pass


def multi_table_join(dfs: list[pd.DataFrame], on: str) -> pd.DataFrame:
    pass


def concat_with_source(dfs: list[pd.DataFrame], names: list[str]) -> pd.DataFrame:
    pass


def find_unmatched(
    left: pd.DataFrame, right: pd.DataFrame, on: str
) -> tuple[pd.DataFrame, pd.DataFrame]:
    pass


if __name__ == "__main__":
    print("=== safe_merge ===")
    left = pd.DataFrame({"id": [1, 2, 3], "val": ["a", "b", "c"]})
    right = pd.DataFrame({"id": [2, 3, 4], "score": [90, 80, 70]})
    print(safe_merge(left, right, on="id", how="left"))

    print("\n=== multi_table_join ===")
    df1 = pd.DataFrame({"id": [1, 2], "a": [10, 20]})
    df2 = pd.DataFrame({"id": [1, 2], "b": [30, 40]})
    df3 = pd.DataFrame({"id": [1], "c": [50]})
    print(multi_table_join([df1, df2, df3], on="id"))

    print("\n=== concat_with_source ===")
    df1 = pd.DataFrame({"x": [1, 2]})
    df2 = pd.DataFrame({"x": [3, 4]})
    print(concat_with_source([df1, df2], ["file_a", "file_b"]))

    print("\n=== find_unmatched ===")
    left = pd.DataFrame({"id": [1, 2, 3], "val": ["a", "b", "c"]})
    right = pd.DataFrame({"id": [2, 4], "score": [90, 70]})
    lo, ro = find_unmatched(left, right, on="id")
    print(f"left_only:\n{lo}\nright_only:\n{ro}")
