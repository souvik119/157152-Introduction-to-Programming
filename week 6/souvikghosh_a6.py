# Multiplication table printer
# Accepts an integer input from user between (1-100) and prints its multiplication table up to user
# specified index
# first function accepts input from user
# second function prints multiplication table
def accept_input():
    '''Accepts user input for a integer between 1-100
    Returns:
    integer number that user input
    index up to which table is to be printed
    '''
    print("###################Multiplication table###################")
    user_inp = int(input("Enter an integer between 1-100 : "))
    user_index = int(input("Enter index up to which table is to be printed from 1-10 : "))
    return user_inp, user_index


def print_table(user_inp, user_index):
    '''Prints multiplication table up to user defined index (1-10) for input input
    Args:
    user_inp : number to print multiplication table
    user_index : index up to which table is to be printed from 1-10
    '''
    print("Multiplication table for the number entered : ")
    for i in range(1, user_index+1):
        print(f'{user_inp} x {i} = {user_inp * i}')
    print("###################End of table###################")


if __name__ == "__main__":
    user_inp, user_index = accept_input()
    print_table(user_inp, user_index)

