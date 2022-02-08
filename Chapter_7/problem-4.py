num=int(input("enter the Number: "))
prime=True
for i in range(2, num):
    if(num%i==0):
        prime=False
        break
if prime:
    print("THis is Prime")
else:
    print("This is not Prime")    