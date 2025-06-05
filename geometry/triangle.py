import math
import logging
from dataclasses import dataclass
from base import Shape

logger = logging.getLogger(__name__)


@dataclass
class Triangle(Shape):
    a: float
    b: float
    c: float

    def __post_init__(self):
        if not self._is_valid():
            raise ValueError("Invalid triangle sides")

    def _is_valid(self) -> bool:
        return (
                self.a + self.b > self.c
                and self.a + self.c > self.b
                and self.b + self.c > self.a
        )

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        result = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        logger.info(f"Calculated area of triangle: {result}")
        return result

    def is_right(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)
