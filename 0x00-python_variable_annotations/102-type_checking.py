from typing import Tuple, List, Any

def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    zoomed_in: Tuple[Any, ...] = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in

if __name__ == "__main__":
    array = (12, 72, 91)

    zoom_2x = zoom_array(array)
    print(zoom_2x)

    zoom_3x = zoom_array(array, 3)
    print(zoom_3x)
