'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    
    # If x is in the list then remove both items, else return True
    for x in range(len(arr)):
        x = arr.pop(0)
        if x in arr:
            y = arr.index(x)
            arr.pop(y)
        else:
            return x

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")