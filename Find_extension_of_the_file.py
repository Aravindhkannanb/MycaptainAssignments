x = input("Input the file name : ")
v = x.split(".")
b=v[-1]

print("The extension of the file {} is {}".format(x,v[-1]))
if(b =='py'):
    print("The Extension of the file is : Python")
else:
    print("bye")
