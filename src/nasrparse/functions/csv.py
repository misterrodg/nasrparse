from io import TextIOWrapper
from charset_normalizer import from_path


def open_csv(csv_path: str) -> TextIOWrapper:
    result = from_path(csv_path).best()
    encoding = result.encoding or "utf-8"
    return open(csv_path, encoding=encoding, newline="")
