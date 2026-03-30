import pandas as pd
from typing import Callable


def create_date_range_df(
    start: str, end: str, freq: str, value_func: Callable
) -> pd.DataFrame:
    pass


def resample_ohlc(df: pd.DataFrame, rule: str) -> pd.DataFrame:
    pass


def rolling_zscore(series: pd.Series, window: int) -> pd.Series:
    pass


def business_day_stats(df: pd.DataFrame, tz: str) -> dict:
    pass


if __name__ == "__main__":
    print("=== create_date_range_df ===")
    df = create_date_range_df("2024-01-01", "2024-01-05", "D", lambda idx: range(len(idx)))
    print(df)

    print("\n=== resample_ohlc ===")
    idx = pd.date_range("2024-01-01", periods=48, freq="h")
    df = pd.DataFrame({"price": range(48)}, index=idx)
    print(resample_ohlc(df, "D"))

    print("\n=== rolling_zscore ===")
    s = pd.Series([1, 2, 3, 10, 3, 2, 1], index=pd.date_range("2024-01-01", periods=7))
    print(rolling_zscore(s, 3))

    print("\n=== business_day_stats ===")
    idx = pd.date_range("2024-01-01", periods=100, freq="3h", tz="UTC")
    df = pd.DataFrame({"val": range(100)}, index=idx)
    print(business_day_stats(df, "US/Eastern"))
