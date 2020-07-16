def binary_recursion(arr, start, end, key):
    if not start < end:
        return -1
    mid = (start + end)//2
    if arr[mid] < key:
        return binary_recursion(arr, mid + 1, end, key)
    elif arr[mid] > key:
        return binary_recursion(arr, start, mid, key)
    else:
        return mid
arr = input('Enter the sorted list of numbers: ')
arr = arr.split()
arr = [int(x) for x in arr]
key = int(input('The number to search for: '))
index = binary_recursion(arr, 0, len(arr), key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))
