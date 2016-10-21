

class parent:
    var1='rose'
    var2=34
    var3=var1+str(var2)

class child(parent):
    var2="toast"

pob=parent()
cob=child()
print(pob.var1)
print(pob.var2)
print(cob.var1)
print(cob.var2)
print(pob.var3)
print(cob.var3)

input("<enter>")
