def linear_search(arr, target):
    
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

def sort_list(arr, order="asc"):
    
    if order == "asc":
        return sorted(arr)
    elif order == "desc":
        return sorted(arr, reverse=True)
    else:
        raise ValueError("Невірний параметр 'order'. Використовуйте 'asc' або 'desc'.")


data = [5, 2, 9, 1, 5, 6]

target = 5
index = linear_search(data, target)
print(f"Елемент {target} знайдено на індексі: {index}")

sorted_asc = sort_list(data, order="asc")
print("Список відсортований за зростанням:", sorted_asc)

sorted_desc = sort_list(data, order="desc")
print("Список відсортований за спаданням:", sorted_desc)
