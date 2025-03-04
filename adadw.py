#finding the equation of a line

print("do you want y intercept or x intercept")
option = input("enter 1 for y intersept and  2 for x intercept")


firstcord = input("enter the  first(biggest y cord) cord in format x,y : ")
secondcord = input("enter the  second(lowest x cord) cord in format x,y : ")

firstcord = tuple(map(int, firstcord.split(',')))
secondcord = tuple(map(int, secondcord.split(',')))

rise = int(firstcord[0]) - int(secondcord[0])
idk = int(firstcord[2]) - int(secondcord[2])

gradient = rise / idk

c = int(firstcord[2]) - gradient * int(firstcord[0])
if option == "1":
    print("y={}x + {} ".format(gradient, c))
elif option == "2":
    varibl = ("{}x= y - {} ".format(gradient, c))
    print("with no factorising", varibl)
    y = 1
    withfactorise = c / gradient
    onewithfactorise = y / gradient
    print("x = {}y + {}".format(onewithfactorise,withfactorise))
