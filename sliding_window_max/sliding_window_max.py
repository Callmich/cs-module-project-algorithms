'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # set an answer list
    # for loop length of nums going through the list
    # if there are values in the window nums[x + k - 1]
        # set a temp variable for the string
        # compare the numbers in the temp variable
        # append the largest into the answer list
    finalAnswer = []
    for x in range(len(nums)-k + 1):
        if nums[x + (k-1)]:
            tempArr = []
            tempArr.extend(nums)
            tempArr = tempArr[x:x+k]
            finalAnswer.append(max(tempArr))
    return finalAnswer
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
