from alternative_constructor import Employee


def test_employee_class(employee):

    assert employee.name == "Jack"


def test_str_method(employee):

    assert str(employee) == f"{employee.name} - {employee.role}"
    print(f"Class: {employee}")


def test_create_employee_from_json():

    data = {
        "name": "Jack Jr.",
        "email": "jackjr@gmail.com",
        "role": "IA guru"
    }
    employee = Employee.from_json_create_employee(data)

    assert employee.name == data['name']
