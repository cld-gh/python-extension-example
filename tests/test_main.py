import python_extension_example as m


def test_version():
    assert m.__version__ == 'dev'


def test_add():
    assert m.add(1, 2) == 3


def test_subtract():
    assert m.subtract(1, 2) == -1


def test_multiply():
    assert m.multiply(5, 7) == 35
