import re

def t2():

    tally = 0

    with open("inputdata.txt", "r") as tiedosto:
        
        for rivi in tiedosto.readlines():

            tally += counter(rivi)

    return tally

            
def counter(rivi):

    

    pattern = re.compile(r"[:;]")

    result = pattern.split(rivi)
    game = result[0].split(" ")

    for handful in result:
        colors = handful.split(",")

        for color in colors:
            color = color.strip()
            value = color.split(" ")


            if value[1] == "green":
                if int(value[0]) > 13:
                    return 0
            elif value[1] == "blue":
                if int(value[0]) > 14:
                    return 0
            elif value[1] == "red":
                if int(value[0]) > 12:
                    return 0

    
    return int(game[1])
    



print(t2())