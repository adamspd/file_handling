#!/usr/bin/env python3


""" Module to help arrange file, move files to the right directory, create directories,
see all information about a file
"""

import os
import datetime
import sys

YES = ["yes", "y", "oui", "o", "1"]


def yes_or_no(invite):
    """By default all non-understandable answer means NO"""
    try:
        return input(invite).lower() in YES
    except:
        return False


def create_file(filename):
    comment = input('Write a short comment to put in the script. Must begin with "#": ')
    # Checking if file already exists
    if not os.path.exists(filename):
        try:
            # if file doesn't exist, try to create it and write the comment inside of it
            with open(filename, "w") as f:
                f.write(comment)
            filesize1 = os.path.getsize(filename)
            print("Creating file named {} successful! Size: {}".format(filename, filesize1))
        except:
            # if any exception is raised, abortion !
            print("Cannot create file named {} !".format(filename))
    else:
        # if file already exist, tell the user
        print("File named {} already exists, try another name !".format(filename))
    return_ = filename + " Size: " + str(os.path.getsize(filename)) + " bytes"
    return return_


def file_size(filename):
    if os.path.exists(filename):
        try:
            return str(os.path.getsize(filename)) + " bytes"
        except:
            print("Cannot calculate the size of {} !".format(filename))
    else:
        print("{} doesn't exist !".format(filename))
        return False


def remove_file(filename):
    if os.path.exists(filename):
        if yes_or_no("Do you want to delete this file?: "):
            try:
                os.remove(filename)
                print("{} succesfully deleted! ".format(filename))
                return True
            except:
                print("Can't delete {}! ".format(filename))
    else:
        print("{} doesn't exist! ".format(filename))
        return False


def new_directory(directory):
    # Before creating a new directory, check to see if it already exists
    if not os.path.isdir(directory):
        try:
            os.mkdir(directory)
            print("{} successfully created !".format(directory))
            return directory
        except:
            print("Cannot created {} !".format(directory))
    else:
        print("{} already created !".format(directory))
        return False


def list_directory(directory=None):
    try:
        return os.listdir(directory)
    except:
        print("Cannot listed file and subdirectories !")


def type_file(directory):
    list_ = list_directory()
    for name in list_:
        fullname = os.path.join(directory, name)
        if os.path.isdir(fullname):
            print("{} is a directory".format(fullname))
        else:
            print("{} is a file".format(fullname))


def file_date(filename):
    timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    date = datetime.datetime.fromtimestamp(timestamp)
    # Return just the date portion
    return "{:%Y-%m-%d}".format(date)
