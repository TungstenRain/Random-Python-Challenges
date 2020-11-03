"""
    Author: Frank Olson

    Given an integer, n, perform the following conditional actions:
        If n is odd, print "Weird"
        If n is even and in the inclusive range of 2 to 5, print "Not Weird"
        If n is even and in the inclusive range of 6 to 20, print "Weird"
        If n is even and greater than 20, print Not Weird
"""
def weird(n):
    """
        Take an integer, n, and print if it is weird

        n: int
    """
    if (n % 2 == 0) and (n in range(2,6) or n > 20):
        print("Not Weird")
    else:
        print("Weird")


def main():
    print("Welcome to the if-else test.")
    n = int(input("Please provide an integer (1 - 100): "))

    weird(n)


if __name__ == "__main__":
    main()