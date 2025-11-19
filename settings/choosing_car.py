from dataclasses import dataclass


@dataclass
class CarChooise:
    AUTO: str
    MODEL: list[str]
    YEAR_FROM: int
    YEAR_TO: int
    VOLUME: str
    PRICE: int
