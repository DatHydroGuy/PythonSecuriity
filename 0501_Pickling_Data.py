"""
Pickling is the term used to describe serialisation of data using python's pickle library.
It creates a binary representation of the objects being pickled and writes them to the specified filename.
"""
import pickle

my_data = "This is my test data"

my_file = "pickle_file.dat"
with open(my_file, 'wb') as writer:
    pickle.dump(my_data, writer)
