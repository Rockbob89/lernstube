import pandas as pd


def clean_numeric_column(series: pd.Series) -> pd.Series:
    pass


def deduplicate(df: pd.DataFrame, subset: list[str], keep: str | bool) -> pd.DataFrame:
    pass


def fill_strategy(df: pd.DataFrame, strategies: dict) -> pd.DataFrame:
    pass


def standardize_strings(series: pd.Series, operations: list[str]) -> pd.Series:
    pass


if __name__ == "__main__":
    print("=== clean_numeric_column ===")
    s = pd.Series(["$1,234.56", " 789 ", "N/A", "$-42.10", "-"])
    print(clean_numeric_column(s))

    print("\n=== deduplicate ===")
    df = pd.DataFrame({"a": [1, 1, 2], "b": [10, 20, 30]})
    print(deduplicate(df, subset=["a"], keep="last"))

    print("\n=== fill_strategy ===")
    df = pd.DataFrame({"a": [1, None, 3], "b": [None, 5, None]})
    print(fill_strategy(df, {"a": "mean", "b": "zero"}))

    print("\n=== standardize_strings ===")
    s = pd.Series(["  Hello, World!  ", "FOO-BAR  "])
    print(standardize_strings(s, ["strip", "lower", "remove_punctuation"]))
