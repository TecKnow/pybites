from typing import Literal, Union

IN_TO_CM = 2.54
CM_TO_IN = 1/IN_TO_CM


def convert(value: Union[float, int], fmt: Literal["in", "cm"]) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if not isinstance(value, (int, float)):
        raise TypeError(
            f"<value> must be an int or float, {value} is {type(value)} instead.")
    if not fmt.lower() in ("in", "cm"):
        raise ValueError(
            f"<fmt> must be \"in\" for inches or \"cm\" for centimeters ")
    if fmt.lower() == "cm":
        return round(value * IN_TO_CM, 4)
    else:
        return round(value * CM_TO_IN, 4)
