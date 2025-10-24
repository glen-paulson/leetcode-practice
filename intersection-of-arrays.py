def int_arrays(arr1, arr2):
    set_a = set(arr1)
    res_arr = []

    for item in arr2:
        if item in set_a:
            res_arr.append(item)
            set_a.remove(item)

    return res_arr
