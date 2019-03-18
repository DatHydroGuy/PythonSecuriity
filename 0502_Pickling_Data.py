"""
Pickling uses it's own pseudo-language to represent the data being serialised so that it can handle more complex
structures.  Unfortunately, it is possible to write malicious files which when un-pickled, lead to arbitrary code
execution.  This is why all articles about the pickle library are accompanied by warnings.
More info here:
https://media.blackhat.com/bh-us-11/Slaviero/BH_US_11_Slaviero_Sour_Pickles_WP.pdf
https://media.blackhat.com/bh-us-11/Slaviero/BH_US_11_Slaviero_Sour_Pickles_Slides.pdf
"""
import pickle

my_file = "pickle_file.dat"
# my_file = "pickle_file_bad.dat"
with open(my_file, 'rb') as reader:
    my_data = pickle.load(reader)

print(my_data)
