'''Prime number'''
def is_prime(n):
    for num in range(1,n+1):
        count=0
        for i in range(1,num+1):
            if num%i==0:
                count+=1
        if count<=2:
            print(num,end=" ")

n=int(input("enter how many number you want to print"))
is_prime(n)