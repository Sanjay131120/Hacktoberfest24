# Function to partition the array based on the pivot element
def partition(array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements in the range [low, high)
    # Compare each element with the pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If a smaller element is found, swap it with the greater element at i
            i += 1
            array[i], array[j] = array[j], array[i]

    # Swap the pivot element with the element at i + 1
    array[i + 1], array[high] = array[high], array[i + 1]

    # Return the partition index
    return i + 1

# Function to perform Quicksort recursively
def quickSort(array, low, high):
    if low < high:
        # Find the pivot element's correct position
        pi = partition(array, low, high)

        # Recursively sort elements before and after the pivot
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

# Driver code to test the quicksort algorithm
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array:")
print(data)

# Perform quicksort
quickSort(data, 0, len(data) - 1)

print("Sorted Array in Ascending Order:")
print(data)
