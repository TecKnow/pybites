from typing import Collection

def uncommon_cities(my_cities: Collection, other_cities: Collection) -> int:
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    return len(set(my_cities).symmetric_difference(other_cities))