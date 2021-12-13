INPUT_A = [10, 1, 2, 5, 37, 100]

MAYBE_RESULT = {
    True: [],
    False: []
}

append_to_chain = True
MAX_SUM_IN_IDX = [0 for i in range(len(INPUT_A) + 1)]

for idx, arr_var in enumerate(INPUT_A):
    if idx == 0 and arr_var > 0:
        MAX_SUM_IN_IDX[1] = arr_var
        MAYBE_RESULT[append_to_chain].append(arr_var)
    else:
        should_add = arr_var + MAX_SUM_IN_IDX[idx - 1] > MAX_SUM_IN_IDX[idx]
        if should_add:
            MAX_SUM_IN_IDX[idx + 1] = arr_var + MAX_SUM_IN_IDX[idx - 1]
            MAYBE_RESULT[append_to_chain].append(arr_var)
        else:
            MAX_SUM_IN_IDX[idx + 1] = MAX_SUM_IN_IDX[idx]
            MAYBE_RESULT[append_to_chain] = MAYBE_RESULT[not append_to_chain].copy()
    append_to_chain = not append_to_chain

print(MAYBE_RESULT[not append_to_chain])
print(sum(MAYBE_RESULT[not append_to_chain]))
