"""
GaNaKannaDa: Stack

Stack is a linear data structure which emphasizes on the order
of pushing and popping data from it. It looks like an array where
data is pushed and popped from a single end. It follows Last In First Out (LIFO)
order of data transfer.
"""
if __name__ == "__main__":
    stack = list()
    stack.append(1)  # insert 1 first
    stack.append(2)  # insert 2 second
    stack.append(3)  # insert 3 last
    print(stack)     # prints data as 1, 2, 3

    # pop one element after another
    print(stack.pop())  # removes 3 first
    print(stack.pop())  # removes 2 second
    print(stack.pop())  # removes 1 last
