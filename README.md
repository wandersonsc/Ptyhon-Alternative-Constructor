[![Build Status](https://travis-ci.org/wandersonsc/Ptyhon-Alternative-Constructor.svg?branch=master)](https://travis-ci.org/wandersonsc/Ptyhon-Alternative-Constructor)

[![codecov](https://codecov.io/gh/wandersonsc/Ptyhon-Alternative-Constructor/branch/master/graph/badge.svg)](https://codecov.io/gh/wandersonsc/Ptyhon-Alternative-Constructor)

# Python Alternative Constructor

### Class Methods and Alternative Constructor.

Well, let see you want to implement an independent "constructors", so how to we go about to create one? And that's when the decoretor `@classmethod` comes into the picture, We normaly add them as a class methods, which does not call the default constructor `__init__` whatsoever!

```python
   @classmethod
   def from_json_create_employee(cls, data):

       # List Comprehension
       return [cls(row['name'], row['email'], row['role']) for row in data]
```

If you look close you will notice, that I am taking in two arguments the class `cls` and `data`, again I am taking in `cls` not `self`.
As the Python documentation said:

> A class method receives the class as implicit first argument, just like an instance method receives the instance. To declare a class method, use this idiom:

```python
 class C:

    @classmethod
    def f(cls, arg1, arg2, ...): ...
```

### Setup

1. Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python` to start Python):

```

pip3 install -r requirements.txt

```

### This project includes:

1. Class Methods
2. Pytest
3. Tracis CI

```

```
