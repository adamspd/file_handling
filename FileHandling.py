#!/usr/bin/env python3
import sys
from FunctionForFileHandling import *


# Menu
def menu():
    print(" Command ".center(20, "*"))
    print(" c: to create new file\n",
          "d: to create a new directory\n",
          "del: to delete a file\n",
          "l: to list a directory\n",
          "date: to print modified date of a file\n",
          "t: to list the type of file in a directory\n",
          "q: to quit\n"
          )
    com = input(": ")
    return com


com = menu()
while com != "q":
    if com == "c":
        filename = input("Name of the file: ")
        create_file(filename)
        com = menu()
    elif com == "d":
        directory = input("Name of the directory: ")
        new_directory(directory)
        com = menu()
    elif com == "del":
        filename = input("Name of the file to delete: ")
        remove_file(filename)
        com = menu()
    else:
        print("Unknown command ")
        sys.exit(0)
