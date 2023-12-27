import re

def t2():

    tally = 0

    with open("inputdata.txt", "r") as tiedosto:
        
        for rivi in tiedosto.readlines():

            tally += counter(rivi)

    return tally

            
def counter(rivi):

    max = [0, 0, 0]
    

    pattern = re.compile(r"[:;]")

    result = pattern.split(rivi)
    game = result[0].split(" ")

    for handful in result:
        colors = handful.split(",")

        for color in colors:
            color = color.strip()
            value = color.split(" ")

            if value[1] == "red":
                if max[0] < int(value[0]):
                    max[0] = int(value[0])
                
            elif value[1] == "green":
                if max[1] < int(value[0]):
                    max[1] = int(value[0])

            elif value[1] == "blue":
                if max[2] < int(value[0]):
                    max[2] = int(value[0])

    income = 1

    for num in max:
        income = income * num
    
    return income

    



print(t2())