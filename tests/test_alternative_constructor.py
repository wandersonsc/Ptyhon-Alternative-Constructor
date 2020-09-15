from alternative_constructor import Employee


def test_employee_class(employee):

    assert employee.name == "Jack"


def test_str_method(employee):

    assert str(employee) == f"{employee.name} - {employee.role}"
    print(f"Class: {employee}")


def test_create_employee_from_json():

    data = [
        {
            "name": "Jack Jr.",
            "email": "jackjr@gmail.com",
            "role": "IA guru"
        },
        {
            "name": "John",
            "email": "john@gmail.com",
            "role": "Dev OP"
        },
        {
            "name": "Dr. Juliane",
            "email": "juliane@gmail.com",
            "role": "Python genius"
        }
    ]
    employee = Employee.from_json_create_employee(data)

    assert employee[0].name == data[0]['name']

    # I am going to leave it here, just in case you are curious how I went about to find those index

    print(F"This is the employee name: {employee[1].name}")
    print(F"This is from json file: {data[1]['name']}")
