'''
Input: a List of integers where every int except one shows up twice
Returns: an integer 
'''
# Day 1
# def single_number(arr):
#     dic = {}
#     for x in arr:
#         if dic.get(x):
#             dic[x] = 2
#         else:
#             dic[x] = 1
#     key_list = list(dic.keys())
#     val_list = list(dic.values())
    
#     return key_list[val_list.index(1)]

# Day 2
def single_number(arr):
    counts = {}

    for num in nums:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    
    for k, v in counts.items():
        if v == 1:
            return K
    


    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")