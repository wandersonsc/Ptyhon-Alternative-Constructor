class Employee:
    """ Model representation of the Employee class"""

    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

    def __repr__(self):
        """ Convert to formal string, for repr(). """

        return f"{__class__.__name__}({self.name})"

    def __str__(self):
        """  string (representation) """

        return f"{self.name} - {self.role}"

    @classmethod
    def from_json_create_employee(cls, data):
        """ Custom class method that's allow you to create Employee instances from a Json file"""

        employees = []

        for row in data:
            employee = cls(row['name'], row['email'], row['role'])
            employees.append(employee)
        return employees
