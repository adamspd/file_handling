#!/usr/bin/env python3
import sys, os, datetime
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
          "help: to have the possibility to know how each command works\n",
          "q: to quit\n"
          )
    com = input(": ")
    return com


com = menu()
while True:
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
    elif com == "date":
        filename = input("Name of the file: ")
        file_date(filename)
        com = menu()
    elif com == "t":
        directory = input("Name of the directory to list type of file from: ")
        type_file(directory)
        print()
        com = menu()
    elif com == "l":
        if not yes_or_no("Do you want to list a specific directory: "):
            print(list_directory())
            com = menu()
        else:
            directory = input("Name of directory or leave empty if current: ")
            print(list_directory(directory))
            com = menu()
    elif com == "help":
        helpme()
        com = menu()
    else:
        print("Unknown command ")
        sys.exit(0)
