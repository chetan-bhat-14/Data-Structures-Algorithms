# Given a list of sub-lists, flatten the lists into a single list

def flatten(input_list):
    temp_list = []
    for i in input_list:
        if isinstance(i, list):
            # Recursively call the function
            # the inner results are stored as a CALL STACK (explained below)
            temp_list.extend(flatten(i))
        else:
            temp_list.append(i)

    return temp_list

# The call stack is a special kind of data structure used by Python (and many other programming languages)
# to keep track of function calls. When a function is called, its execution context (including parameters,
# local variables, and the current position) is pushed onto the stack. When the function returns,
# its context is popped off the stack, and the program resumes execution at the point where the function was called.


if __name__ == '__main__':
    list_1 = [1, [2, [3, [4, 5]], 6]]
    final_list = flatten(list_1)
    print(final_list)
