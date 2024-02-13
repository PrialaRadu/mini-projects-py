# Application that checks if a year is leap or not, using 2 methods

from calendar import isleap


# Method 1 (without 'calendar' library)
def is_leap_year_manual():
    # Retrieves and validates user input
    while True:
        try:
            year = int(input("Type the year: "))
            if year < 0:
                raise ValueError('Type a positive integer! ')
            break
        except ValueError:
            print('Type a valid integer! ')
    # Checks if the year is divisible by 4, 100 or 400
    return True if year % 4 == 0 or year % 100 == 0 or year % 400 == 0 else False


# Method 2 (using .isleap() function from 'calendar' library)
def is_leap_year_with_calendar():
    # Retrieves and validates user input
    while True:
        try:
            year = int(input("Type the year: "))
            if year < 0:
                raise ValueError('Type a positive integer! ')
            break
        except ValueError:
            print('Type a valid integer! ')
    # Checks if the year is leap using isleap() function
    return isleap(year)
