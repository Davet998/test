temperatures=[10,-20,-289,100]

def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f

with open("C:\\git\\test\\temps.txt",'a')as file:
    for t in temperatures:
        print(c_to_f(t))
        file.write("\n"+str(c_to_f(t)))
