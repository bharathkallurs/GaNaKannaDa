"""
GaNaKannaDa: Binary Search
Problem: Given an arary of integers, search for an integer given as key.
Example Input: array = [1, 2, 3, 4, 5, 6, 7, 8] key = 6
Example Output: 6 is present in the array

binary_serach:
Run a while loop for the limits left and right indices of the array.
The condition for while loop is to make sure left index is <= right index
Calculate mid variable to get the middle element of the array
Run 3 conditions (if..else ladder) to check if key is present within left and right index.
1. If current array element matches key, return True
2. If key is greater than current array element is greater, set left to mid+1
3. If key is lesser than current array element, set right to mid-1
As left and right indices keep changing, if left becomes greater than right, we exit while loop
Return False, to indicate number not found.

ಇಬ್ಭಾಗ ರೀತಿಯ ಹುಡುಕಾಟ (ಬೈನರಿ ಸರ್ಚ್):

ಒಂದು while ಲೂಪ್ ಅನ್ನು ಎಡ ಮತ್ತು ಬಲ ಎಂಬ ಎರಡು ಸೂಚಕಗಳಿಂದ ಚಲಾಯಿಸಿ.
ಈ while ಲೂಪ್ ಎಡ ಸೂಚಕ ಬಲ ಸೂಚಕಕ್ಕಿಂತ ಕಡಿಮೆ ಅಥವಾ ಒಂದೇ ಇರುವ ತನಕ ಓದುವಂತೆ ಷರತ್ತು ವಹಿಸಿ.
ಈ while ಲೂಪಲ್ಲಿ ಮೊದಲಿಗೆ ಮಧ್ಯದ ಸೂಚಕವನ್ನು ಲೆಕ್ಕ ಹಾಕಿ. (ಎಡ ಮತ್ತು ಬಲ ಸೂಚಕಗಳನ್ನು ಕೂಡಿ, ಉತ್ತರವನ್ನು ಇಬ್ಭಾಗಿಸಿ)
array ಯಲ್ಲಿ ಮಧ್ಯದ ಸೂಚಕ ತೋರಿಸುವ ಗೂಡಿನಲ್ಲಿನ ಸಂಖ್ಯೆಯನ್ನು (ಇದನ್ನು X ಎಂದುಕೊಳ್ಳೋಣ) key ಗೆ ಹೋಲಿಸಿ.
ಸರಿ ಹೊಂದಿದರೆ ಸರಿ (ಅಥವಾ True) ಎಂದು while ಲೋಪಿನಿಂದ ಹೊರ ಬನ್ನಿ.
ತಪ್ಪಾಗಿದ್ದರೆ, ಇನ್ನೆರಡು ಸಾಧ್ಯತೆಗಳಿವೆ.
ಮೊದಲನೆಯದು, ನಾವು ಹುಡುಕುತ್ತಿರುವ key X ಗಿಂತ ಹೆಚ್ಚಿದ್ದರೆ ಎಡ ಸೂಚಕವನ್ನು ಮಧ್ಯ + ೧ ಎಂದು set ಮಾಡಿ.
ಎರಡನೆಯದು, ನಾವು ಹುಡುಕುತ್ತಿರುವ key X ಗಿಂತ ಕಮ್ಮಿಯಿದ್ದರೆ ಬಲ ಸೂಚಕವನ್ನು ಮಧ್ಯ - ೧ ಎಂದು set ಮಾಡಿ.
while ಲೂಪ್ ಬಲಕ್ಕಿಂತ ಎಡ ಸೂಚಕ ಚಿಕ್ಕದಿರುವ ವರೆಗೂ ಚಲಾಯಿಸಿ.

ಒಂದು ವೇಳೆ ಬಲಕ್ಕಿಂತ ಎಡ ಸೂಚಕ ದೊಡ್ಡದಾದರೆ while ಲೋಪನ್ನು ನಿಲ್ಲಿಸಿ ಹೊರ ಬಂದು, ತಪ್ಪು (ಅಥವಾ False) ಎಂದು ಪ್ರೋಗ್ರಾಮಿಂದ ಹೊರ ಬನ್ನಿ.
"""


def binary_search(array, key, left, right) -> bool:
    """
    Binary Search function to check if a key is present in the input array
    """

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == key:
            return True
        elif array[mid] < key:
            left = mid + 1
        else:  # array[mid] > key
            right = mid - 1

    return False


if __name__ == "__main__":
    # Read the number array from input. Map each number to int datatype
    array = list(map(int, input().strip().split()))
    # Read key to be searched in the number array
    key = int(input().strip())

    # Call the linear_search function to find if number is present in array
    left = 0
    right = len(array) - 1  # -1 to get last index of the array

    if binary_search(array, key, left, right):
        print("%d is present in the array" % key)
    else:
        print("%d is not present in the array" % key)
