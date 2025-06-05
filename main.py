from geometry.circle import Circle
from geometry.triangle import Triangle
from geometry.base import Shape
import logging

logging.basicConfig(level=logging.INFO)

def main():
    shapes: list[Shape] = [
        Circle(radius=3),
        Triangle(a=3, b=4, c=5)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.area()}")

if __name__ == "__main__":
    main()
