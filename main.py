import logging

from geometry.factory import ShapeFactory

logging.basicConfig(level=logging.INFO)


def main():
    shapes = [
        ShapeFactory.create_shape("circle", radius=3),
        ShapeFactory.create_shape("triangle", a=3, b=4, c=5),
    ]

    for shape in shapes:
        print(shape.area())


if __name__ == "__main__":
    main()
