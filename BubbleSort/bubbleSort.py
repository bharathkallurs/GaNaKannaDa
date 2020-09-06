"""
GaNaKannada: Bubble Sort
Problem: Given an array of integers, sort it in ascending (non-decreasing) 
         order of values from lowest to highest.
Example Input: array = [5, 3, 4, 2, 0, 1]
Example Output: output = [0, 1, 2, 3, 4, 5]

bubble_sort:
Bubble sort has 2 for loops.
The outer for loop runs to maintain the iterations for each array element
The inner for loop runs to compare each of the neighbouring elements
The inner for loop runs n times for each iteration of outer for loop
The if condition inside inner for loop compares neighbouring elements.
If j'th element is greater than (j+1)'th element then swap the 2 elements.
Once all the positions are complete and both for loops finish, the array
will be sorted.


Time Complexity: O(n**2) ==> [read as Big O of n squared]
"""


def bubble_sort(array) -> list:
    """
    Bubble sort function to sort the array in increasing order of elements
    """

    n = len(array)  # get array length

    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j+1]:
                # swap a[i] and a[j]
                array[j], array[j+1] = array[j+1], array[j]

    return array


if __name__ == "__main__":
    # Read the number array from input. Map each number to int datatype
    array = list(map(int, input().strip().split()))

    # Call bubble sort function
    print(bubble_sort(array))
