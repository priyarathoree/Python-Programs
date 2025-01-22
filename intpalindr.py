'''Palindrome number'''

def is_palindrome(n):
    num=n
    rev=0
    while n>0:
        dig =n%10
        rev=(rev*10)+dig
        n=n//10
    if num==rev:
        return ("Palindrome")
    else:
        return ("Not palindrome")


num=int(input("enter number"))
print(is_palindrome(num))