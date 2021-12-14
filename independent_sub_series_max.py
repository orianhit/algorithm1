from treelib import Node, Tree

# INPUT_A = [10, 1, 2, 5, 37, 100]


INPUT_A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def get_max_ind_sum(arr, debug=False):
    tree = Tree()
    tree.create_node("root", "root")

    maybe_result = {
        'A': None,
        'B': None
    }

    append_to_chain = 'A'
    max_sum_per_idx = [0 for i in range(len(arr) + 1)]

    for idx, arr_var in enumerate(arr):
        if idx == 0 and arr_var > 0:
            max_sum_per_idx[1] = arr_var
            tree.create_node(arr_var, idx, parent="root")
            maybe_result[append_to_chain] = idx
        else:
            should_add = arr_var + max_sum_per_idx[idx - 1] > max_sum_per_idx[idx]
            if should_add:
                max_sum_per_idx[idx + 1] = arr_var + max_sum_per_idx[idx - 1]
                parent = "root" if maybe_result[append_to_chain] == None else maybe_result[append_to_chain]
                tree.create_node(arr_var, idx, parent=parent)
                maybe_result[append_to_chain] = idx
            else:
                max_sum_per_idx[idx + 1] = max_sum_per_idx[idx]
                # this line can be cost O(n) but can be implemented as 2way_linked_list
                maybe_result[append_to_chain] = maybe_result['B' if append_to_chain == 'A' else 'A']
        if debug:
            print("=====================================")
            tree.show()
        append_to_chain = 'B' if append_to_chain == 'A' else 'A'

    output_sum = print_output(append_to_chain, maybe_result, tree)
    return output_sum


def print_output(append_to_chain, maybe_result, tree):
    parent = tree.get_node(maybe_result['B' if append_to_chain == 'A' else 'A'])
    print(f"Last tree node (representing reversed root of solution) is: {parent}")
    output_sum = 0
    while parent and parent.identifier != 'root':
        output_sum += int(parent.tag)
        parent = tree.parent(parent.identifier)
    print(f"Max sum is {output_sum}")
    return output_sum


if __name__ == '__main__':
    get_max_ind_sum(INPUT_A, True)
