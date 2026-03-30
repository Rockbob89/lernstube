import pandas as pd
from pathlib import Path


def smart_read_csv(path: str, **kwargs) -> pd.DataFrame:
    pass


def chunked_filter(
    path: str, column: str, value: str, chunksize: int = 10000
) -> pd.DataFrame:
    pass


def convert_format(input_path: str, output_path: str) -> None:
    pass


def df_to_json_records(df: pd.DataFrame) -> str:
    pass


if __name__ == "__main__":
    print("=== df_to_json_records ===")
    df = pd.DataFrame({
        "a": [1, None],
        "date": pd.to_datetime(["2024-01-01", "2024-06-15"]),
    })
    print(df_to_json_records(df))

    # smart_read_csv, chunked_filter, convert_format require files
    # Create a test CSV to try them:
    test_df = pd.DataFrame({"name": ["Alice", "Bob"], "score": [95, 87]})
    test_df.to_csv("/tmp/test_io.csv", index=False)

    print("\n=== smart_read_csv ===")
    print(smart_read_csv("/tmp/test_io.csv"))

    print("\n=== convert_format ===")
    convert_format("/tmp/test_io.csv", "/tmp/test_io.json")
    print(pd.read_json("/tmp/test_io.json"))
