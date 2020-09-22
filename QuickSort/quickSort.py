"""
GaNaKannaDa: Quick Sort
Problem: Given an array of integers, sort it in ascending (non-decreasing)
         order of values from lowest to highest.
Example Input: array = [5, 3, 4, 2, 0, 1]
Example Output: output = [0, 1, 2, 3, 4, 5]

quicksort:
Quick sort works on the principle of divide and conquer.
Divide and conquer is one of the important concepts in algorithm design.
quick sort partitions the problem array into 2 halves using a pivot element.
First it chooses left most index as left and right most index as right.
Till left is less than right, it partitions the array around a pivot.
It first finds the pivot element using the following steps.
1. set i as low-1 and pivot as last element in the array (or index high)
2. For every element j in the array check if that element is less than pivot.
3. If true in step 2, increment the i variable and swap ith element and jth element.
4. Once the for loop is complete, swap the i+1th element and high index.

Step 4 is carried out because that is the actual position of the pivot.
If you remember we assigned pivot with last element. So pivot now has to be i+1th element.
This value is returned to quicksort function.

Here the array is partitioned to 2 halves from low to pivot's position and
pivot's position to high.

Time Complexity: O(nlog(n)) ==> [read as Big O of n logarithmic n] in best and average case
                 O(n**2) ==> [read as Big of n squared] in worst case scenario.
"""


def qs_partition(array, low, high):
    """
    Find a pivot element by initially setting it to array[high]
    Then find all elements which are lesser than pivot and do the
    swap for those elements with smaller element. Once all the sorting
    is complete, swap the high and i+1 th element to ensure the last
    element is also in order required
    """
    i = (low - 1)
    pivot = array[high]

    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]

    return i+1


def quicksort(array, low, high):
    """
    Quick sort function to recursively establish
    bounds using pivot, low and high. This function
    recursively splits the array into smaller windows
    and there by ensures quick sort is executed within this window.
    """
    if low < high:
        # partition the array to achieve pivot and there by
        # sort by putting smallest element in the array first.
        partition_index = qs_partition(array, low, high)

        # sort elements before and after partition
        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)

    return array


if __name__ == "__main__":
    # Read the number array from input. Map each number to int datatype
    array = list(map(int, input().strip().split()))

    # Call merge sort function with
    # array, first index of array as 0 and
    # last index of array as length of array - 1
    print(quicksort(array, 0, len(array)-1))
