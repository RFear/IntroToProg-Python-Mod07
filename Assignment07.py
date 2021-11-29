# ------------------------------------------------#
# Title: Pickling, Errors, and Exemption Handling.
# Desc: This script will demonstrate how pickling
#       works as well as structured error handling.
# Change Log:
# RFear, 2021-11-28, Created Script
# ------------------------------------------------#

# ------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------ #
# An example of how to use pickling.
# ------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------ #

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


# ------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------ #
# An example of how to work with errors and handle exemptions.
# ------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------ #

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
