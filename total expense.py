print("enter quantity: ")
qty = float(input())

print("enter Rate: ")
rate = float(input())

if (qty>1000):
    dis = 10
expense = (qty*rate)-(qty*rate*dis / 100)
print("\n total Expenses = Rs ", expense)