class Employee:

    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

    def __repr__(self):
        """ Convert to formal string, for repr(). """

        return f"{__class__.__name__}({self.name})"

    def __str__(self):

        return f"{self.name - self.role}"
