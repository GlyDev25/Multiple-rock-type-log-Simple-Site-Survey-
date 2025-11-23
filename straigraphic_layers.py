total_thickness = 0
grid = ("enter your grid values for this locality")69
print(grid)
northings = (float(input("enter grid Northings value _ N ")))
eastings = (float(input("enter grid Eastings value _ E ")))
outcrops = int(input("how many outcrops? _ "))
for each_outcrop in range(1, outcrops+1):
    layers = int(input(f'how many layers of did you observe in outcrop {each_outcrop}? _'))
    total = 0
    for each_layers in range(1, layers + 1):
        layer_thickness = int(input(f'what is the thickness of layer {each_layers}, found in outcrop {each_outcrop} in meters(m)? _ '))
        total = total + layer_thickness
    print(f'total thickness is {total}m')  