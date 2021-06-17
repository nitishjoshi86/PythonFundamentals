#python has functions for crud in files

#open a file  

myfile = open('myfile.txt','w')

#get some info
print('name: ',myfile.name)
print('is closed: ',myfile.closed)
print('opening mode:  ',myfile.mode)

#write to file
myfile.write('This is nitish joshi learning fundamentals of python with help of traversy media')
myfile.write(' and python is cool')
myfile.close()

#append
myfile = open('myfile.txt','a')
myfile.write(' I did some html css projects')
myfile.close()

#read
myfile = open('myfile.txt','r+')
text = myfile.read(200)
print(text)