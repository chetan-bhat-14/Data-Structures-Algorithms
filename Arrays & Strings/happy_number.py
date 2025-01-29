# A number is called happy if it leads to 1 after a sequence of steps wherein each step number is replaced
# by the sum of squares of its digit that is if we start with Happy Number and keep replacing it
# with digits square sum, we reach 1

# Input: n = 19
# Output: True
# 19 is Happy Number,
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# As we reached to 1, 19 is a Happy Number

# Function to compute squares of each digit using string conversion
def calculate_sq_sum_str(n):
    return sum(int(i) ** 2 for i in str(n))


# Function to compute squares of each digit in a integer
def calculate_sq_sum(n):
    total_sum = 0
    while n > 0:
        # Modulus operation gives the last digit
        digit = n % 10
        # Calculate the square of the digit
        digit_squares = digit * digit
        total_sum += digit_squares
        # Remove the last digit
        n = n // 10

    return total_sum


def happy_number(number):
    seen_set = set()
    # Keep looping until we get 1
    while number != 1:
        number = calculate_sq_sum(number)

        # To check if we have got a cycle
        if number in seen_set:
            return False

        seen_set.add(number)

    return True


if __name__ == "__main__":
    input_number = 202
    res = happy_number(input_number)
    print(res)
