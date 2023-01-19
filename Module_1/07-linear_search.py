"""
Linear search is a simple algorithm that can be used to find an element in a list or an array. It involves iterating through each element in the list or array, one by one, and checking if it is the element we are looking for. If the element is found, the search is stopped, and the index of the element is returned. If the element is not found, the search continues until the end of the list or array, and the value -1 is returned.

Here's an example of the linear search algorithm using the iterative approach:
"""
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [1, 2, 3, 4, 5]
x = 4
result = linear_search(arr, x)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found in the array.")

# output Element found at index: 3

"""
Linear search can also be implemented using the recursive approach. In this approach, the function calls itself recursively until the element is found or the end of the list or array is reached.
"""
def linear_search_recursive(arr, x, i):
    if i == len(arr):
        return -1
    if arr[i] == x:
        return i
    return linear_search_recursive(arr, x, i + 1)

arr = [1, 2, 3, 4, 5]
x = 4
result = linear_search_recursive(arr, x, 0)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found in the array.")
# output Element found at index: 3

"""
It's worth noting that linear search algorithm has O(n) time complexity in the worst case, that means if the element is not in the array/list, it will have to check all the elements in the array, so if the array/list is big it will take a long time.

In short, Linear search algorithm is a simple and straightforward algorithm that can be used to find an element in a list or an array. It can be implemented using the iterative approach or the recursive approach. The iterative approach is more efficient and has the same time complexity as the recursive approach (O(n)) but it
"""
