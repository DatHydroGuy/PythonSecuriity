# Temporary files
#
# ISSUE
# Do not use mktemp()
# It does not safeguard the temporary file being made, and you may be vulnerable to:
# 1) Writing your data into the wrong file and exposing your data
# 2) Reading the wrong (possibly malicious) data into your application
#
# FIX
# Use the mkstemp method within the tempfile module


# Not patching your Python runtime
#
# ISSUE
# Since “Python”, ie CPython is written in C, there are times when the Python interpreter
# itself has holes. Common security issues in C are related to the allocation of memory,
# and buffer overflow errors.
# CPython has had a number of overrun or overflow vulnerabilities over the years, each of
# which have been patched and fixed in subsequent releases.
# Here is an example of an integer overflow vulnerability which enables arbitrary code
# execution:
# https://www.cvedetails.com/cve/CVE-2017-1000158/
# It affects all Python versions from 2.7.13 and below.
#
# FIX
# Use Python 3 and ensure you patch your runtime!


# Not patching your Python dependencies
#
# ISSUE
# It is common to "pin" versions of Python packages into your applications because "these
# are the versions which work".  Sound familiar?
# All of the vulnerabilites discussed can occur in packages that your application uses. The
# developers of these packages fix security issues constantly, and you are expected to do
# the same for the applications / packages / solutions you create.
#
# FIX
# Use a service like https://pyup.io/ to check for vulnerabilites and updates.  Raise and
# merge pull requests to your application and re-run your unit tests to ensure no
# functionality has been broken.  This will help to keep you packages uo-to-date.
# Also, you can use a tool like InSpec (https://www.inspec.io/) to validate the installed
# versions of your packages on a production environment.  This way, you can write rules to
# force upgrades of packages with known vulnerabilities.


# Bandit
#
# Bandit is a static code linter which can be used to catch many known code issues and
# vulnerabilities.  Consider building it into your CI/CR/CD pipeline.
