# Introduction

The following is a decorator that can be used to provide parameter checking to
methods and classes.  

This decorator would not be possible without the inspiration of the following:

* [So you want to be a Python expert? by James Powell](https://www.youtube.com/watch?v=cKPlPJyQrt4)
* [Pre/Post-Condition Decorator Example](https://wiki.python.org/moin/PythonDecoratorLibrary#Pre-.2FPost-Conditions)
* [Andrew P accepts decorator](https://github.com/andrewp-as-is/accepts.py)

The above inspired me to create this decorator to reduce the clutter of my code. 

Even thou the accepts decorator already checks for the type.  It is somewhat limited
because it expects the exact number of parameters of the method.  It forces the users
to decorator all of the parameters instead of the ones that one wanted check.  This 
limitation has been removed for this decorator.

## Objective

To allow for a wide range of parameter checking that can be used by
anyone without having to include the parameter checks within the calling method.
This will allow someone to provide cleaner code for the implemented method while
adding some complexity to the decorator.

## Features

The decorator provides the ability for a user to check a parameter for type and/or
value expectation.  This also includes checking the return value of a given method
call.

The decorator is used by using the contract decorator with your method.  The decorator
will expect the following syntax:

```python
    import contract

    @contract({
        'a': [checktype(float), closed(0.0, 1.0)],
        'b': [checktype(int), gteq(1)],
        'c': [checktype(int), gteq(1)]
    })
    def __init__(self,a, b, c, d):

```

The above will check that the a parameter is of type float and is between 0.0 and 1.0.
The b is checked that is it an integer and is greater than of equal to 1.  The same for
that parameter c.  While the parameter d does not required any contract requirement.

The following table contains the different options that the can be used with this decorator.

| Name | Parameters | Type | Description |
|---|---|---|---|
| validvalues | tuple | Value Check | Checks that the parameter value is part of the tuple |
| checktype | type | Type Check | Checks if the parameter is an instance of the expected type |
| closed | a,b such that a <= b | Closed Range Check | Checks if the value is between two values including a and b |
| opened | a,b such that a < b | Opened Range Check | Checks if the value is between two values excluding a and b |
| closedopened | a,b such that a < b | Closed/Opened Check | Checks if the value is between two values including a |
| openedclosed | a,b such that a < b | Opened/Closed Check | Checks if the value is between two values including b | 
| gt | a | Value Check | Checks that the parameter value is greater than a | 
| lt | a | Value Check | Checks that the parameter value is less than a |
| gteq | a | Value Check | Checks that the parameter value is greater than or equal to a | 
| lteq | a | Value Check | Checks that the parameter value is less than or equal to a |

## Examples

The following example offers some ways that this decorator can be used within
someone code.

### Type Check.

The following code shows how you can check that a given parameter is of a given type.

```python
    import contract

    @contract({
        'a': [checktype(float)]
    })
    def m(a):

```

The above will determine if the passed value a is a float type.

### Range Checks

The following contains the different range checks that can be applied. 

```python
    import contract

    @contract({
        'a': [closed(0, 1)],
        'b': [gteq(2)],
        'c': [gt(3)],
        'd': [lt(4)],
        'e': [lteq(5)],
        'f': [opened(10.0, 11.0)],
        'g': [closedopened(12, 13)],
        'h': [openedclosed(14, 15)],
    })
    def range_check(self,a, b, c, d, e, f, g, h):

```

The above will then perform the expected checks for each of the parameters.

Note that the above checks are not restricted to the primitive values but can be 
any class that implements the different range checks methods of the Data Model. 
You can then use the Range checks with a users defined class that implements 
the __lt__, __le__, __gt__, and __ge__ methods.
  
### Tuple Check

```python
    @contract({
        'a': [validvalues(set('blue','green','red'))]
    })
    def contains(a,b):

```

The above example will insure that the parameter a will be to set to one of the
values, 'blue', 'green' or 'red'.

### Return Value Check

```python
    @contract({
        None: [gt(101)]
    })
    def contains(a,b):

```

The aboue check will determine that the return value is greater than 100.  Note
that you need to specific that the parameter name is None.  This is how we 
associate the check to the return value.
