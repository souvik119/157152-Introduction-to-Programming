# File statistics
# Reads a file based on the user input for the file name
# Display each line to the screen with a line number
# Prints statistics like Line Count and Character Count at the end of the program
# Program continues until user quits

def get_file_name():
    '''
    Prompts user to input file name to be read and returns the file name string
    '''
    file_name = input("Please enter name of file to be read (including extension): ")
    return file_name


def file_stat(file_name):
    '''
    - Reads the file name entered by the user
    - Displays each line to the screen with a line number
    - prints stats at the end of file read
    '''
    line_count = 0
    character_count = 0
    try:
        print('File contents below : ')
        f = open(file_name, 'r')
        for line in f:
            print(f'{line_count + 1} - {line}', end='')
            line_count += 1
            for character in line:
                character_count += 1
        print('\n')
        print('#########################################')
        print('File stats')
        print(f'Line count is : {line_count}')
        print(f'Character count is : {character_count}')
        print('#########################################')
        f.close()
    except:
        print(f'Error reading the file : {file_name}')


def file_reader():
    '''
    Starts the program and keeps continuing it till user user quits
    '''
    file_name = get_file_name()
    file_stat(file_name)
    while True:
        user_input = input('Enter q to quit or any other key to retry : ')
        if user_input == 'q' or user_input == 'Q':
            print('Thank you for using file reader. Bye!')
            exit()
        file_name = get_file_name()
        file_stat(file_name)


file_reader()
