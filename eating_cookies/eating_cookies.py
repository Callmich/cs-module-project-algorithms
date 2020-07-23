'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    if n < 0:
        return 0
    if n < 2:
        return 1
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3) 


# if there is less than 2 cookies there is only one way to eat it
# I want to set a counter and update it by one two or three recursively until the counter either hits n or goes over it
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
