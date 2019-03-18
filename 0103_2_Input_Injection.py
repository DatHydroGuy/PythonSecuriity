import subprocess


# Fix 2: Don't use shell=True in your subprocess calls
def open_log_file(filename):
    command = 'notepad "{source}"'.format(source=filename)
    print(command)
    subprocess.call(command)


open_log_file("log.txt")
# open_log_file(r'log.txt" & dir C:\windows > C:\temp\hacky_stuff.txt')

"""
Notes:
The subprocess parameter shell=True invokes the process using an intermediate shell / command prompt from the host
operating system.  This means that the first parameter becomes a command to execute, and the rest of the parameters
are arguments to the shell program itself.  This is what makes it so dangerous.
Removing the shell=True parameter means that the entire parameter list are the command to execute.  So in our case,
Notepad will not only open the file, but it will attempt to make sense oof the rest of the input and fail silently
(because notepad cannot execute a 'dir' command).
"""
