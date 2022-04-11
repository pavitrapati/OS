#Experiment 9

import os

parent_dir = "D:\\KARUNYA\\sem4\\OS\\lab\\exp9\\"


def create_dir_and_file():
    s = input("Enter the name of the directory: ")
    path = os.path.join(parent_dir, s)
    os.mkdir(path)
    filename = input("Enter the name of the file: ")
    filepath = path + "/"
    for i in range(5):
        temp = filename + "_" + str(i)
        f = open(filepath + temp, "x")
        temp = ""
    return path


def search_file(dirpath):
    global flag
    query = input("Enter name of the file to be searched: ")
    dirlist = os.listdir(dirpath)
    for i in dirlist:
        if i == query:
            flag = True
            break
        else:
            flag = False
    if flag:
        print("File Exists!")
    else:
        print("File does not exist")


def display(dirpath):
    dirlist = os.listdir(dirpath)
    for i in dirlist:
        print(i, end=" ")


def delete(dirpath):
    global search
    search = input("Enter path of the file to be Deleted: ")
    dirlist = os.listdir(dirpath)
    dirlist = sorted(dirlist)
    for i in dirlist: print(i, end=" ")
    print()
    os.remove(search)
    dirlist = os.listdir(dirpath)
    dirlist = sorted(dirlist)
    for i in dirlist: print(i, end=" ")


while True:
    n = int(input("\nChoose the Function:\n1. Create File\n2. Search File\n3. Display Files\n4. Delete file\n5. Exit"))
    if n == 1:
        dirpath = create_dir_and_file()
    elif n == 2:
        search_file(dirpath)
    elif n == 3:
        display(dirpath)
    elif n == 4:
        delete(dirpath)
    else:
        break