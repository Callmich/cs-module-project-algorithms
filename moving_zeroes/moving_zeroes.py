'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # itterate through the array 
        # if n == 0 
            # remove that from the array
            # add to a 0 counter
        # else
            # add to a number counter
        # add a 0 to the end of the array for each 0
        # return array and possibly number counter

    zeroCounter = 0
    numberCounter = 0
    zeroArr = []
    for x in range(len(arr)):
        if arr[x] == 0:
            zeroArr.append(x)
            zeroCounter += 1
    zeroArr = zeroArr[::-1]
    for x in zeroArr:
        del arr[x]
    for x in range(zeroCounter):
        arr.append(0)
    
    return arr




if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")