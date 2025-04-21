def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    # Whenever the problem includes 2 lists or strings
    # Always use 2 pointers to iterate and track each element from either lists
    i, j = 0, 0
    list1 = []
    # Iterate i and j until reaches each string length
    while i < len(word1) and j < len(word2):
        list1.append(word1[i])
        list1.append(word2[j])
        i += 1
        j += 1

    # If either string is larger than the other
    # Continue to append the elements to the list from each of the string
    while i < len(word1):
        list1.append(word1[i])
        i += 1

    while j < len(word2):
        list1.append(word2[j])
        j += 1

    # Instead of using while for remaining characters use below
    # list1.extend(word1[i:])
    # list1.extend(word2[j:])

    # Join each element in the list as a string
    return "".join(list1)


if __name__ == "__main__":
    print(mergeAlternately("abcdef", "pqr"))
