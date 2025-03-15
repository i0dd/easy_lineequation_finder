#finding the equation of a line

print("do you want y intercept or x intercept")
option = input("enter 1 for y intersept and  2 for x intercept")


firstcordx = input("enter the  first(biggest y cord) cord in format x : ")
firstcordy = input("enter the  first(biggest y cord) cord in format y : ")
secondcordx = input("enter the  second(lowest x cord) cord in format x : ")
secondcordy = input("enter the  second(lowest x cord) cord in format y : ")

rise = int(firstcordx) - int(secondcordx)
idk = int(firstcordy) - int(secondcordy)

gradient = rise / idk

c = int(firstcordy) - gradient * int(firstcordx)
if option == "1":
    print("y={}x + {} ".format(gradient, c))
elif option == "2":
    varibl = ("{}x= y - {} ".format(gradient, c))
    print("with no factorising", varibl)
    y = 1
    withfactorise = c / gradient
    onewithfactorise = y / gradient
    print("x = {}y + {}".format(onewithfactorise,withfactorise))