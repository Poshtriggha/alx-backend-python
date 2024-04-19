from typing import Mapping, Any, TypeVar, Union

# Define a type variable for the default value
T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Get a value safely from a dictionary.

    """
    if key in dct:
        return dct[key]
    else:
        return default
