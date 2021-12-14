# INPUT_A = [10, 1, 2, 5, 37, 100]

INPUT_A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def get_max_ind_sum(arr, debug=False, print_idx=False):
    maybe_result = {
        True: [],
        False: []
    }

    append_to_chain = True
    max_sum_per_idx = [0 for i in range(len(arr) + 1)]

    for idx, arr_var in enumerate(arr):
        to_append = idx if print_idx else arr_var
        if idx == 0 and arr_var > 0:
            max_sum_per_idx[1] = arr_var
            maybe_result[append_to_chain].append(to_append)
        else:
            should_add = arr_var + max_sum_per_idx[idx - 1] > max_sum_per_idx[idx]
            if should_add:
                max_sum_per_idx[idx + 1] = arr_var + max_sum_per_idx[idx - 1]
                maybe_result[append_to_chain].append(to_append)
            else:
                max_sum_per_idx[idx + 1] = max_sum_per_idx[idx]
                # this line can be cost O(n) but can be implemented as 2way_linked_list
                maybe_result[append_to_chain] = maybe_result[not append_to_chain].copy()
        if debug:
            print("=====================================")
            print(f"first list: {maybe_result[True]}")
            print(f"second list: {maybe_result[False]}")
        append_to_chain = not append_to_chain

    print(maybe_result[not append_to_chain])
    output_sum = sum(maybe_result[not append_to_chain])
    print(output_sum)
    return output_sum


if __name__ == '__main__':
    get_max_ind_sum(INPUT_A, True, True)
