filename=input("Enter the file name: ")
import os
result=os.path.isfile(filename)
if result == True:
    print("The filename which you entered already exist select any one option to perform the action which you need:")
    print("A)Read the file\nB)Delete and start over\nC)Append the file\n")
    option=input()
    if option == "A" or option == "a":
        File=open(filename,"r")
        Read=File.read()
        print(Read)
        File.close()
    elif option == "B" or option == "b":
        os.remove(filename)
        File=open(filename,"w")
        print("A new has been created in its place you can use however you want")
        File.close()
    elif option == "C" or option == "c":
        File=open(filename,"a")
        line=input("Enter the data which you want to insert in the file")
        File.write(str(line))
        print("Your file has been inserted")
        File.close()
    else:
        print("You have entered a wrong option")
else:
    File=open(filename,"w")
    print("The file name you entered dosent exist so we have created it as anew one enter the data which you want to write into your file")
    lines=input("Enter the content which you want to insert into the file:\n")
    File.write(str(lines))
    print("Your content is inserted int the file thank you")
    File.close()