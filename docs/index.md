# Pickling and Structured Error Handling
**Dev:** *RFear*
**Date:** *11.28.2021*

## Introduction
This page will discuss the concept of pickling in python.  Structured error handling and using exception classes will also be discussed.  Each of these items are discussed in their respective sections.  Each section defines the concept, provides a programming example, a description of what is occurring within the programming example, and additional resources that may be helpful.  Understanding these core python principals are essential to a beginning python programmer.

## Pickling
In python pickling refers to serializing and de-serializing python objects to a file.  Python objects which can be pickled include list, dictionaries, etc.  One example of why this is useful is that a pickled python object can be open a reconstructed in another python script.  For example, say one colleague is running an experiment and collecting a lot of data.  They could “pickle” the data and send it to other colleagues who could run analyses on the data set.

### Program Example
```
import pickle

# Variables for pickling
pickle_list = ["a", "b", "c"]
pickle_dict = {"firstname": ["Bob", "Ryan", "Michael"],
               "lastname": ["Smith", "Fear", "Jones"],
               "Age": [50, 30, 27]}
pickle_int = 10
pickle_flt = 25.5
pickle_bool = True
pickle_items = [pickle_list, pickle_dict, pickle_int, pickle_flt, pickle_bool]
pfname = "pickle_file.txt"

print("\n***** The following is an example of how to pickle and read data from a pickled file *****\n")
# Save data to a pickled file
pickle_file = open(pfname, "wb")
pickle.dump(pickle_items, pickle_file)
pickle_file.close()

print("The following variables have been stored into a collector variable 'pickle_items' "
      "and saved to the file 'pickle_file.txt'.\n")
print(f"\tpickle_list: {pickle_list}")
print(f"\tpickle_dict: {pickle_dict}")
print(f"\tpickle_int: {pickle_int}")
print(f"\tpickle_flt: {pickle_flt}")
print(f"\tpickle_bool: {pickle_bool}")
print(f"\tpickle_items: {pickle_items}\n")
print("The pickled file has been closed.\n\n")

# Read and print unpickled data
print("The pickled file is now opened and the contents are read into a new variable 'data'.")
pickle_import = open(pfname, "rb")
data = pickle.load(pickle_import)
print(f"The contents of the variable 'data':\n{data}\n")
print("The item of each element in 'data':")
for item in data:
    print(f"Variable type: {type(item)} and contents: {item}")
```
*Pickling Example in Python*

### Program Execution
The program execution in the PyCharm environment is shown in Figure 1.
![Program Execution of Pickling - PyCharm](/docs/images/pickling_pycharm.png "Program Execution of Pickling - PyCharm")
Figure 1: Program Execution of Pickling - PyCharm

The program execution in the PyCharm environment is shown in Figure 2.
![Program Execution of Pickling - Command Window](/docs/images/pickling_cmd.png "Program Execution of Pickling - Command Window")
Figure 2: Program Execution of Pickling - Command Window

### Program Explanation
First, I import the pickle module.  Next I define a list, dictionary, integer, floating point, and a Boolean then collect all of these items in a list called pickle_items.  I then save this data to a file called “pickle_file.txt”.  The contents of this file are shown in Figure 3, the data is written to the file in binary.  Although humans may not be able to fully understand the content in this file, it is perfectly useable by the computer.  I also print to the screen what has been accomplished.

![Content in pickle_file.txt](/docs/images/pickling_file.png "Content in pickle_file.txt")
Figure 3: Content in *pickle_file.txt*

Next the file “pickle_file.txt” is read into the program.  Note, in this example the data exported was in a list, so when I read in the information, the variable data is a list with all of the contents from the variable pickle_items.  To prove this, I print out the data to the screen.

### Additional Helpful Resources
A YouTube video and two web pages that discuss the topic of pickling in python further are included below.

