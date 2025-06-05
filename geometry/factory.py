from geometry.circle import Circle
from geometry.triangle import Triangle


class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str, *args, **kwargs):
        if shape_type == "circle":
            return Circle(*args, **kwargs)
        elif shape_type == "triangle":
            return Triangle(*args, **kwargs)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")
