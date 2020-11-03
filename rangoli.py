"""
    Author: Frank Olson

    For a  given an integer, N. Your task is to print an alphabet rangoli of size N.
    (Rangoli is a form of Indian folk art based on creation of patterns.)
"""
def print_rangoli(n):
    from string import ascii_lowercase as chars
    heap = [(('-'.join(chars[i:n])[::-1]+'-'.join(chars[i:n])[1:])).center(4*n-3, '-')for i in range(n)]
    print(*(heap[::-1]+heap[1:]), sep="\n")

def main():
    """
        Main function
    """
    print("Welcome to the Rangoli ascii art.")
    num = int(input("Enter the size of the Rangoli art (1-27): "))

    print_rangoli(num)


if __name__ == "__main__":
    main()