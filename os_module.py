"""
This is a doc string

>>> import os_module
>>> os_module.__doc__

prefix with r to make \n as raw string.

"""

#module
import os
print(os.listdir())

#intraspection
#print(dir(os))

#path to module
print(os.__file__)
print(os.__doc__)

#import datetime
#print(dir(datetime))
#print(datetime.time())
#from command line pip install glob2
#import glob2
#print(glob2.glob("*.py"))
