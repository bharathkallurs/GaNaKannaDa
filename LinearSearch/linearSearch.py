"""
GaNaKannaDa: Linear Search
Problem: Given an array of integers, search for an integer given as key.
Example Input: array = [1, 2, 3, 4, 5, 6, 7, 8] key = 6
Example Output: 6 is present in the array

linear_search:
Run a single for loop for the entire array.
Run an if condition inside the for loop to check if key matches any value in array.
Return True if it does, else False

ಸರಣೀಯ ಹುಡುಕಾಟ (ಲೀನಿಯರ್ ಸರ್ಚ್):
ಪೂರ್ತಿ ಸರಣಿಗೆ ಒಂದು for ಲೂಪ್ ಚಲಾಯಿಸಿ.
ಅದರ ಒಳಗೆ ಒಂದು if ಶರತ್ತನ್ನು (condition) ಸೇರಿಸಿ. 
key ಸರಣಿಯ ಯಾವುದಾದರೊಂದು ಸಂಖ್ಯೆಗೆ ಹೊಂದಿದರೆ  ಸರಿ (True) ಇಲ್ಲವಾದರೆ ತಪ್ಪು (False) ಕಳುಹಿಸಿ. 
"""


def linear_search(array, key) -> bool:
    """
    Linear Search function to check if a key is present in the input array
    """
    for i in range(len(array)):
        if key == i:
            return True

    return False


if __name__ == "__main__":
    # Read the number array from input. Map each number to int datatype
    array = list(map(int, input().strip().split()))
    # Read key to be searched in the number array
    key = int(input().strip())

    # Call the linear_search function to find if number is present in array
    if linear_search(array, key):
        print("%d is present in the array" % key)
    else:
        print("%d is not present in the array" % key)
