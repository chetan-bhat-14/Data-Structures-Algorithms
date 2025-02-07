# Merge Sort
# Uses Divide and Conquer principle
# Break array into sub-arrays and find the least and combine each combination

def merge_sort(input_array):
    if len(input_array) > 1:
        mid = len(input_array) // 2
        # Take first to mid-elements from input array
        left = input_array[:mid]
        # Take elements from mid to last elements from input array
        right = input_array[mid:]

        # Use recursion
        merge_sort(left)
        merge_sort(right)

        i = j = 0
        k = 0
        # Until we reach either end of the array keep sorting elements
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                input_array[k] = left[i]
                i += 1
            else:
                input_array[k] = right[j]
                j += 1
            k += 1

        # When we run out of the elements from either array, sort the remaining 
        while i < len(left):
            input_array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            input_array[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    arr = [6, 5, 12, 10, 9, 1]
    merge_sort(arr)
    print(arr)
