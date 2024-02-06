
from colorutils import Color, rgb_to_hex

def get_complementary_color_rgb(color):
    """Return complementary color of the color passed in RGB format"""
    red   = 255 - int(color[0])
    green = 255 - int(color[1])
    blue  = 255 - int(color[2])
    
    return Color(rgb=(red, green, blue))

def get_complementary_color_hex(color):
    """Return complementary color of the color passed in HEX format"""
    red   = 255 - int(color[0])
    green = 255 - int(color[1])
    blue  = 255 - int(color[2])
    
    return rgb_to_hex(Color(rgb=(red, green, blue)))

if __name__ == "__main__":
    print("Type 'exit' to quit.")
    while True:
        inputed_color = Color(hex=input("\nYour color: "))
        if inputed_color == "exit": break
        
        inputed_color = inputed_color.rgb

        print(f"RGB Complementary Color: {get_complementary_color_rgb(inputed_color)}")
        print(f"HEX Complementary Color: {get_complementary_color_hex(inputed_color)}")
