sub1=int(input("Enter marks of First Subject\n"))
sub2=int(input("Enter marks of Second Subject\n"))
sub3=int(input("Enter marks of Third Subject\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33% in one the the subjects")

elif(sub1+sub2+sub3)/3<40:
    print("You are fail due to total percentage less then 40")
else:
    print("Congratulations You are Pass")

