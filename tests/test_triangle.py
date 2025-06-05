import pytest
from geometry.triangle import Triangle


@pytest.fixture
def right_triangle():
    return Triangle(a=3, b=4, c=5)


def test_triangle_area(right_triangle):
    assert right_triangle.area() == pytest.approx(6.0, 0.001)


def test_triangle_is_right(right_triangle):
    assert right_triangle.is_right()


def test_invalid_triangle_raises():
    with pytest.raises(ValueError):
        Triangle(a=1, b=2, c=10)


@pytest.mark.parametrize("a,b,c", [
    (-1, 2, 3),
    (2, -1, 3),
    (2, 3, -1),
])
def test_triangle_negative_sides_raise(a, b, c):
    with pytest.raises(ValueError):
        Triangle(a=a, b=b, c=c)


@pytest.mark.parametrize("a,b,c,is_right", [
    (3, 4, 5, True),
    (5, 12, 13, True),
    (7, 24, 25, True),
    (6, 6, 6, False),  # равносторонний
    (2, 3, 4, False),  # остроугольный
])
def test_triangle_is_right_param(a, b, c, is_right):
    t = Triangle(a, b, c)
    assert t.is_right() == is_right
