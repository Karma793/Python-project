def checker(var1,var2,var3):
    if var1 == var2 or var1 == var3 or var2 == var3:
        return True   
    else:
        return False
num1 = 6
num2 = 5
num3 = int("5")
#here i have used int function to represent a string as an integer so that it can compare the values
result = checker(num1,num2,num3)
print(result)
li=[['a','b']]
print(li[0][0])
li=[['john','doe']]
print(li[-1][-1])
