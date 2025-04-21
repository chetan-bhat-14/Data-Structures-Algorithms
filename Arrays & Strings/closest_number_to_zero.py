def closest_number_to_zero(input_arr):
    if len(input_arr) == 0:
        return None
    if input_arr is None:
        return None

    # abs(x) ensures closeness to zero
    # -x ensures that positive numbers are preferred when two are equally close (e.g., prefers 2 over -2)
    return min(input_arr, key=lambda x: (abs(x), -x))


if __name__ == '__main__':
    input_arr = [-4 ,-2 ,1 ,4 ,8]
    print('Closest to Zero: {}'.format(closest_number_to_zero(input_arr)))