a = int(input("Enter your age:"))
#if elif else ladder

if(a>=18):
    print("you are above the age of consent")
    print("Good for you")

elif(a<0):
    print("you are entering an invalid negativ age")

elif(a==0):
    print("you are entering 0 which is not a valid age")        

else:
    print("you are below the age of consent")

print("End of the program")    
