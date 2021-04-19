users_password = input("Create your password:")


class ShortPassword(Exception):
    pass


class NoDigits(Exception):
    pass


class NoDifferentRegisters(Exception):
    pass


class NoSymbols(Exception):
    pass


upper_case = 0
lower_case = 0
numbers = 0
symbol = 0

for i in users_password:
    if i.isupper():
        upper_case += 1
    elif i.islower():
        lower_case += 1
    elif i.isdigit():
        numbers += 1
    else:
        symbol += 1


def strength_checker(password):
    if len(password) < 8:
        raise ShortPassword("Your password is too short!")
    if upper_case == 0 or lower_case == 0:
        raise NoDifferentRegisters("Password has to consist of letters of lower and upper register!")
    elif numbers == 0:
        raise NoDigits("Password has to have at least 1 digit!")
    elif symbol == 0:
        raise NoSymbols("Password has to have at lest one symbol! ")
    else:
        return True


def true_false_checker(password):
    try:
        strength_checker(password)
        if strength_checker(password) is True:
            return True
    except NoDifferentRegisters or NoSymbols or NoDigits or ShortPassword:
        return False


print(true_false_checker(users_password))