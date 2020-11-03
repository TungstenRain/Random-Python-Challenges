"""
    Author: Frank Olson

    You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

    For Example:
        Www.HackerRank.com → wWW.hACKERrANK.COM
        Pythonist 2 → pYTHONIST 2
    
    Input Format:
        A single line containing a string S.
    
    Constraints:
        0 < len(S) < 1000

    Output Format:
        Print the modified string S.
"""
def swap_cases(s):
    return s.swapcase()

def split_and_join(line):
    return line.replace(" ", "-")

def count_substring(string, sub_string):
    return sum([ 1 for i in range(len(string)-len(sub_string)+1) if string[i:i+len(sub_string)] == sub_string])


if __name__ == "__main__":
    s = "A String is very important!"
    print(swap_cases(s))
    print(split_and_join(s))

    print(count_substring("I am an Indian, by birth.", "Birth"))

    s = "1235"
    t = type(s)
    for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
        print(any(method(c) for c in s))