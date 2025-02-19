list1 = [1,2,3,2,1]

copyList1 = list1.copy()
copyList1.reverse()

if(list1 == copyList1):
    print("a palindrome")

else:
    print("Not a palindrome")