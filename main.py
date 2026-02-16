#Skills Test 3rd Quarter
from pyscript import display, document


def username_verification():
    username = document.getElementById('username').value.strip()
    username_length = len(username)

    if username_length < 7:
        display(
            f'Your username is too short. Add at least {7 - username_length} more character/s to proceed.',
            target='output'
        )
        return False

    return True


def password_verification():
    password = document.getElementById('password').value
    password_length = len(password)
    password_has_number = any(char.isdigit() for char in password)
    password_has_letter = any(char.isalpha() for char in password)

    if password_length < 10:
        display(
            f'Your password is too short. Add at least {10 - password_length} more character/s to proceed.',
            target='output'
        )
        return False

    if not password_has_letter:
        display('Password must contain at least one letter.', target='output')
        return False

    if not password_has_number:
        display('Password must contain at least one number.', target='output')
        return False

    return True


def account_creation(e):
    e.preventDefault() 

    document.getElementById('output').innerHTML = ''

    # get values safely
    username = document.getElementById('username').value.strip()
    password = document.getElementById('password').value
    firstname = document.getElementById('firstname').value.strip()
    lastname = document.getElementById('lastname').value.strip()
    age = document.getElementById('age').value.strip()
    gender = document.getElementById('gender').value

    # VALIDATION: all fields required
    if not all([username, password, firstname, lastname, age, gender]):
        display("Please fill out all fields before signing up.", target="output")
        return

    # username + password rules
    if not username_verification():
        return

    if not password_verification():
        return

    # SUCCESS
    display("Account created. Welcome to the Twisted Spellbound Tournament! You may now log in using your credentials.", target="output")
