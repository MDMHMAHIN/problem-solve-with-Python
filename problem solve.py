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

x = int(input("Enter a number:"))
if(x % 7 == 0):
    print(x,"multiple of 7")

else:
    print(x,"not multiple of 7")


#4 WAP to ask the user to enter names of their 3 favorite movies & store them in a list.


movies = []

movie1 = str(input("Enter a movie:"))
movie2 = str(input("Enter a movie:"))
movie3 = str(input("Enter a movie:"))



movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)


