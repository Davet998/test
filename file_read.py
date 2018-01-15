file = open("C:\\git\\test\\README.md",'r')
content = file.read()
print(content)
file.seek(0)
content=file.readlines()
print(content)
content = [i.rstrip("\n") for i in content]
print(content)
file.close()
