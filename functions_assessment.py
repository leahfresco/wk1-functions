"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

"""

###############################################################################

# PART ONE: Write your own function declarations.

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', I'd like to visit 'town name here'!" depending on what the function
#        from part (a) evaluates to.

def is_hometown(town):
    """ Determines if town given is Leah's hometown.
    >>> is_hometown("Houston")
    False

    >>> is_hometown("Cupertino")
    True

    """
    # Returns whether town is Cupertino
    return town == "Cupertino"

def full_name(first_name, last_name):
    """ Returns full name from inputs of first and last name.
    >>> full_name("Leah", "Yukelson")
    'Leah Yukelson'

    """
    return first_name + " " + last_name

def greeting(first_name, last_name, home_town):
    """ Prints greeting based on first and last name and home town.
    >>> greeting("Steve", "Jobs", "Cupertino")
    Hi Steve Jobs, we're from the same place!

    >>> greeting("Beyonce", "Knowles", "Houston")
    Hi Beyonce Knowles, I'd like to visit Houston!
    """

    # Greeting if home town matches Leah's home town
    if home_town == "Cupertino":
        print "Hi {} {}, we're from the same place!".format(first_name, last_name)
    else:
        print "Hi {} {}, I'd like to visit {}!".format(first_name, last_name, home_town)        


###############################################################################

# PART TWO

#    (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "raspberry", or
#        "blackberry."

#    (b) Write another function, shipping_cost(), which calculates shipping
#        cost by taking a fruit name as a string and calling the `is_berry()`
#        function within the `shipping_cost()` function. Your function should
#        return 0 if is_berry() == True, and 5 if is_berry() == False.

#    (c) Make a function that takes in a number and a list of numbers. It should
#        return a new list containing the elements of the input list, along with
#        given number, which should be at the end of the new list.

#    (d) Write a function calculate_price to calculate an item's total cost by
#        adding tax, and any fees required by state law.

#        Your function will take as parameters (in this order): the base price of
#        the item, a two-letter state abbreviation, and the tax percentage (as a
#        two-digit decimal, so, for instance, 5% will be .05). If the user does not
#        provide a tax rate it should default to 5%.

#        CA law requires stores to collect a 3% recycling fee, PA requires a $2
#        highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
#        items with a base price under $100 and $3 for items $100 or more. Fees are
#        added *after* the tax is calculated.

#        Your function should return the total cost of the item, including tax and
#        fees.


def is_berry(fruit):
    """Determines if fruit is a berry

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    """
    # Returns whether the string "berry" is within the fruit string
    return "berry" in fruit


def shipping_cost(fruit):
    """Calculates shipping cost of fruit

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    """

    # Returns free shipping cost if fruit is berry, 5 otherwise
    if is_berry(fruit) == True:
        return 0
    return 5

def append_to_list(lst, num):
    """Returns a new list consisting of the old list with the given number
       added to the end.

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    """
    # New list bound to input list
    new_lst = lst
    # Appends the new item, num, to the last index of the new_lst
    new_lst[len(new_lst): len(new_lst)] = [num]
    return new_lst


def calculate_price(base_price, state, tax=0.05):
    """Calculate total price of an item, figuring in state taxes and fees.

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

    """

    total_price = base_price * (1 + tax) # Total price of item with tax
    ca_recycle_percent = 1.03 # CA law requires stores to collect a 3% recycling fee
    pa_highway_fee = 2 # PA requires a $2 highway safety fee
    ma_low_common_fee = 1 # MA has a fee of $1 for items with a base price under $100
    ma_high_common_fee = 3 # MA has a fee of $3 for items $100 or more

    # Calculate total price based on state fees
    if state == "CA":
        total_price = total_price * ca_recycle_percent
    elif state == "PA": 
        total_price += pa_highway_fee
    elif state == "MA":
        if total_price < 100:
            total_price += ma_low_common_fee
        else:
            total_price += ma_high_common_fee
    return total_price


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own.

#    (a) Make a new function that takes in a list and any number of additional
#        arguments, appends them to the list, and returns the entire list. Hint: this
#        isn't something we've discussed yet in class; you might need to google how to
#        write a Python function that takes in an arbitrary number of arguments.

#    (b) Make a new function with a nested inner function.
#        The outer function will take in a word.
#        The inner function will multiply that word by 3.
#        Then, the outer function will call the inner function.
#        Print the output as a tuple, with the original function argument
#        at index 0 and the result of the inner function at index 1.

#        Example:

#        >>> outer("Balloonicorn")
#        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

def append_any_arguments(lst, *args):
    """ Appends any number of additional arguments to the input list and returns
        the entire list.

        >>> append_any_arguments([1, 2, 3, 4], 5, 6, 7, 8)
        [1, 2, 3, 4, 5, 6, 7, 8]

        >>> append_any_arguments(["a", "b", "c"], [1, 2], 3243)
        ['a', 'b', 'c', [1, 2], 3243]

    """
    # Appends each item given within variable number of args
    for item in args:
        lst.append(item)

    return lst # Returns original lst with the appended arguments

def outer(input_word):
    """ Takes in a string and calls inner function multiplies_by_three to
    multiply that string by three and returns a tuple with original string
    at index 0 and the multiplied string at index 1

    >>> outer("Balloonicorn")
    ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

    """
    def multiplies_by_three():
        """ Multiplies a word by three
        """
        return input_word * 3 # Multiplies input string by 3

    # Return a tuple with input string and the output of the function of
    # multiplies_by_three
    return (input_word, multiplies_by_three())
###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
