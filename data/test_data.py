from enum import Enum


class SortOptions(str, Enum):
    LOW_TO_HIGH = "Price: low to high"
    HIGH_TO_LOW = "Price: high to low"


SEARCH_AND_NUMBER = [("city", 10), ("habits", 15)]
FILTERS = [SortOptions.LOW_TO_HIGH, SortOptions.HIGH_TO_LOW]
