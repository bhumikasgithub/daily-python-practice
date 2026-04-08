def remove_duplicates(arr):
    unique_list = []

    for i in arr:
        if i not in unique_list:
            unique_list.append(i)

    return unique_list


# Example
arr = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(arr)

print("Array after removing duplicates:", result)