def main():
    color = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "beige": "#f5f5dc", "black": "#000000", "BlanchedAlmond": "#ffebcd", "BlueViolet": "#8a2be2", "brown": "#a52a2a", "burlywood": "#deb887", "CadetBlue": "#5f9ea0", "chocolate": "#d2691e"}
    print(color)
    serch_color(color)

def serch_color(color):
    pick_color = input("Enter color: ")
    while pick_color != "":
        if pick_color in color:
            print(pick_color, "is", color[pick_color])
        else:
            print("Invalid color")
        pick_color = input("Enter color: ")

main()