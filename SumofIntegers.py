#Write a program to find the number and sum of all integers greater than 100 and less than 200 that are divisible by 7.
i=100
sum=0
for i in range(200):
    if i%7==0:
        sum+=i

print(f"Sum:{sum}")