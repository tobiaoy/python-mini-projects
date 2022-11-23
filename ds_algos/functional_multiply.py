# we want to make function that multiplies without using the multiply operator
# multiplication is just adding over and over

def multiply(num1, num2):
    # our base case
    if num1 <= 0 or num2 <= 0:
        return 0
    elif num1 == 1:
        return num2
    elif num2 == 1:
        return num1
    # our recursive case
    else:
        ans = num1
        ans += multiply(num1,num2 - 1)
        return ans


if __name__ == '__main__':
    print(multiply(3,9)) # should be 27