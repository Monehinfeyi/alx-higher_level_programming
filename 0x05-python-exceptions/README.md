## 0x05. Python - Exceptions


## Requirements:

> Language: Python

> .Allowed editors: vi, vim, emacs

> .All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)

> .All your files should end with a new line

> .The first line of all your files should be exactly #!/usr/bin/python3

> .A README.md file, at the root of the folder of the project, is mandatory

> .Your code should use the pycodestyle (version 2.8.*)

> .All your files must be executable

> .The length of your files will be tested using wc


## Learning Objectives 👨‍💻

#### What you should learn from this project:


> Why Python programming is awesome

> What’s the difference between errors and exceptions

> What are exceptions and how to use them

> When do we need to use exceptions

> How to correctly handle an exception

> What’s the purpose of catching exceptions


> How to raise a builtin exception

> When do we need to implement a clean-up action after an exception

## TASKS

> 0. Safe list printing

Write a function that prints x elements of a list.

> 1. Safe printing of an integers list

Write a function that prints an integer with "{:d}".format().

> 2. Print and count integers

Write a function that prints the first x elements of a list and only integers.

> 3. Integers division with debug

Write a function that divides 2 integers and prints the result.

> 4. Divide a list

Write a function that divides element by element 2 lists.


> 5. Raise exception

Write a function that raises a type exception.

> 6. Raise a message

Write a function that raises a name exception with a message.

> 7. Safe integer print with error message

Write a function that prints an integer.

### .Prototype: def safe_print_integer_err(value):
.value can be any type (integer, string, etc.)
.The integer should be printed followed by a new line
.Returns True if value has been correctly printed (it means the value is an integer)
.Otherwise, returns False and prints in stderr the error precede by Exception:
.You have to use try: / except:
.You have to use "{:d}".format() to print as integer
.You are not allowed to use type()

> 8. Safe function
.Write a function that executes a function safely.

### Prototype: def safe_function(fct, *args):
.You can assume fct will be always a pointer to a function
.Returns the result of the function,
.Otherwise, returns None if something happens during the function and prints in stderr the error precede by Exception:
.You have to use try: / except:

> 9. ByteCode -> Python #4
.Create the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

> 10. CPython #2: PyFloatObject
.Create three C functions that print some basic info about Python lists, Python bytes an Python float objects.

> Python lists:

### Prototype: void print_python_list(PyObject *p);

.Format: see example
.If p is not a valid PyListObject, print an error message (see example)
. Python bytes:

### Prototype: void print_python_bytes(PyObject *p);
.Format: see example
.Line “first X bytes”: print a maximum of 10 bytes
.If p is not a valid PyBytesObject, print an error message (see example)
.Python float:

### Prototype: void print_python_float(PyObject *p);
.Format: see example
.If p is not a valid PyFloatObject, print an error message (see example)
.Read /usr/include/python3.4/floatobject.h
About:

> Python version: 3.4
.You are allowed to use the C standard library
.Your shared library will be compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
.You are not allowed to use the following macros/functions:

.Py_SIZE
.Py_TYPE
.PyList_Size
.PyList_GetItem
.PyBytes_AS_STRING
.PyBytes_GET_SIZE
.PyBytes_AsString
.PyBytes_AsStringAndSize
.PyFloat_AS_DOUBLE
.PySequence_GetItem
.PySequence_Fast_GET_SIZE
.PySequence_Fast_GET_ITEM
.PySequence_ITEM
.PySequence_Fast_ITEMS
.NOTE:

> The python script will be launched using the -u option (Force stdout to be unbuffered).
It is strongly advised to either use setbuf(stdout, NULL); or fflush(stdout) in your C functions IF you choose to use printf. The reason to that is that Pythonsprintand libCs printf don’t share the same buffer, and the output can appear disordered.

# AUTHOR:
> MONEHIN FEYISARA
