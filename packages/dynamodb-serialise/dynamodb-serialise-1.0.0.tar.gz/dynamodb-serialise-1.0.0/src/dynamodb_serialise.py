"""Deserialise from and serialise to DynamoDB."""

import collections
import typing as t


def _number(v: str) -> t.Union[float, int]:
    """Convert to number, ie int otherwise float."""
    try:
        return int(v)
    except ValueError:
        return float(v)


def _binary(v: t.Union[str, bytes]) -> bytes:
    """Convert to bytes, ie decode base-64 if string."""
    if isinstance(v, bytes):
        return v

    import base64

    v_b64 = v.encode()
    return base64.b64decode(v_b64)


def deserialise(o: t.Dict[str, t.Any]) -> t.Any:
    """Deserialise value from DynamoDB."""
    try:
        (dynamodb_type,) = o
    except ValueError:
        raise ValueError(f"Invalid DynamoDB value: {o}") from None
    data = o[dynamodb_type]
    if dynamodb_type == "M":
        return {k: deserialise(v) for k, v in data.items()}
    elif dynamodb_type == "L":
        return [deserialise(v) for v in data]
    elif dynamodb_type == "SS":
        return {v for v in data}
    elif dynamodb_type == "NS":
        return {_number(v) for v in data}
    elif dynamodb_type == "BS":
        return {_binary(v) for v in data}
    elif dynamodb_type == "N":
        return _number(data)
    elif dynamodb_type == "B":
        return _binary(data)
    elif dynamodb_type in ("S", "BOOL", "B"):
        return data
    elif dynamodb_type == "NULL":
        return None
    else:
        raise ValueError(f"Unknown DynamoDB type '{dynamodb_type}': {o}")


def serialise(
    o: t.Any,
    bytes_to_base64: bool = False,
    empty_set_type: str = "SS",
    fallback: t.Callable[[t.Any], t.Dict[str, t.Any]] = None,
) -> t.Dict[str, t.Any]:
    """Serialise value to DynamoDB.

    Args:
        o: value to serialise
        bytes_to_base64: convert bytestrings to base-64 strings
        empty_set_type: set type string for empty sets
        fallback: applied to values with unhandled types, default: raise
    """

    if o is None:
        return {"NULL": True}
    elif isinstance(o, str):
        return {"S": o}
    elif isinstance(o, bool):
        return {"BOOL": o}
    elif isinstance(o, (int, float)):
        return {"N": str(o)}
    elif isinstance(o, bytes):
        if bytes_to_base64:
            import base64

            o = base64.b64encode(o).decode()
        return {"B": o}

    elif isinstance(o, set):
        if not o:
            import warnings

            warnings.warn(f"Casting empty set to type: {empty_set_type}")
            return {empty_set_type: []}

        first, *remaining = o
        for type_, key in ((str, "SS"), ((int, float), "NS"), (bytes, "BS")):
            if isinstance(first, type_):
                if not all(isinstance(r, type_) for r in remaining):
                    raise ValueError(f"Set elements must be of only one type: {o}")
                break
        else:
            raise ValueError(f"Unhandled type for set elements: {o}")

        if type_ == (int, float):
            o = [str(v) for v in o]
        elif type_ is bytes and bytes_to_base64:
            import base64

            o = [base64.b64encode(v).decode() for v in o]
        else:
            o = list(o)
        return {key: list(o)}

    elif isinstance(o, (list, tuple, collections.UserList)):
        return {
            "L": [serialise(v, bytes_to_base64, empty_set_type, fallback) for v in o]
        }

    elif isinstance(o, (dict, collections.OrderedDict, collections.UserDict)):
        return {
            "M": {
                k: serialise(v, bytes_to_base64, empty_set_type, fallback)
                for k, v in o.items()
            }
        }

    elif fallback:
        return fallback(o)
    else:
        raise ValueError(f"Unhandled type: {o}")
