import math
import logging
from dataclasses import dataclass
from base import Shape

logger = logging.getLogger(__name__)


@dataclass
class Circle(Shape):
    radius: float

    def area(self) -> float:
        if self.radius <= 0:
            raise ValueError("Radius must be positive")
        result = math.pi * self.radius ** 2
        logger.info(f"Calculated area of circle: {result}")
        return result
