import subprocess


def open_log_file(filename):
    command = 'notepad "{file_to_open}"'.format(file_to_open=filename)
    subprocess.call(command, shell=True)  # a bad idea!


"""
Now we see what happens if a malicious user passes in a command which not
only makes it look like we've innocently opened a file, but covertly logs
information about our filesystem..."""
open_log_file(r'log.txt" & dir C:\windows > C:\temp\hacky_stuff.txt')

#  What if 'dir C:\windows' was replaced by 'del C:\windows /f /s /q'???
