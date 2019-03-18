import subprocess
import shlex


# Fix 1: Use shlex to split and securely quote your inputs
def open_log_file(filename):
    try:
        parsed_filename = shlex.split(filename)
        command = 'notepad "{file_to_open}"'.format(file_to_open=shlex.quote(parsed_filename[0]))  # Note the [0]!
        print(command)
        subprocess.call(command, shell=True)
    except ValueError as ve:
        print('Error processing input: {0}'.format(ve))


open_log_file("log.txt")
# open_log_file(r'log.txt" & dir C:\windows > C:\temp\hacky_stuff.txt')
# open_log_file(r'"log.txt" & dir C:\windows > C:\temp\hacky_stuff.txt')

"""
Notes:
Shlex splits the input and re-quotes it for us.  This negates input injection attacks which attempt to chain
malicious commands together.
We use filename[0] at line 9, because shlex will have split the input for us, and we're only interested in opening
the filename passed in.  It is reasonable to assume that this would be the first (and only) parameter.
"""
