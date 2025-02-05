# Used to define Global variables
import pytest
import source.shapes as shapes

@pytest.fixture
def my_global_rectangle():
    return shapes.Rectangle(10, 20)


@pytest.fixture()
def wierd_global_rectangle():
    return shapes.Rectangle(5, 6)

