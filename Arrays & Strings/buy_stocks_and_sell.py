def buy_stock(array):
    # Fix a minimum value
    min_value = array[0]
    max_profit = 0
    for i in array:
        # If the value i is less than the min value
        if i < min_value:
            min_value = i
        else:
            # Calculate the profit
            profit = i - min_value
            # Compare the max value with the profit
            max_profit = max(max_profit, profit)

    return max_profit


if __name__ == "__main__":
    input_arr = [7, 1, 5, 3, 6, 4]
    print(buy_stock(input_arr))