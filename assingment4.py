myUniqueList=[]
def givingvalues(x):
    global myUniqueList
    if myUniqueList != x:
        myUniqueList.append(x)
        return True
    else:
       return False
givingvalues(5)
givingvalues(4)
givingvalues(3)
givingvalues(2)
givingvalues(1)
print(myUniqueList)