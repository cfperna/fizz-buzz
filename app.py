# fin

# x = int(input("enter number : "))

# adding some more comment


def fizz_buzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return 'fizz_Buzz'
    if x % 3 == 0:
        return 'Fizz'
    if x % 5 == 0:
        return 'bzz'
    return x


print(fizz_buzz(15))
