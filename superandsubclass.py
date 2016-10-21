

class parentclass:
    var1='rose'
    var2=23

class childclass(parentclass):
    var3=235
    pass
    



parentobj=parentclass()
print(parentobj.var1)
childobj=childclass()
print(childobj.var1)
print(childobj.var2)
print(childobj.var3)

input("<enter>")
