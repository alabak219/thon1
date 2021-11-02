import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("YES! We have a match!")
else:
    print("No match")


import os

def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print ()

current_path()

os.chdir('../.')

current_path()








