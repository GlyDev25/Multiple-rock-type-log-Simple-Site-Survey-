sample = []

locality =input("what is the locality number of this location?")
northings = input("enter the northings value of this location _ ")
eastings = input("enter the eastings value of this location _ ")
sample_number = int(input("how many rock sample did you find in this location? _ "))
for each_sample in range(1, sample_number + 1):
    rock_name = input(f"what is the name of rock {each_sample}")
    rock_class = input(f"what category of rock is this rock, is it an igneous, sedimentary, or metamorphic rock? _ ")
    mineral_class = input(f"is rock {each_sample} a felsic rock or mafic rock? _ ")
    if mineral_class == "felsic":
        print("the minerals in this rock are are basically felsic minerals")
        felsic_minerals
    elif mineral_class == "mafic":
        print("the minerals in this rock are basically mafic minerals")
mineral_content = input("what class of rock is this; is it an igneous rock")
