

fob=open("G:/Computer Programs/Python/fileexpt.txt ",'r' )
listme=fob.readlines()
print(listme)
fob.close()
listme[2]='changing 3rd line of file\n'
fob=open("G:/Computer Programs/Python/fileexpt.txt ",'w' )
fob.writelines(listme)
fob.close()

fob=open("G:/Computer Programs/Python/fileexpt.txt ",'r' )
listme=fob.readlines()
print(listme)
fob.close()

input("<enter>")
