"""
I did not realise how much I rely on Google and my friends to troubleshoot my broken ideas.
Bouncing things off other people is a big part of my workflow.
This is hard and stressful xD
I feel like I could do so much more work! 
"""
account = {}
user_name = False
username_input = ''
password_input = ''
attempts = 5

def load_file():
    """
    Description: Here is just a simple file read function call. 
    I literally pulled this from the examples, and it worked. KISS for the win.

    Return: I return the read lines as a variable that gets saved once the function is run.
    """
    filename = 'data.txt'
    infile = open(filename, 'r')
    lines = infile.readlines()
    infile.close()
    return lines


def get_account_info(attempts):
    """
    Description: THIS WAS SO HARD!!!!! I had to make the loop STOP as soon as there was a match.
    The idea is that you strip the lines, check the first 2 indexes, if they match pull the account info.
    This should loop the usernam/password prompts endlessly until you get BOTH exact matches.
    I then push everything into a new object to later call the different parts as needed.

    Return: We are just returning True/False to keep the loop running until the inputs are valid.
    """
    for line in file:
        split_line_list = line.rstrip().split(",")
        if username_input == split_line_list[0] and password_input == split_line_list[1]:
            user_username = split_line_list[0]
            user_password = split_line_list[1]
            user_full_name = split_line_list[2]
            user_balance = split_line_list[3]

            account['username'] = user_username
            account['password'] = user_password
            account['name'] = user_full_name
            account['balance'] = int(user_balance)
            return True
    print(f'username and password not found. You have {attempts} left before your account get locked!!!')
    return False

def display_info():
    """
    Description: Here I just run a simple prompt if the user wants to view their account info.
    The idea is that as the "Banking" project gets bigger this will need to be called more often.
    """
    info = input('Would you like to see your account info? ').lower()
    if info == 'yes':
        print(f"Full name: {account['name']} Balance: {account['balance']}")


def balance_input_check(amount):
    """
    Description: Here I just built a function to check if the user input is valid.
    You want this seperate I think if we are modeling SOLID programming? 
    Specifically hitting DIP (Dependency Inversion Principle).
    But I am still trying to wrap my head around SOLID concepts, this was just me trying it.

    Return: We just return the amount to then update the balance total in the object.
    """
    while True:
        if amount.isnumeric():
            return int(amount)
        else:
            print(f'{amount} is not a valid number.')

def balance_update(update_amount):
    account['balance'] += update_amount


while user_name == False:
    attempts -= 1
    username_input = input('Enter username here: ')
    password_input = input('Enter password here: ')
    print(username_input, password_input)
    file = load_file()
    user_name = get_account_info(attempts)
    if attempts == 0:
        print('ACCOUNT HAS BEEN LOCKED')
        exit()

while user_name == True:
    display_info()
    info = input('Would you like to withdraw or deposit money? ').lower()
    if info == 'deposit':
        amount = input('How much? ')
        update_amount = balance_input_check(amount)
        balance_update(update_amount)
    if info == 'withdraw':
        amount = input('How much? ')
        update_amount = balance_input_check(amount)
        if update_amount >= account['balance']:
            print(f"Sorry not enough funds in the account. Your balance is: {account['balance']}")
        balance_update(update_amount * -1)
    display_info()
    log_out = input('Would you like to log out? ')
    if log_out == 'yes':
        exit()
    else:
        user_name = True



"""
Here I want to build out a load function that grabs the lines and
sorts them into objects with key value pairing like:
username: username
password: password
name: full name
balance: account total

Should I make this a class? Example:

class Bank {
    constructor(accountDetails = {username: username, password: password, name: fullName, balance: $$}) {
        this.accountDetails = accountDetails
    }

    setAccountName

}
"""