import subprocess


def open_log_file(filename):
    """
    This is our great new function which takes a passed-in
    filename, and uses a command prompt to open the file
    in notepad.
    """
    command = 'notepad "{file_to_open}"'.format(file_to_open=filename)
    subprocess.call(command, shell=True)  # a bad idea!


"""
Here, we demonstrate how to call our function in a safe
manner by using a real filename.
Remember, in the real world, we would be allowing
other people to pass in the filename...
"""
open_log_file("log.txt")
