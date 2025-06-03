from _pytest.fixtures import fixture

pytest_plugins = ["pytester", "plugin"]
@fixture
def b():
    return 2


@fixture
def a():
    return 1