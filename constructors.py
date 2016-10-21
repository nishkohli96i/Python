
class xyz:
    def apples(self):
        print("apple  pie")

obj=xyz()
print(obj.apples())

class news:
    def __init__(self):
        print("Constructor")
newobj=news()

class xq(xyz):
    y=2

req=xq()
req.apples()



input("<enter>")
