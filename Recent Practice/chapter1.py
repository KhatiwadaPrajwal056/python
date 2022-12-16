'''

modules, comment and pips
# playing audio with external mudule
import subprocess    #Subprocess in Python is a module used to run new codes and applications by creating new processes. It lets you     start new applications right from the Python program you are currently writing.               
audio_file = "file path" 
return_code = subprocess.call(["afplay", audio_file]) 

# printing contents of a directory with module os,  this module provides the facility to establish the interaction between the user and the operating system
import os
print(os.listdir())     # gives the list of folders in the dir...

'''
#Packages: it is a container for many modules  
# its simple the taking datas from another directory using dot operator
from game import hero
hero.pubg()         #didnt work here , works on pycharm


























