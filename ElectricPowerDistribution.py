"""An electric power distribution company charges domestic customers as
follows: Consumption unit Rate of charge:
0-200 Rs. 0.50 per unit
201-400 Rs. 0.65 per unit in excess of 200
401-600 Rs 0.80 per unit excess of 400
601 and above Rs 1.00per unit excess of 600
If the bill exceeds Rs. 400, then a surcharge of 15% will be charged,
and the minimum bill should be Rs. 100/-
Create a Python program based on the scenario mentioned above."""

a=int(input("enter the input"))
if  a<=200:
     price=a*0.50
elif a<=400:
     price=200*0.50+(a-200)*0.65
elif a<=600:
     price=200*0.5+200*0.65+(a-400)*0.85
else:
    price=200*0.5+200*0.65+(a-600)*1.00

if price<100:
     price=100
elif price>400:
    surcharge=price*0.15
    price=price+surcharge

print(f"The total bill price is ${price:.2f}")

