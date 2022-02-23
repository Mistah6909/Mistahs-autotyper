import sys
import os
import platform
os1 = platform.system()
#these if statements check to see what os is running since shell command syntax is dependent on OS 
if os1 == "Linux": 
  os.system("python -m pip install whl pynput 1.7.6")
elif os1 == "Windows":
  os.system("py -m pip install whl pynput 1.7.6")
elif os1 == "MacOS":
  os.system("py - m pip install whl pynput 1.7.6")
  
  
 print("pynput has succesfully been installed on your computer!")
