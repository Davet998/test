planet = input("What planet are you from? ")
print(planet)

def cur_conv(rate,euros):
    dollars=euros*rate
    return dollars

r=input("Enter rate: ")
e=input("Enter euros: ")

print(cur_conv(float(r), float(e)))
