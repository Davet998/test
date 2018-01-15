file = open("C:\\git\\test\\test.txt",'w')
file.write("Line 1")
file.close()

file = open("C:\\git\\test\\test.txt",'a')
file.write("\nLine 2")
file.close()

with open("C:\\git\\test\\test.txt",'a')as file:
    #file.seek(0)
    file.write("\nLine 3")
#file closes automatically
