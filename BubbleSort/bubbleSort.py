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

ಬಬಲ್ ಸಾರ್ಟ್:
Array data structure ಅನ್ನು ಏರಿಕೆಯ ಅಥವಾ ಇಳಿಕೆಯ (ಆರೋಹಣ ಅಥವಾ ಅವರೋಹಣ) ಕ್ರಮದಲ್ಲಿ ಜೋಡಿಸಲು ಇರುವ ಪದ್ಧತಿಯನ್ನು sorting ಎಂದು ಕರೆಯುತ್ತಾರೆ.
ಈ array ಯನ್ನು ಈಗ ಏರಿಕೆಯ ಕ್ರಮದಲ್ಲಿ ಜೋಡಿಸಲು ಪ್ರಯತ್ನಿಸೋಣ.
ಮೊದಲಿಗೆ ಸಂಖ್ಯೆ 5 ರಿಂದ ಶುರು ಮಾಡಿ ಒಂದೊಂದೇ ಪಕ್ಕದ ಗೂಡಿನ ಸಂಖ್ಯೆಯನ್ನು ಹೋಲಿಸುತ್ತಾ,ಅಂದರೆ compare ಮಾಡುತ್ತಾ ಸಾಗೋಣ.
ಒಂದು ವೇಳೆ ಐದಕ್ಕಿಂತ ಬಲ ಗೂಡಿನ ಸಂಖ್ಯೆ ಚಿಕ್ಕದಿದ್ದರೆ ನಾವು ಆ ಗೂಡಿನ ಸಂಖ್ಯೆಯನ್ನು ಐದೊರೊಂದಿಗೆ ಬದಲಾಯಿಸೋಣ.
ಇದಕ್ಕೆ "swap" ಎಂದು ಕರೆಯುತ್ತಾರೆ. ಒಂದು ವೇಳೆ ಐದಕ್ಕಿಂತಾ ಬಲ ಗೂಡಿನ ಸಂಖ್ಯೆ ದೊಡ್ಡದಿದ್ದರೆ, ಆ ಗೂಡಿನ ಸಂಖ್ಯೆಯನ್ನು ಹಾಗೆ ಬಿಟ್ಟು ಈ ಆವರ್ತನೆಯನ್ನು
(ಅಂದರೆ Iteration) ಮುಗಿಸಬಹುದು. ನಮ್ಮ ಈ ಆವರ್ತನೆಯಲ್ಲಿ 5 ಇಡೀ array ಯಲ್ಲಿ ದೊಡ್ಡ ಸಂಖ್ಯೆಯಾಗಿರುವ ಕಾರಣ, array ಯ ಕೊನೆಯ 
ಗೂಡಿನವರೆಗೂ ನಮ್ಮ ಈ ಹೋಲಿಕೆ ಮಾಡುತ್ತಿರುವ ಆವರ್ತನೆ ಚಾಲನೆಯಲ್ಲಿ ಇರುತ್ತದೆ.


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
