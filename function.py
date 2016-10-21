
def whatsup(x):
    return 'whatsup ' +x
x=input("enter a name ")
print(whatsup(x))

def add(x):
    x=x+10
    return x
     
print(add(12))


def names(first,last):
    print('%s %s' %(first,last))

names('delaney','jane')




def names1(first='kent',last='jones'):
    print('%s %s'% (first,last))

names1()
names1('jon')
names1(last='henry')
    
input("<enter>")
