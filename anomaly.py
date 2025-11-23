concentration_treshold = 250
grid = ("enter your grid values")
print(grid)
northings = (float(input("enter grid Northings value _ N ")))
eastings = (float(input("enter grid Eastings value _ E ")))
concentration = float(input("what is the concentration value of Fe in this point? _ "))
if concentration < concentration_treshold:
    print(f"low concentration value at Point {northings} {eastings}")
elif concentration > concentration_treshold:
    print(f"high concentration value at Point {northings} {eastings}")
    