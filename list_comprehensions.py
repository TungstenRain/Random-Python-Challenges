"""
    Author: Frank Olson

    Let's learn about list comprehensions!
    
    You are given three integers x, y, and z representing the dimensions of a cuboid along with an integer n.
    
    Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k is not equal to n.
    Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z. Please use list comprehensions rather than multiple loops, as a learning exercise.

    Example:
        x = 1
        y = 1
        z = 2
        n = 3

    All permutations of are:
        [[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [0,1,2],[1,0,0],[1,0,1],[1,0,2],[1,1,1],[1,1,2]]

    Print an array of the elements that do not sum to n = 3.
        [[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,2]]

    Input Format:
        Four integers x, y, and z, each on a separate line.

    Constraints:
        Print the list in lexicographic increasing order.
    
    Explanation 0:

    Each variable x, y, and z will have values of 0 or 1. All permutations of lists in the form
        [i,j,k] = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
    Remove all arrays that sum to n = 2 to leave only the valid permutations.
"""
def main():
    """
        main function
    """
    print("Welcome to List Comprehensions where we're going to print out a list of coordinates in lexigraphical order.")
    x = int(input("Please enter an integer for x: "))
    y = int(input("Please enter an integer for y: "))
    z = int(input("Please enter an integer for z: "))
    n = int(input("Please enter an integer for n: "))

    # initialize lists
    x_list = []
    y_list = []
    z_list = []
    
    for i in range(x+1):
        x_list.append(i)
    for j in range(y+1):
        y_list.append(j)
    for k in range(z+1):
        z_list.append(k)

    print([[x, y, z] for x in x_list for y in y_list for z in z_list if (x + y + z) != n])
    

if __name__ == "__main__":
    main()