# Assignment 4:
# Module 5: Files, Exceptions, and Errors in Python
# Task 1: Read a File and Handle Errors

try:
    print ('Reading file content:')
    with open('sample.txt', 'r') as file:
        i = 1
        for line in file:
            if len(line.strip()) > 0:
                print ('Line ' + str(i) + ': ' + line.strip())
                i+=1
except FileNotFoundError:
    print ('Error: The file sample.txt was not found.')
except IOError:
        print ('Error: Unexpected error. Could not read the file.')
