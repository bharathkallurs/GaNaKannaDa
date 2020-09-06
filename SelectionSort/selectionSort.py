"""
GaNaKannada: Selection Sort
Problem: Given an array of integers, sort it in ascending (non-decreasing)
         order of values from lowest to highest.
Example Input: array = [5, 3, 4, 2, 0, 1]
Example Output: output = [0, 1, 2, 3, 4, 5]

selection_sort:
Selection sort has 2 for loops.
The outer for loop runs to maintain the iterations for each array element
The inner for loop runs to compare minimum most element in the for loop
Once after finding minimum element from inner for loop, swapping of current (i.e, i'th)
element with minimum element takes place.
Once all the positions are complete and both for loops finish, the array
will be sorted


ಉದಾಹರಣೆಗೆ ಮೇಲಿನ ಸಾಲಿನಲ್ಲಿರುವ array ಯನ್ನು ಗಮನಿಸಿ
ಮೊದಲಿಗೆ ಐದರಿಂದ ಶುರು ಮಾಡಿ, ಮಿಕ್ಕೆಲ್ಲ ಗೂಡುಗಳನ್ನು ನೋಡೋಣ.
ಮೂರರಿಂದ ಶುರು ಮಾಡಿ ಕೊನೆಯಲ್ಲಿ ಒಂದರ ವರೆಗೆ ಸೊನ್ನೆ ಅತಿ ಕಡಿಮೆ ಮೌಲ್ಯವನ್ನು ಹೊಂದಿದೆ.
ಇದನ್ನು ಐದರ ಗೂಡಿನೊಂದಿಗೆ swap ಮಾಡಬೇಕು. ಇದೇ ರೀತಿ ಎರಡನೇ ಗೂಡಿನಲ್ಲಿರುವ ಮೂರನ್ನು ಇಟ್ಟುಕೊಂಡು,
ಅದರ ಬಲಕ್ಕಿರುವ ಮಿಕ್ಕೆಲ್ಲ ಗೂಡುಗಳನ್ನು ಹೋಲಿಸುತ್ತಾ ಹೋದಲ್ಲಿ ನಮಗೆ ಸಂಖ್ಯೆ ಒಂದು ಕಡಿಮೆ ಮೌಲ್ಯವಿರುವ ಗೂಡೆಂದು ಗೊತ್ತಾಗುತ್ತದೆ.
ಈಗ ಮೂರನ್ನು ಒಂದರಿಂದ swap ಮಾಡಬೇಕು. ಇದೇ ರೀತಿ array ಯಲ್ಲಿನ ಎಲ್ಲಾ ಗೂಡುಗಳನ್ನು ಹೋಲಿಸಿ array ಯನ್ನು ಪೂರ್ತಿ
swap ಮಾಡಿ ಮುಗಿಸಿದ ನಂತರ selection sort algorithm ಮುಗಿಯುತ್ತದೆ. 

Time Complexity: O(n**2) ==> [read as Big O of n squared]
"""


def selection_sort(array) -> list:
    """
    Selection sort function to sort the array in increasing order of elements
    """

    n = len(array)  # get array length

    for i in range(n):
        min_ele_idx = i
        for j in range(i+1, n):
            if array[min_ele_idx] > array[j]:
                min_ele_idx = j

        # swap a[i] and a[j]
        array[i], array[min_ele_idx] = array[min_ele_idx], array[i]

    return array


if __name__ == "__main__":
    # Read the number array from input. Map each number to int datatype
    array = list(map(int, input().strip().split()))

    # Call selection sort function
    print(selection_sort(array))
