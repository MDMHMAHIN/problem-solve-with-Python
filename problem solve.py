#1 WAP to check if a number entered by the user is odd or even.

number = int(input("Enter a number:"))
rem = number % 2
if (rem == 0): 

    print("The number is Even")

else:
    print("The number is odd")



#2 WAP to find the greatest of 3 numbers entered by the user.

number1 = int(input("Enter the Number1:"))
number2 = int(input("Enter the Number2:"))
number3 = int(input("Enter the Number3:"))

if(number1 >= number2 and number1 >= number3):
    print("Number 1 is Bigest Number :",number1)

elif(number2 >= number3):
    print("Number 2 is Bigest Number:",number2)

else:
    print("Number 3 is Bigest Number:",number3)



#3 WAP to check if a number is a multiple of 7 or not.

