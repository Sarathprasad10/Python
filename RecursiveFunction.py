# Write a recursive function to calculate the sum of numbers from 0 to 10
sum=0
n=0
def CalSum(n):
    if n==0:
        return 0
    else:
        return n+CalSum(n-1)
result=CalSum(10)

print(result)