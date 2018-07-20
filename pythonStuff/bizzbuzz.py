
### my implementation of bizzbuzz

###


def bizzbuzz(num):
    """ Prints bizz if divisible by 3, buzz if divisible by 5

    Prints out bizz if a num divisible by 3 and prints out buzz if divisible by bizzbuzz

    Args num (int): the number you want to print bizzbuzz for
    """
    string = ''
    if(num%3==0):
        string += 'bizz'
    if(num%5==0):
        string += 'buzz'
    #if(string):
    print(string)

"""
x = input('Your number: ')
y=1
while y<=x:
    bizzbuzz(y)
    y+=1
"""

def print_person(first, last, middle=None):
    """Prints out person's names

    This funciton prints out a person's name. It's not too useful

    Args:
        first (str): This person's first name
        last (str): This person's last name
        middle (str): Optional. This person's middle name
    """
    middle=middle or ""
    return '{f} {m} {l}'.format(f=first, m=middle, l=last)
