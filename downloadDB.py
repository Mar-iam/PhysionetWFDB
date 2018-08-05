#!/usr/bin/env python

'''
This python script intends to download Physionet datasets
and save the files into a certain folder based on user input

author  : Mariam
date    : 25072018

'''

import os
import wfdb

def getDBList():
    # Retreive a list of available databases in Physionet
    dbs = wfdb.get_dbs()
    return dbs

def validateDB(name):
    dbs = getDBList()
    found = any(name in sublist for sublist in dbs)

    return found

def downloadDB(name):
    # Download WFDB record of Normal Sinus Rhythm of RRI DB
    path = (os.getcwd() + '\\' + name)
    if os.path.exists(path):
        return name + " is already exist"
    else:
        wfdb.dl_database(name,path)
        return "Done"

if __name__ == '__main__':
    while(True):
        print("Insert a number based on your desired output:")
        print("[1]: Display a list of available Databases in Physionet\n"
              "[2]: Download a certain database by providnig DB code\n"
              "[3]: Terminate")

        keyInput = input()

        if keyInput == "1":
            dbs = getDBList()
            for line in dbs: print(line)

        elif keyInput == "2":
            dbName = input("Enter the code of the DB to be downloaded ")
            if(validateDB(dbName)):
                msg = downloadDB(dbName)
                print(msg)
            else:
                print("You have entered an invalid DB code")

        elif keyInput == "3":
            print("Terminating the program")
            break

        else:
            print("You have entered an invalid input")
