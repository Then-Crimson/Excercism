"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant below.


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
"""
Module for calculating lasagna preparation and baking times.
Contains functions to calculate remaining and elapsed cooking times.
"""

# Constant for expected baking time
EXPECTED_BAKE_TIME = 40  # minutes

def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining baking time.
    
    Args:
        elapsed_bake_time (int): Baking time already elapsed in minutes
        
    Returns:
        int: Remaining baking time in minutes
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


# Constant for preparation time per layer
PREPARATION_TIME = 2  # minutes per layer

def preparation_time_in_minutes(number_of_layers):
    """Calculate total preparation time based on number of layers.
    
    Args:
        number_of_layers (int): Number of lasagna layers
        
    Returns:
        int: Total preparation time in minutes
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed time (preparation + baking).
    
    Args:
        number_of_layers (int): Number of lasagna layers
        elapsed_bake_time (int): Baking time already elapsed in minutes
        
    Returns:
        int: Total elapsed time in minutes
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.



#TODO: define the 'elapsed_time_in_minutes()' function below.



# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
