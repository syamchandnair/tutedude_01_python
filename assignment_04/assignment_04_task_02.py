# Assignment 4:
# Module 5: Files, Exceptions, and Errors in Python
# Task 2: Write and Append Data to a File

try:
    # writing to the file
    input_text = input('Enter text to write to the file: ')
    file = open('output.txt', 'w')
    f_write = file.write(input_text + '\n')
    print ('Data successfully written to output.txt.\n')
    file.close()

    # appending additional text
    input_text = input('Enter additional text to append: ')
    file = open('output.txt', 'a')
    f_write1 = file.write(input_text + '\n')
    print ('Data successfully appended.\n')
    file.close()

    # reading contents.
    file = open('output.txt', 'r')
    f_read = file.read()
    print ('Final content of output.txt:')
    print(f_read)
    file.close()

except IOError:
        print ('Error: Unexpected IO error. ')
