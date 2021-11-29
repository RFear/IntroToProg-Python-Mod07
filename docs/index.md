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


### Program Explanation

### Additional Helpful Resources

## Structured Error Handling
### Program Example
### Program Execution
### Program Explanation
### Additional Helpful Resources

## Summary
In this page the concepts of pickling and structured error handling in python were discussed.  Programming example were provided along with demonstrations of their execution.  Descriptions of program execution were also included.  Additional resources to YouTube and other helpful web pages were also provided.  With the concept of pickling and structured error handling a newer python programmer can now work with serialized data as well as gain greater control over how their code deals with errors due to external inputs.
