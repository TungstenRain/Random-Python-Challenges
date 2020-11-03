"""
    Author: Frank Olson

    Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
    You are given n scores. Store them in a list and find the score of the runner-up.

    Input Format:
        The first line contains n. The second line contains an array A[] of integers each separated by a space.

    Constraints:
        2 <= n <= 10
        -100 <= A[i] <= 100

    Output Format:
        Print the runner-up score.
"""
from collections import OrderedDict


def get_runner_up_1(a_list):
    # Remove duplicates
    return sorted(list(set(a_list)))[-2]

def get_runner_up_2(a_list):
    # Remove duplicates
    # Option one: a_set = list(set(a_list))
    return sorted(list(OrderedDict.fromkeys(a_list)))[-2]



def main():
    A = [-100,0,56,25,99,-25]
    print(A)
    print("The runner up is: ", get_runner_up_1(A))
    print("The runner up is: ", get_runner_up_2(A))

if __name__ == "__main__":
    main()