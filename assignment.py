def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    # pass  My name is Alice and I am 30 years old
    return f"My name is {name} and I am {age} years old"
    # "My name is John and I am 25 years old"

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    # pass
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    # pass
    total = 0
    for i in range(1,n+1):
        total+=i
    return total

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    # pass
    return (sum(numbers),max(numbers),min(numbers))

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    #  pass
    return [name for name,score in students_dict.items() if score > 80 ]
    # for name,score in students_dict.items():
    #     if score>80:
    #         return name

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    # pass
    return set(list1).intersection(list2)

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    # pass
    return {
        "sum":a+b,
        "difference":a-b,
        "product":a*b,
        "quotient":a/b if b!=0 else "undefined"
    }

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    # pass
    return {
        "and": x and y,
        "or": x or y,
        "not": not x,
        "not y": not y
    }


def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    # pass
    return {
        "and":a&b,
        "or":a|b,
        "xor":a^b,
        "not a":~a,
        "not b":~b    
    }

# Call to functions

""" print(format_string("Abubakar",30))

print(conditional_check(22))

print(loop_sum(10))

number=[1,2,3,4,5]
print(list_operations(number))

student_dict ={
    "Abubakar":99,
    "Omar":80,
    "Yussuf":69
}
print(dict_operations(student_dict))

list1=[1,3,5,7,8]
list2=[4,1,8,1,0]
print(set_operations(list1,list2))

a=4.0
b=2.0
print(arithmetic_ops(a,b))

x=True
y=False
print(logical_ops(x,y))

a=4
b=2
print(bitwise_ops(a,b)) """