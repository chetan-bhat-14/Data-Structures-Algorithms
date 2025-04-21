def max_occurence_digit_count(array):
    # Initalize 2 variables one to hold counts of each digit at each iteration
    # One to get the max value between the already initialized max_count and curr_count
    curr_count = 0
    max_count = 0
    for i in array:
        if i == 1:
            curr_count += 1
            max_count = max(max_count, curr_count)
        else:
            # Re-initialize curr_count to 0 to restart the count
            curr_count = 0

    return max_count


if __name__ == '__main__':
    input_arr = [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1]
    print("Max Occurrence of 1 is : {}".format(max_occurence_digit_count(input_arr)))
