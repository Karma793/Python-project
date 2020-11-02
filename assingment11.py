def draw(x,y):
    try:
        print(x,y)
    except ValueError:
        print("The exception is Value error")
    except IndexError:
        print("There is an index error")
        pass
    except NameError:
        print("There is an name error")
    except RuntimeError:
        print("There is an Run-Time error")
    except MemoryError:
        print("There is an memory error")
    except ReferenceError:
        print("There is an reference error")
    except TypeError:
        print("There is an type error")
    except NameError:
        print("There is an name error")
    except SyntaxError:
        print("There is an Syntax error")
    except KeyError:
        print("There is an key error")
    except Exception as e:
        print(e)
    finally:
        print("There is no error\nThank you")
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