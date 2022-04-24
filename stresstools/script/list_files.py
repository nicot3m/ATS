import glob, os

from pathlib import Path

def function_to_run():
    path = "C:\Users\nicot\NICO\INFO\TEST_STRESSTOOLS\"
    list_file = []

    for file in glob.glob(path):
        list_file.append(file)

    print("list_file", list_file)
    
    return list_file
