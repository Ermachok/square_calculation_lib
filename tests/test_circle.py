import pytest

from geometry.circle import Circle


@pytest.fixture
def unit_circle():
    return Circle(radius=1)


def test_circle_area(unit_circle):
    assert unit_circle.area() == pytest.approx(3.1416, 0.001)


@pytest.mark.parametrize(
    "radius, expected_area",
    [
        (0, 0),
        (1, 3.1416),
        (2.5, 19.6349),
    ],
)
def test_circle_area_param(radius, expected_area):
    c = Circle(radius=radius)
    assert c.area() == pytest.approx(expected_area, 0.001)


def test_circle_negative_radius():
    with pytest.raises(ValueError):
        Circle(radius=-3)
