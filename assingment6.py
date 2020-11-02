def draw(x,y):
    if x==5 and y==6:
        for row in range(x):
            if row % 2 == 0:
                for col in range(1,y):
                    if col % 2 == 1:
                        if col!= 5:  
                            print(" ",end=" ")
                        else:
                            print(" ")
                    else:
                        print("|",end=" ")
            else:
                print("---------")
        return True
    else:
        return False
row= int(input("Enter the row value:\n"))
col = int(input("Enter the coloumn value:\n"))
get=draw(row,col)
print(get)