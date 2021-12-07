#Hayden Covington

import getopt, sys
#import subprocess as sp
import os
import errno
import numbers

version = 1.0
DEBUG = False

full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]

def checkPath(fullPath):
    if os.path.exists(fullPath):
        doConversion(fullPath)
    else:
        print("\n ERROR: path not validated")

def doConversion(fullPath):
    print("Beginning conversion; this could take a while")

    allowedChars = { "," }

    #Change to 'with open'?
    #Make import easier somehow? GUI with drag-drop?
    inputfile = open(fullPath, "rb")
    outputfile = open("decoded_file", "w+b")

    #Character validation
    currentChar = inputfile.read(1)
    while currentChar!="":
        if currentChar.isdigit() or currentChar in allowedChars:
            outputfile.write("%c" % currentChar)
        else:
            if DEBUG: print("DEBUG: invalid char, discarding")
        currentChar = inputfile.read(1)

    inputfile.close()
    outputfile.close()

    with open('decoded_file') as secondPass:
        fullText = secondPass.read()
        spliced = fullText.split(",")
    with open('decoded_file', 'w+') as thirdPass:
        for i in range(len(spliced)):
            f = spliced[i]
            if f!="":
                thirdPass.write(str(f) + "\n")

    #Make a temp bash script to do some bash things since its eaiser than in python
    sc = open("printfile.sh", "w+")
    sc.write('#!bin/sh\n\nwhile read line\ndo\n\tprintf "%02x\\n" "$line"\ndone < "$1"') #Thanks to the person that taught me this :)
    sc.close()
    os.system("sh printfile.sh decoded_file > hexValues")

    #OS commands were simpler here too
    os.system("cat hexValues | xxd -p -r > DD_decoded_file")

    #Clean up
    os.system("rm printfile.sh")
    os.system("rm decoded_file")
    os.system("rm hexValues")

    print("ddDecode: conversion complete")

def main(argv):
    short_options = "f:"
    long_options = ["file"]
    try:
        arguments, values = getopt.getopt(argument_list, short_options, long_options)
    except getopt.error as err:
        print(str(err))
        sys.exit(2)
    for current_argument, current_value in arguments:
        if current_argument in ("-f","--file"):
            checkPath(current_value)

if __name__ == "__main__":
    main(sys.argv[1:])
