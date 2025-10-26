from datetime import datetime, date


def to_nullable_bool(string: str) -> bool | None:
    string = string.strip()
    if string == "Y":
        return True
    if string == "N":
        return False
    return None


def to_nullable_date(string: str, format: str) -> date | None:
    string = string.strip()
    if string == "":
        return None
    if format == "YYYY/MM":
        string += "/01"
    try:
        date_object = datetime.strptime(string, "%Y/%m/%d")
        return date_object.date()
    except ValueError:
        print(
            f"{__name__}: Could not convert '{string}' to a date in format '{format}'."
        )
        return None
    except TypeError:
        print(f"{__name__}: Input {string} is not a valid string type.")
        return None


def to_nullable_float(string: str) -> float | None:
    string = string.strip()
    if string == "":
        return None
    try:
        result = float(string)
        return result
    except ValueError:
        print(f"{__name__}: Could not convert '{string}' to a float.")
        return None
    except TypeError:
        print(f"{__name__}: Input {string} is not a valid string type.")
        return None


def to_nullable_int(string: str) -> int | None:
    string = string.strip()
    if string == "":
        return None
    try:
        result = int(string)
        return result
    except ValueError:
        print(f"{__name__}: Could not convert '{string}' to an integer.")
        return None
    except TypeError:
        print(f"{__name__}: Input {string} is not a valid string type.")
        return None


def to_nullable_string(string: str) -> str | None:
    string = string.strip()
    if string == "":
        return None
    return string
