import sys

from palindrome import check_palindrome

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage:")
        print("python test.py word")
        print("where word is the word to be tested as a palindrome")
        sys.exit(0)

    word = sys.argv[1]
    check_palindrome(word)