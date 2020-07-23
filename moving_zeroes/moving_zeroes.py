'''
Input: a List of integers
Returns: a List of integers
'''
# Day 1
# def moving_zeroes(arr):
#     # Your code here
#     # itterate through the array 
#         # if n == 0 
#             # remove that from the array
#             # add to a 0 counter
#         # else
#             # add to a number counter
#         # add a 0 to the end of the array for each 0
#         # return array and possibly number counter

#     zeroCounter = 0
#     numberCounter = 0
#     zeroArr = []
#     for x in range(len(arr)):
#         if arr[x] == 0:
#             zeroArr.append(x)
#             zeroCounter += 1
#     zeroArr = zeroArr[::-1]
#     for x in zeroArr:
#         del arr[x]
#     for x in range(zeroCounter):
#         arr.append(0)
    
#     return arr

# Day 2
def moving_zeroes(arr):
    if len(arr) < 2:
        return arr
    # initialize a left and right pointer
    # left is 0
    # right is last index in arr
    leftPointer = arr[0]
    rightPointer = arr[1]
    # while left <= right:
    while leftPointer < rightPointer:
        if rightPointer == arr[len(arr)-1]:
            rightPointer = arr[len(arr)-2]
        # if left points at a zero and right points at non-zero
            # swap left and right items in original arr
            # increment left
            # decrement right
        if leftPointer == 0 and rightPointer != 0:
            leftPointer, rightPointer = rightPointer, leftPointer
            rightPointer += 1
            leftPointer += 1
        else:
            # if left is non-zero:
                # increment left
            # if right is zero:
                # decrement right
            if rightPointer == 0:
                rightPointer += 1
            if leftPointer != 0:
                leftPointer += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")