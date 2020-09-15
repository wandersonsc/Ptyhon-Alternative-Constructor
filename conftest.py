import pytest
from alternative_constructor import Employee


@pytest.fixture(scope='module')
def employee():

    employee = Employee('Jack', 'jack@awesometech.com', 'Software Engineer')
    return employee
