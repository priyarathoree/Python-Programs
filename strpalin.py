'''palindrome , prime , 34 '''
def str_palindrome(str1):
    str2=str1[::-1]
    if str1==str2:
        return ("Palindrome")
    else:
        return ("Not Palindrome")

str1=input("Enter string")
print(str_palindrome(str1))