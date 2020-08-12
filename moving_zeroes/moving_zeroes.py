'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    
    ls = []
    
    # append to ls if zero and isnert at start if not
    for x in range(len(arr)):
        if arr[x] == 0:
            ls.append(arr[x])
        else:
            ls.insert(0, arr[x])

    return ls

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")