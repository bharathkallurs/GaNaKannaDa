"""
GaNaKannaDa: Merge Sort
Problem: Given an array of integers, sort it in ascending (non-decreasing)
         order of values from lowest to highest.
Example Input: array = [5, 3, 4, 2, 0, 1]
Example Output: output = [0, 1, 2, 3, 4, 5]

merge_sort:
Merge sort works on the principle of divide and conquer.
Divide and conquer is one of the important concepts in algorithm design.
We divide the input array into 2 halves by finding the middle point (or mid point).
We recurse through until there is only one element in each of the subdivided arrays.
We will now have a series of Left and Right sub arrays under each recursion.
Once recursion is complete, the actual comparison before merging these elements back happens.
We compare each element from Left sub-array and Right sub-array and add it in increasing order
We go through the entire list of Left and Right subarrays obtained in each recursion.
Length of left and right subarrays decide for a recursion to continue or not.
(Basically to divide the array further or not)

After comparison and adding the elements from left and right sub array to result,
the overall sorted array is obtained:

Time Complexity: O(nlog(n)) ==> [read as Big O of n logarithmic n]
"""


def merge(array, start, mid, end):
    """
    Merge algorithm to divide the array in halves.
    Compare each element from left half with elements on right half.
    Copy back to original array which ever smaller for a given position.
    """
    len1 = mid - start + 1
    len2 = end - mid

    # create temp arrays
    L = [0] * (len1)
    R = [0] * (len2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, len1):
        L[i] = array[start + i]

    for j in range(0, len2):
        R[j] = array[mid + 1 + j]

    i = j = 0
    k = start

    # Run while loop till newly formed arrays
    # are lesser than their assigned lengths. Check L and R above.
    while i < len1 and j < len2:
        # Compare element of L with R.
        # Only if L[i] is less than or equals R[j] increment i
        # Observe j is not incremented as we are only copying
        # smaller elements first to get increasing order.
        # Same logic applies in else but for R[j].
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1

        k += 1

    # Simply copy remaining elements of L
    while i < len1:
        array[k] = L[i]
        i += 1
        k += 1

    # Simply copy remaining elements of R
    while j < len2:
        array[k] = R[j]
        j += 1
        k += 1


def merge_sort(array, l, r) -> list:
    """
    Merge sort function to divide the array into halves in every recursion
    """
    if l < r:
        # find the mid point of the array
        mid = (l + r) // 2
        # Recurse from start (or l) to mid point
        merge_sort(array, l, mid)  # starting to mid
        # Recurse from mid point to end (or r)
        merge_sort(array, mid + 1, r)  # mid+1 to array end
        # Initiate the merge function once the recursion is complete
        merge(array, l, mid, r)

    return array


if __name__ == "__main__":
    # Read the number array from input. Map each number to int datatype
    array = list(map(int, input().strip().split()))

    # Call merge sort function with
    # array, first index of array as 0 and
    # last index of array as length of array - 1
    print(merge_sort(array, 0, len(array)-1))
