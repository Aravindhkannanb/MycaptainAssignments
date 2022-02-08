x = input("Input the file name : ")
v = x.split(".")
b = repr(v[1])

print("The extension of the file {} is {}".format(x,b))
if(b[1:len(b)-1]=='py'):
    print("The Extension of the file is : Python")
else:
    print("bye")
