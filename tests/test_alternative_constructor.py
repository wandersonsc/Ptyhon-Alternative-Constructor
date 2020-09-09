

def test_employee_class(employee):

    assert employee.name == "Jack"


def test_str_method(employee):

    assert str(employee) == f"{employee.name} - {employee.role}"
    print(f"Class: {employee}")
