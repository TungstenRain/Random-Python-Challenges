"""
    Author: Frank Olson

    Without using any string methods, try to print the following:

    123...n

    Note that "..." represents the consecutive values in between.

    Example:
        n=5

    Print the string:
        12345
    
    Input Format:
        The first line contains an integer n
    
    Constraints:
        1 <= n <= 150
    
    Output Format:
        Print the list of integers from 1 through n as a string, without spaces.
"""
from __future__ import print_function

def main():
    """
        Main function
    """
    # Welcome and request user input
    print("Welcome to testing a print function where you submit an integer and we print out all the numbers up to and including that number.")
    n = int(input("Please enter an integer between 1 and 150: "))

    a_list = []
    for i in range(n):
        a_list.append(i+1)

    print(*a_list, sep = "")

if __name__ == "__main__":
    main()