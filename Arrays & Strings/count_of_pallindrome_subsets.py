# Given a string s, the task is to count all palindromic substring of length more than one.

# Input: s = “abaab”
# Output: 3
# Explanation: Palindromic substrings with length greater than 1, are “aba”, “aa”, and “baab”.

# Input: s = “abbaeae”
# Output: 4
# Explanation: Palindromic substrings with length greater than 1, are “bb” , “abba” , “aea”, “eae”.

def check_pallindrome(s, i, j):
    # Use 2 pointers to check palindromes
    while i < j:
        if s[i] != s[j]:
            return False
        # Increment i to move right (ascending)
        i += 1
        # Decrement j to move left (descending)
        j -= 1
    return True


def countPS(string):
    # Initialize counter to store all counts of palindrome subsets
    pallin_counts = 0
    # Get the first character 
    for i in range(len(string)):
        # Get the second character
        for j in range(i + 1, len(string)):
            # Function takes string indices to check palindromes
            if check_pallindrome(string, i, j):
                pallin_counts += 1

    return pallin_counts


if __name__ == "__main__":
    s = "abaab"
    print(countPS(s))
