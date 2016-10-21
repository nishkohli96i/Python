
class dert:
    def createName(self,name):
        self.name=name;
    def displayname(self):
        return self.name
    def saying(self):
        print("hello %s" % self.name )


first=dert()
second=dert()

first.createName('nish')
second.createName('jack')
print(first.displayname())
first.saying()




input("<enter>")
