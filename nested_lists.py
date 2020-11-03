"""
    Author: Frank Olson

    Given the names and grades for each student in a Physics class of N students,
    store them in a nested list,
    and print the name(s) of any student(s) having the second lowest grade.
    
    Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
    
    Input Format:
    The first line contains an integer, N, the number of students.
    The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.
    
    Constraints:
    There will always be one or more students having the second lowest grade.
    
    Output Format:
    Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line
"""
def main():
    # Initialize a dictionary
    names_and_scores = {}

    for _ in range(int(input())):
        name = input()
        score = input()
        names_and_scores[name] = score

    # Initialize variables
    second_lowest_score = sorted(list(set(names_and_scores.values())))[1]
    name_list = []

    for key, value in names_and_scores.items():
        if value == second_lowest_score:
            name_list.append(key)
    
    for name in sorted(name_list):
        print(name)

if __name__ == "__main__":
    main()