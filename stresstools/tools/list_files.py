import glob, os

def simple_function(path_folder):
    list_file = []
    for file in glob.glob(path_folder):
        list_file.append(file)
    return(list_file)