from pathlib import Path


def word_frequency(filepath):
    pass

def merge_csv_files(filepaths, output):
    pass

def json_transform(input_path, output_path, transform_fn):
    pass

def find_files(directory, pattern):
    pass


if __name__ == "__main__":
    # word_frequency
    print(word_frequency(Path("sample.txt")))

    # merge_csv_files
    merge_csv_files([Path("a.csv"), Path("b.csv")], Path("merged.csv"))

    # json_transform
    json_transform(
        Path("input.json"),
        Path("output.json"),
        lambda item: {**item, "name": item["name"].upper()}
    )

    # find_files
    print(find_files(Path("."), "*.py"))