[YouTube video about pickling](https://www.youtube.com/watch?v=2Tw39kZIbhs)

[DataCamp info about Pickle in Python](https://www.datacamp.com/community/tutorials/pickle-python-tutorial)

[GeeksForGeeks info about Understanding Python Pickling](https://www.geeksforgeeks.org/understanding-python-pickling-example/)

## Structured Error Handling
It is common that when a program is interacting with a user errors will occur.  When errors occur, and are not handled, the program could stop executing and the user is left frustrated that they cannot use your code.  One way to deal with errors is structured error handling.  This is commonly dealt with what is called a “try-exception” block of code.  The logic for this block of code is shown in Figure 4.  Note, there are additional ways to handle errors by including “else” and “finally” blocks of code and Figure 4 describes what happens if these are used.

![Try-Except Code Block Logic](/docs/images/strut_error_handling_logic.png "Program Execution of Pickling - Command Window")
Figure 4: Try-Except Code Block Logic

### Program Example
```
# Variables for structured error handling
xInt = 10
xStr = "hello"
xLst = [0, 1, 2, 3]
fname = "mydata.txt"

print("\n\n\n***** The following four examples of how to handle some common errors *****\n")

# handle a ZeroDivisionError
print("Here I will try to divide by 0 raising a ZeroDivisionError")
try:
    y = xInt / 0
except ZeroDivisionError as e:
    print("My custom error message: ")
    print("\tCannot divide by zero.")
    print("This is what Python might say:")
    print(f"\t{e}: {e.__doc__}\n")

# handle a TypeError
print("\nHere I will try to add the integer 5 to a string raising a TypeError")
try:
    y = xStr + 5
except TypeError as e:
    print("My custom error message: ")
    print("\tCannot add a string and an integer.")
    print("This is what Python might say:")
    print(f"\t{e}: {e.__doc__}\n")

# handle a IndexError
print("\nHere I will try to index an element in a list that doesn't exist raising an IndexError")
try:
    y = xLst[5]
except IndexError as e:
    print("My custom error message:")
    print("\tCannot index an element outside of list.")
    print("This is what Python might say:")
    print(f"\t{e}: {e.__doc__}\n")

# handle FileNotFoundError
print("\nHere I will try to open a non-existing file raising a FileNotFoundError")
try:
    f = open(fname, "r")
except FileNotFoundError as e:
    print("My custom error message:")
    print("\tCannot find file. Or file does not exist.")
    print("This is what Python might say:")
    print(f"\t{e}: {e.__doc__}\n")
else:
    print("Successfully read file.")  # This line will execute if there are no exceptions
finally:
    print("Made it to this line.")  # This line will execute regardless if there is an error
```
### Program Execution
The program execution in the PyCharm environment is shown in Figure 5.
![Program Execution of Structured Error Handling - PyCharm](/docs/images/struct_error_hand_pycharm.png "Program Execution of Structured Error Handling - PyCharm")

Figure 5: Program Execution of Structured Error Handling - PyCharm

The program execution in the PyCharm environment is shown in Figure 6.
![Program Execution of Structured Error Handling - Command Window](/docs/images/struct_error_hand_cmd.png "Program Execution of Structured Error Handling - Command Window")

Figure 6: Program Execution of Structured Error Handling - Command Window

### Program Explanation
For the example I begin by defining some variables that will be used.  In the next four try-exception blocks I show common exceptions that are raised, a custom error message, and the message python may print out.  The four exceptions are ZeroDivisionError, TypeError, IndexError, and FileNotFoundError.

First, I show an example of dividing by zero.  If a program is performing arithmetic and this situation occurs this exception can be raised and another option could be entered.  Next, I show an example of a type error.  This can occur when you are trying to perform arithmetic with two different variable types such as a string or an integer.  Next, I show an example of an IndexError, this can occur when trying to access an element of a list or dictionary that doesn’t exist.  Finally, I show an example of trying to access a file that doesn’t exist.

Note, with the FileNotFoundError the “else” and “finally” blocks are used.  As Figure 4 indicates, the “else” block executes when no exceptions are raised and the “finally” block will always execute.  I will now create the file “mydata.txt”, notice the change in Figure 7 from Figure 6.  Since the file “mydata.txt” now exist the else block executes.

The program execution in the PyCharm environment is shown in Figure 7.
![Else/Finally Execution](/docs/images/struct_error_hand_cmd2.png "Else/Finally Execution")

Figure 7: Else/Finally Execution

### Additional Helpful Resources
A YouTube video and two web pages that discuss the topic of structured error handling further are included below.

[YouTube video about Exceptions in Python](https://www.youtube.com/watch?v=nlCKrKGHSSk)

[DataCamp info about Exception and Error Handling in Python](https://www.datacamp.com/community/tutorials/exception-handling-python)

[W3Schools info about Python Try Except](https://www.w3schools.com/python/python_try_except.asp)

## Summary
In this page the concepts of pickling and structured error handling in python were discussed.  Programming example were provided along with demonstrations of their execution.  Descriptions of program execution were also included.  Additional resources to YouTube and other helpful web pages were also provided.  With the concept of pickling and structured error handling a newer python programmer can now work with serialized data as well as gain greater control over how their code deals with errors due to external inputs.
