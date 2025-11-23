limit = 10.0
wells = int(input("input the numbers of wells_ "))
for each_well in range(1, wells+1):
    water_level = int(input(f"what is the depth of the water level in well number {each_well}? _ "))
    if water_level > limit:
        print("safe water level!")
    elif water_level < limit:
        print("the Aquifer is depleting!") 